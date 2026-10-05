# paper_ipm_sop - STE rewrite report (saved by the coordinator from the agent's reply)
Status: DONE. Lint (units) E=0 W=0; rendered E=0 W=0; verify PASS; section gate OK. 213 of 290 units changed (labels 72 of 100).
TN added 101, all used (method, regulation, chemistry, organism, equipment, role/record). TV added: scout, die, destroy.
Number changes: U0230 "Tier 1?" -> "First sign?" (digit 1 gone; text now first/second part); "N percent" -> "N%"; "2+" -> "2 or more". Values unchanged.
Content decisions: PHI expanded once (U0008); EYEBROW keeps "Plant health" to match nav; "lightest control" -> "weakest treatment", "serious" -> "large", "hazardous" -> "dangerous material", "good bugs" -> predators; "mould-risk" link text -> "mold risk"; flow wrap line counts equal original (16-char wrap script); 26 labels exceed +15%; long p units split.
Needs review: dropped "plain-language", "indoor", "records that hold up", cheap/cost, "knockdown", "tougher", "nobody has to guess"; U0022 "monitor, bug, spray, or pull" -> "scout, release, spray, remove" (2-line limit); "reverse" now only in caption U0199; the bar unit " effort" is not extracted and stays non-STE.
Tool feedback: lint accepts `airborne` (= in flight) and `wound` (= past of wind) so R9.2 misses them; SUBSTITUTIONS says "in place of" but lint rejects `place`; no tool checks equal wrap lines before verify.
