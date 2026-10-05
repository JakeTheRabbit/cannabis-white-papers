# paper_co2_enrichment - STE rewrite report (saved by the coordinator from the agent's reply)
Status: DONE. Lint (units) E=0 W=4 ("room is (not) sealed" states a condition = false alarm); rendered E=0 W=4; verify PASS; section gate OK. 241 of 308 units changed (labels 22).
TN added 87 (air/time, plant science, materials, equipment, safety, other). Unused (delete): combustion, ventilation. TV added: none.
Number changes: no digit changes. Vague counts: "a few hundred ppm" -> "two hundred ppm or more"; "tens of percent" -> "ten percent or more"; "tens or hundreds of kilos" -> "ten to many hundred kilograms"; "thousands of ppm" -> "many thousand ppm".
Content decisions: analogies removed (lock and key, accelerator, pump, tank, convoys, dark side); level -> concentration, band -> range, purge -> air exchange, ambient -> outdoor air; 24 units split.
Nuance lost / review: SUB cut to 6 sentences ("mechanism" not named); META "Evidence-linked + safety standards" -> "38 sources"; chronic/acute -> slow/fast; "classic study" -> "primary investigation"; lost "standalone", "forensic", "you pay for". Glossary says "CO2 supplementation"; paper says "CO2 enrichment" (unify).
Tool feedback: ste_verify counts SUB as a paragraph (6 sentences), unit lint does not; R1.2 misses wrong POS: "leaves" (verb), "complete" (adjective), "opposite" (noun), "less" (adverb), "work" (verb).
