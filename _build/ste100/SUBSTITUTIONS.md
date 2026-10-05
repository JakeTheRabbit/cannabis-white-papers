# Frequent non-STE words in this corpus → what to write instead

Source: the Issue 9 dictionary (alternatives) + patterns for words that have no one-word swap.
A swap is only valid if the **meaning stays**. If it does not, change the sentence (Rule 9.1).
Look up anything else with `ste_lookup.py <word>`; `--entry <word>` shows the dictionary page.

## Function words and adverbs

| Avoid | Write |
|---|---|
| every X | each X / all X ("each day") |
| per | for each / each ("for each plant"); inside a unit symbol (mL/h) it is fine |
| any | drop it, or "one", or recast ("If there is a leak" not "If any leak") |
| both | the two |
| never | do not ("Do not let the block dry") |
| so / so that | thus; because; as a result; "to" + verb; "until" |
| still | continue to / stay |
| just | only; (drop it) |
| once | one time; when |
| actually, really, simply, honestly, genuinely, quietly, deliberately | drop the word |
| even (adv) | drop; or "also" |
| often | frequently |
| already | drop; or "in progress" |
| exactly, precisely | accurately; correct; (drop) |
| instead | "Use X in place of Y" / alternative |
| enough | sufficient |
| rather | drop |
| well | correctly; fully |
| now | at this time |
| later | after (this); subsequent |
| likely | possible; "it is possible that" |
| slightly | small ("a small decrease") |
| roughly, about + number | approximately |
| twice | two times |
| evenly | equally; at the same rate |
| upward | up |
| what / why / whether | "the information that", "the reason" is NOT approved; recast. whether → if |
| within | in; "in less than" |
| under | below (position); "less than" (limit); in |
| over | above (position); "more than" (limit); on; along |
| inside / outside | in / inner; external / near |
| toward | to; in the direction of |
| via | through |
| beyond | more than |
| among | in |
| like (prep) | "same as" / drop the comparison |
| vs, versus | "compared with" / "and" |
| either … or | "one of these: …"; or write two sentences |
| whose | recast |

## Verbs and modals

| Avoid | Write |
|---|---|
| should | must (a rule) / "we recommend that you" (advice) |
| may, might | can (possibility) / "it is possible that" |
| would, could | can / will; recast |
| need (to) | "it is necessary to" / imperative / `must` |
| have to | `must` / imperative |
| require(d) | necessary |
| ensure, verify, confirm, establish | make sure (that) |
| avoid | prevent; "do not" |
| allow | let ("lets the water drain") |
| provide | supply; give |
| obtain, achieve, reach, gain | get; (a value) "becomes" |
| maintain | keep; hold |
| reduce, lower (v = ok), lose | decrease |
| rise, raise | increase |
| grow (plant) | "becomes larger" / "increases in size"; growth is a TN |
| run (a controller, a pump) | operate |
| build | assemble; "make" |
| take | get; remove; "need" is not approved; recast |
| carry | transmit; transport |
| leave | keep; let stay; go away from |
| log, watch | record; look at / monitor |
| treat | apply; (a disease) "apply a treatment" |
| use up | recast |
| match | agree with; align |
| inspect | examine |
| indicate, describe, explain | show; give information about; tell |
| understand, learn | know ("you will know how to …") |
| help (noun) | aid |
| begin | start |
| end (verb) | stop |
| happen | occur |
| appear, seem | show; "look" is for eyes |
| produce | make; cause; supply |
| create, generate | make; cause |
| determine, calculate | calculate (approved); find |
| estimate, assess | calculate; examine |
| measure | approved |
| observe | monitor; see |
| consider, assume | think |
| depend on | "if" (recast: "The rate changes if the temperature changes") |
| differ, vary | change; different |
| exceed | "is more than" |
| handle | touch; use; move |
| store | keep; contain (storage is a TN) |
| flush, drain, dry, mix, apply, fill, clean, soak, cut | approved (check the entry) |
| check (v), test (v), damage (v), cover (v) | NOT approved as verbs: "do a check of", "do a test", "cause damage to", "put a cover on" |
| water (v), feed (v), root (v), flower (v), trim (v), clone (v) | nouns only: "apply water to", "apply feed", "make roots", "cut" |
| steer | control; "crop steering" is a listed technical noun |

## Adjectives and nouns

| Avoid | Write |
|---|---|
| big, bigger | large, larger |
| whole, entire | all; full |
| real, true, exact | correct; accurate |
| wrong | incorrect |
| normal, routine | usual; correct |
| fresh | new; clean |
| old | used; remaining; expired |
| early / late (stage) | "first stage", "last stage"; "short" is not time |
| main, major | primary |
| common | same; "frequent" |
| fine | small |
| little, few | small; "a small number of"; "not sufficient" |
| gentle | careful; light |
| extra | more |
| several | some |
| single | one |
| identical | same |
| steady | stable |
| final | last |
| daily, weekly | each day, each week |
| healthy | in good condition (plant: "in good condition") |
| way, method | procedure; method is approved |
| size | TN (listed) |
| reason | because of; cause |
| result | approved (noun) |
| amount | quantity |
| accuracy | precision |
| people | person; personnel |
| action, activity, job | task; procedure; step |
| guide, tip, hint | TN only when it is a document/part; otherwise recast |
| issue, problem | problem is approved; "issue" = TN (document edition) only |
| thing(s) | name the thing |
| part of speech traps | "work" is a noun only; "help" is a verb only; "damage" is a noun only; "test", "check" nouns only |

## Recasting patterns (no one-word swap)

- "X gets hotter" → "X becomes hotter" (BECOME is approved).
- "The roots grow into the block" → "The roots become longer and go into the block."
- "Water drains out" → "Water flows out" (FLOW is approved) / "Water leaves the block through the drain".
- "keep an eye on" → "monitor".
- "make sure you don't …" → "Make sure that you do not …".
- "which means that" → "Thus," / "As a result,".
- "it depends" → state the condition: "If the room is hot, …".
- "the more … the more …" → "When X increases, Y increases."
- "up to 30 °C" → "a maximum of 30 °C".
- "at least 20 minutes" → "a minimum of 20 minutes".
- "a few" → "some" / "a small number of".
- "kind of / sort of" → drop.
- "we'll" / "don't" → "we will" / "do not".
- Passive "is measured every hour" → "The sensor measures it every hour" / "Measure it every hour."
- Gerund "Checking the pH daily prevents …" → "A daily check of the pH prevents …" → ("daily" is not approved:) "A check of the pH each day prevents …".
- "e.g., X, Y" → "for example, X and Y". "etc." → drop or "and other …".

## More replacements found by the pilot rewrites (verified in the dictionary)

| Avoid | Write |
|---|---|
| simple | easy |
| tall, dense, plain | high; high density; only water / (drop) |
| double | two times |
| severe, mild | very bad / dangerous (severe); weak (mild) |
| gentle | careful; light |
| healthy | in good condition |
| choice | selection; alternative |
| switch (v) | set (the switch to …) |
| claim, study, experiment, trial | test (n); recast ("a test shows that …") |
| estimate (v) | recast. The noun `estimate` and the adjective `approximate` are approved |
| scan (v) | examine; for NFC / QR: "read the tag with the phone" |
| reason | because of; cause |
| case | condition |
| place (n, v) | area; position; put |
| link (v) | attach; connect |
| design (v) | recast (have / make) |
| staff, people, team | personnel; person |
| owner, visit, box, path, series, context, idea, rule, meaning, remember, technical | not approved and not technical nouns: recast or name the thing |
| nothing, someone, everyone, anything | "no …", "a person", "all personnel": recast |
| so + adjective + that | "very … ; thus …", or `because` |
| investigation | approved (noun). `Research` is not: use "investigations" or "tests" |
| `~` before a number | `approximately` |

## Approved words with a narrow meaning (read the entry: `ste_lookup.py <word>`)

`push` apply a force to move something away from the source (not "push the plant to flower": say "cause", "give more");
`pull` apply a force toward the source; `move` change position or location (not "the value moves up": "increases");
`get` obtain (never "get hotter / get higher": "become hotter", "increase"); `keep` continue to have or hold; `stay` continue to be in a place or condition;
`give` provide; `show` cause to be seen / be in view; `turn` rotate around an axis (not "turns yellow": "changes color to yellow");
`go`, `come` move to / from a place; `put` cause something to move to a position; `make` manufacture, cause, become;
`let` give opportunity; `fall` move down by gravity (not "temperature falls": "decreases"); `drink` consume liquid (safety text only; plants "absorb" or "use" water);
`know` be sure of data; `see` know with the eyes; `find` discover, examine; `think` have an opinion; `try`; `burn` combustion or heat damage;
`tight` "not free"; `full` at the maximum; `level` (adj) horizontal to a datum, (n) a horizontal line, plane or condition — for a number say "value";
`light` (adj) small mass or weight; `free` can move easily; `high` / `low` large / small value; `long` / `short` length or duration;
`between` related to something before and after in time or position; `with` association, help, or means; `about` concerned with;
`above` / `below` physical position only (limits: "more than", "less than").

## More from the cloning pilot

| Avoid | Write |
|---|---|
| `as` (conjunction) | `when`, `while` or `because` |
| faster, longer, best (adverbs) | "more quickly", "for a longer time", "the most" |
| schedule (noun) | procedure; "times" |
| "a 45° cut" | "cut the stem at 45°" (`cut` is a verb; the noun is only "one complete sequence") |
| within 30 seconds | "in 30 seconds or less" |
| transmit (disease) | `transmit` only means to send a signal or energy. For a disease say "the disease can move from one plant to another" |
| clear plastic | transparent plastic |
| by (classified by) | recast |
| point (= idea) | recast |
| active | recast (use / working) |
| colors and body parts | not in the dictionary: they are technical nouns (already in the shared list: white, brown, yellow, green, red … hand, skin) |
| lower leaves | bottom leaves (`lower` = more low in value; position = `bottom`) |
