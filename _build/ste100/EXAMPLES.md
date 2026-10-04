# Before / after examples (all "after" text is clean under `ste_lint.py`)

Use these to calibrate tone and sentence size. They come from the rockwool paper.

## Lead paragraph (descriptive, 25 words max per sentence)

Before:
> Rockwool (stone wool) is spun rock fibre. It holds no nutrients of its own and reacts with nothing you feed it, so root-zone EC is essentially the EC of the pore water. That makes it the most precise substrate you can steer with. It also means the block has no buffer: get the water wrong and the plant feels it the same hour.

After:
> Rockwool (stone wool) is a fiber of rock. Rockwool does not contain nutrients and does not change the feed. Thus the EC of the root zone is the EC of the pore water.
>
> Rockwool is the most accurate substrate to control, but it has no buffer. If the water content is incorrect, the plant shows the effect in the same hour.

What changed: American spelling (fiber); `holds no … of its own` → `does not contain`; `reacts with nothing` → `does not change`; `so` → `Thus`; `precise` → `accurate`; `steer with` → `control`; the colon sentence became two sentences; `feels it` (figurative) → `shows the effect`; one topic per paragraph (two paragraphs).

## Definition (defterm.body)

Before: `The drop in water content between the daily peak and the next low, caused by the plant drinking and by evaporation.`
After: `The quantity by which the water content decreases from the peak to the next low. The plant uses water, and the air removes water from the block.`

Note: `decrease` is a verb only (the noun is not approved), `drop` and `drinking` are not approved, `caused by … drinking` is passive/gerund. Two short sentences.

## Instruction (imperative, 20 words max)

Before: `Fill the block to saturation, then let it dry back during the day.`
After: `Apply water until the block is full. During the day, the water content decreases.`

(The second sentence is a description of what happens, so it is not an instruction.)

## Safety text (warn/danger callout)

Before: `Never let the block dry below 25% water content, or it will channel and refuse water.`
After: `WARNING-style order first, result second:` `Do not let the water content become less than 25%. A block that is too dry cannot receive water again. The roots become dry and the plant can be defective.`

(`never` → `Do not`; `below` for a limit → `less than`; `will channel` and `refuse` are not approved: say what the block cannot do and what follows.)

## Note and hedge

Before: `Take these numbers with a grain of salt: they come from a handful of trials.`
After: `The data come from a small number of tests. Thus the values are a start point for your room.`

(Idiom removed; the hedge stays; no instruction inside a note.)

## Condition first

Before: `Apply water in two short shots when the slab is dry.`
After: `When the slab is dry, apply water in two short shots. Wait 30 minutes. Then examine the runoff EC.`

## Things the linter cannot see (you must check)

- A word can be on the approved list and still have the wrong meaning in your sentence. Read the entry (`ste_lookup.py --entry word`).
- Pronouns: each `it`, `they`, `this` must have one clear noun to point to. Repeat the noun when in doubt.
- Articles: `the/a/this` before nouns. Not "Remove block from tray" but "Remove the block from the tray."
- Consistent terms: one name per thing across the whole paper (the glossary term).

## More examples (from the pilot rewrites; all lint-clean)

**Caption** (descriptive, citations stay)
- Before: `Coco holds more air at field capacity than peat, so roots get oxygen even when the medium is wet. Exact values vary with the pith-to-chip mix and pot size.`
- After: `At field capacity, coco contains more air than peat. Thus the roots get oxygen when the substrate is wet. The values are not the same for all coco. They change with the ratio of pith to pieces of husk and with the size of the pot.`

**Diagram label** (`label` unit: short, same size)
- Before: `A normal day in coco: VWC drops, then refills` → After: `A usual day in coco: VWC falls, then increases`
- Before: `The plant drinks the pot down through the day, and irrigation refills it back to field capacity.` → After: `During the day, the plant uses the water in the pot. Irrigation fills the pot again to field capacity.`

**Table cells and headers** (fragments become short full statements; no semicolons)
- Before: `After lights-on, before the first shot, no water` → After: `The time after lights-on and before the first shot. You do not apply water.`
- Before: `A short morning dryback that gets the plant drinking before feeding starts` → After: `A short dryback. It makes the plant start to use water before the first feed.`
- Header before: `Push GENERATIVE (flower)` → after: `For GENERATIVE growth (flower)`  (`push` means "apply a force")

**Step title and step body** (imperative, 20 words max; the title stays a short noun phrase)
- Title before: `Flower wk 1–2 (stretch)` → after: `Weeks 1 to 2 of flowering (stretch)`
- Body before: `Steer vegetative: keep VWC high, drybacks small, EC moderate. Build a big, healthy plant and root system.`
- Body after: `Use vegetative steering: keep the VWC high, keep the drybacks small, and keep the EC moderate. Make the plant and the root system large and in good condition.`

**Callout title** (noun phrase or short command, no idiom)
- `Change one thing at a time` → `Change one control at a time`;  `Two numbers, one story` → `Read the two numbers together`.

**Definition with a name that is a code or product** (use the whole name as a technical noun with `--add-tn`): `Home Assistant`, `pause point`, `pencil-whipping` are defined once, then used unchanged.

**What a rewrite often needs that a word swap cannot give** (decide each time): split a long sentence into two; turn a passive into "the system does X"; put the condition first; replace a figure of speech by the mechanism (`drinks the pot down` → `uses the water in the pot`); replace `will` + passive by an imperative or "you can …".
