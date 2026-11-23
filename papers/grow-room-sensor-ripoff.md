---
slug: "grow-room-sensor-ripoff"
title: "THE $6 CHIP INSIDE YOUR $800 BOX"
eyebrow: "Investigative Grow-Room Hardware Exposé"
summary: "How Grow-Tech Brands Sold You Disposable Humidity Sensors, Hid the Chemical Drift, and Let Your Sprays Wreck Your Rooms — Plus the 20-Minute Protocol to Take Back Control."
track: "Environment and climate"
read_time: "~45 min to read"
diagrams: "12 Visual Graphs & Diagrams"
related: ["temp-humidity-vpd", "hvac-dehumidification", "harvest-dry-trim-cure", "signal-and-noise"]
url: "https://www.growlabs.nz/wiki/grow-room-sensor-ripoff.html"
md_url: "https://www.growlabs.nz/wiki/papers/grow-room-sensor-ripoff.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: []
---

# THE $6 CHIP INSIDE YOUR $800 BOX

_Investigative Grow-Room Hardware Exposé · ~45 min to read_

> How Grow-Tech Brands Sold You Disposable Humidity Sensors, Hid the Chemical Drift, and Let Your Sprays Wreck Your Rooms — Plus the 20-Minute Protocol to Take Back Control.

## The $250,000 Contradiction

$6.50 vs. $1,450Bare SHT45-AD1F chip cost vs. retail grow sensors running the same fragile polymer physics
      1 of 17Retail grow brands naming their exact RH chip in their own manual (Ecowitt -EP)
      +10.6% RHReal-world silent drift caught in a licensed flower room (+33.7% VPD with zero alarms)
      ±5% RHTotal width of the ASTM dry-room safe zone (0.55–0.65 aw) between hay & mould

Walk into almost any commercial cannabis facility—or a dialed-in craft grow—and you will see the exact same absurdity: **$100,000 to $250,000+ worth of precision HVAC, dehumidification, and environmental controls taking orders from a $4 to $6 silicon chip hanging directly over the canopy.**

Nobody checks it. Nobody replaces it on a schedule. The dashboard prints `60.2% RH` and `1.06 kPa` to two decimal places, the trend line looks silky smooth, and nobody gets an alarm—so everybody assumes the room is locked in.

**It probably isn't.**

You replace pH electrodes, HEPA filters, carbon scrubbers, and RO membranes on strict schedules because the companies selling them admit they are consumables. Yet the humidity probe steering your entire crop—from a **$9 Govee puck** up to an **$800 Growlink ESM-2** or **$500 Pulse Pro**—is marketed as if it lasts forever.

Here is the ugly reality the grow-tech industry hopes you never look up:

1. **Almost every grow sensor on the market uses the exact same fragile physics:** an exposed microscopic polymer sponge that costs **$2 to $15** (even Sensirion's flagship **SHT45-AD1F** costs **$5.90–$6.90** single-unit and **~$4.16–$4.55** on a factory reel).
2. **Every chip maker explicitly warns that the chemicals you spray ruin these chips.** Sensirion, Texas Instruments, Bosch, TE Connectivity, Silicon Labs, and Aosong all put isopropyl alcohol (IPA), ethanol, hydrogen peroxide (H2O2), acids, ammonia, ozone, and detergents right on their "do not expose / irreversible drift" lists. TI flatly admits that **a single contamination event can add more error than 10 years of normal aging.**
3. **Paying $500 to $800+ for "enterprise" grow sensors like AROYA and Growlink is the biggest ripoff in indoor cultivation.** You aren't buying industrial chemical immunity—you're paying a **75× to 180× markup** on the exact same $4–$6 polymer die, glued inside a proprietary non-serviceable box with **no $20 swappable RH tip** and **no 180 °C chemical purge**. Worse, **AROYA Climate One, AROYA Climate Station, Growlink ESM-2/ClimaLINK, Agrowtek, and Argus Omni all strap an active aspiration fan onto it**—turning your $500–$800 "enterprise" box into a **chemical vacuum cleaner** that sucks ZeroTol fog, IPA fumes, foliar oils, and sulfur straight across the chip every time nobody shuts it down!
4. **Almost no grow brand tells you what chip is inside, how fast it drifts, or when to bin it.** Across 25 grow and greenhouse sensor lines audited from datasheets, manuals, support pages, and FCC internal photos, **only one consumer brand (Ecowitt's `-EP` probe)** names its exact chip in its own docs. Instead, brands quietly hand you a **±10% to ±20% software offset slider**—an accidental confession that their probes wander off a cliff.
5. **You can't fix chemical poisoning with a software offset.** Contamination bends the sensor's response curve, flips the sign of the error across the humidity range, and makes the probe sluggish—or completely "blind."

Figure 1. What you pay vs. the silicon doing the work. High price tags don't buy chemical immunity—they lock a disposable polymer die inside a non-serviceable (or fan-aspirated) box.

#### Real-World Proof: The 10.6-Point Surprise

Figure 2. A dew-point check proved the 10.628% RH gap was a pure moisture-element failure—not temperature. One 20-minute reference swap caught it immediately.

This isn't lab theory. On **September 24, 2026**, inside a licensed commercial flower room in New Zealand (Room F2), a room node running an **M5Stack ENV III (Sensirion SHT30)**—which had lived through routine IPM and room sanitation cycles—was swapped for a brand-new bare **Sensirion SHT45** in the exact same position on the exact same node.

Metric
Old SHT30 vs. New SHT45
What It Meant

**Temperature difference****+0.073 °C** [+0.13 °F]Virtually identical — not a temperature fault
**Humidity difference****SHT30 read +10.628% RH higher**Dew-point check confirmed pure RH element error
**Displayed vs. Actual Room RH**Screen: **60.0%** · True room: **~49.4%**Dehumidifiers were hammering the room 10+ points too dry
**Planned vs. Actual Leaf VPD**Planned: **1.06 kPa** · Actual: **1.41 kPa**Plants were stuck in aggressive dry-back stress (+33.7% VPD)

Nothing alarmed. The graph looked clean, smooth, and believable. For who knows how many weeks, the HVAC and dehumidifiers obeyed every command—steering the room straight to the wrong number. A single fresh reference sensor caught a 10.6-point lie in 20 minutes.

## How Your Sensor Actually Works—And the 5 Ways Your Sprays Break It

#### The Polymer Sponge Inside the Box

Nearly every digital RH probe under a few hundred dollars—and plenty over $500—is a **polymer-capacitive sensor**. Picture two microscopic metal plates (often interdigitated fingers) sandwiching a porous **1–10 µm hygroscopic polymer film**—essentially a microscopic sponge.

- A dry polymer has a low dielectric constant (**εr ≈ 2–6**).
- Liquid/sorbed water has a massive dielectric constant (**εr ≈ 80.1** at room temperature).

When water vapour diffuses into the polymer sponge, capacitance jumps, and the chip converts that into `%RH` using a factory curve.

**The fatal flaw:** Water isn't the only molecule that fits into those pores. Silicon Labs states it bluntly in its datasheet: _"any changes to the dielectric constant of the polymer film will be detected as a change in relative humidity."_ Sensirion puts it even simpler: **the chip cannot tell contaminants from water.**

Not all polymers are built equal:

- **Thermoplastic polymers** (linear/lightly branched chains in cheap dies) have loose free volume—solvents easily swell and permanently rearrange the chains, wrecking calibration for good.
- **Thermoset polymers** (heavily crosslinked networks, like Honeywell HIH, Rotronic Hygromer, or crosslinked polyimides) resist swelling much better—yet active vapours still skew their readings until purged.

Sensirion's Contamination Guide warns that contamination risk scales with **Concentration × Exposure Time × Temperature**. A warm grow room running 24/7 with weekly IPM sprays, IPA wipe-downs, and between-run fogging is literally the worst-case torture chamber imaginable.

Figure 3. Risk scales with Concentration × Exposure Time × Temperature. A warm grow room sprayed every week is worst-case on all three.

#### Busting the #1 Grow-Room Myth: "Dirty Sensors Always Read Wet"

Most growers assume a poisoned sensor always reads too high (wet). **That is dangerously half-wrong.**

Sensirion splits contamination into **surface** (oils, dust, crusts on the outside) and **bulk** (chemicals diffusing _into_ the polymer—"by far the most frequent form"). Once chemicals get inside or coat the chip, there are **five distinct ways your sensor betrays you**:

1. **Flat Offset (The Rare One):** The whole reading shifts up or down uniformly. This is the _only_ failure an app calibration slider can fix—and the _least common_ result of chemical poisoning.
2. **Slope Collapse & The Crossover Trap (The Sneakiest Killer):** Polar solvents like ethanol (εr = 24.5), acetone ($20.7$), IPA ($17.9$), and acetic acid ($6.15$) hydrogen-bond to water's binding sites inside the polymer.

- At **low RH** (where the polymer should be nearly empty), those extra polar molecules _add_ capacitance → the sensor **reads HIGH (wet)**.
- At **high RH** (where water should fill those sites), those contaminants _block_ water (εr ≈ 80) with a weaker dielectric → the sensor **reads LOW (dry)** and loses gain/sensitivity.
- **The Crossover Trap:** Because it reads high at the bottom and low at the top, the poisoned curve _crosses_ the true line right around **50–65% RH**—meaning a wrecked probe can look **100% accurate at one room setpoint** while lying its ass off at lights-off spikes or in a 75% salt bag!
- _Hard lab proof (Honeywell HIH-3602 vapour tests):_ Methanol shifted a sensor **−5.4% RH at 0% RH** and **+39.8% RH at 75% RH**. A 50/50 ethanol/methanol mix shifted **+14.5% at 0% RH** and **−17.4% at 75% RH**—the error completely flipped sign across the range! Similarly, TI's HDC3020 exposed to 65.7% IPA read **+2% at 10% RH** and **−2% at 90% RH**.

1. **High-Humidity Creep (Reversible, But Constant in Grow/Dry Rooms):** Sitting above **80% RH** for days causes water clustering inside the polymer. Sensirion's datasheets admit **+3% RH upward creep after 60 hours >80% RH** on _both_ SHT3x and SHT4x chips (Aosong lists the exact same +3% creep on the AHT20). In Matsuguchi's hot-humid ageing test (40 °C [104 °F] / 90% RH for 1,000 h), a polyimide prototype shifted **+6% RH wet**. Lights-off flower spikes, propagation domes, and wet drying rooms live in this zone.
2. **Surface Fouling, Sluggish Lag & Salt Crusts:** Foliar oils, surfactants, waxes, and dust coat the inlet or membrane. The sensor lags **15 to 60 minutes** behind real humidity swings—reading falsely wet while a room dries and falsely dry while humidity spikes—making dehumidifiers overshoot and hunt non-stop. Worse, TI documents that **ionic salt/condensation residues above 80% RH cause errors often exceeding −10% RH**, and TI's heavy surface-coating smoke test destroyed sensor gain from **+25% down to −50% RH** across the range.
3. **The "Blind Sensor," Delayed Drift & Hardware Corrosion:**

- **Blind Sensor:** Saturate the polymer enough and the output barely moves at all—printing a rock-steady, super-believable `58.4% RH` while measuring nothing.
- **Delayed Drift:** Both Sensirion and Vaisala warn that slow-diffusing contaminants keep creeping into the polymer _after_ exposure ends. A probe can pass inspection the morning after a spray and drift out of spec **a week later**.
- **Corrosion:** Strong oxidizers, bleach/chlorine, and sulfur + night dew corrode copper PCB traces, pins, and silver/nickel electrodes into resistive sulfide crusts (Cu2S, Ag2S) or dead open circuits. TI physically observed **corroded copper traces and pins** in its 4.5% hypochlorite test.

Figure 5. Why single-point app calibration is a trap: in real lab tests, chemical exposure makes the same sensor read HIGH at one humidity and LOW at another.

**Side-Note — Your CO2 Sensor Isn't Safe Either:** While capacitive RH chips are casualty #1, NDIR CO2 sensors also degrade when fogger oils, surfactants, and salt mists coat their internal gold-plated optical mirrors and IR filters. Worse, Automatic Baseline Calibration (ABC) assumes the room drops to ~400 ppm outdoor air regularly—so in sealed CO2-enriched flower rooms, ABC actively masks or corrupts calibration.

## The Grow-Room Chemical Hit List

Here is what you actually spray, wipe, fog, and burn—matched directly against published lab tests and manufacturer compatibility limits.

Grow-Room Product / Source
Active & Hidden Ingredients
How It Wrecks Sensors + Hard Published Data
Typical Drift & Reversibility

**70–99% IPA & Ethanol** (bench wipes, tool dips, hand sanitizer) & **Green Cleaner**Isopropanol, ethanol _(Note: Green Cleaner is soybean oil + SLS + **IPA as inert!**)_Polar –OH groups mimic water (εr = 17.9–24.5). Sensirion: _"irreversibly in most cases."_ Bosch: permanent damage _"very likely."_ TI: _"will always have large impact on RH accuracy."_ **Lab data:** Honeywell 66% IPA liquid soak left **+1.83% RH** at 75% after 60h recovery; ethanol vapour headspace caused **outright failure** (89–893h). Vaisala: standard sensors in IPA vapour drifted **within 24 h**; in 126-day 50,000 ppm IPA test, a rival exceeded 3 pts while Vaisala HMP7 held. TI HDC3020: 862–1,003 ppm ethanol (21d) = +0.7 at 10% / −0.9 at 90%; 8× 30s 65.7% IPA shots = +2 at 10% / −2 at 90%. Rotronic ±2% continuous limit: IPA 4,800–6,000 ppm, ethanol 3,500–5,800 ppm.High at low RH, low at high RH (or erratic). Brief exposure reversible; heavy exposure permanent unless baked.
**ZeroTol 2.0 / SaniDate** (room fogging & sanitation)**27.1% H2O2**, **2.0% peracetic acid (PAA)**Aggressive oxidizers attack polymer backbone + H2O2 gives a _stronger_ capacitive signal than water. Sensirion & TI list H2O2 as irreversible. Vaisala: _"Standard RH sensors are not recommended in vaporized H2O2."_ Even catalytically protected Vaisala **PEROXCAP** reads **+1% RH at 300 ppm** and **+3% at 900 ppm** (23 °C [73.4 °F]), and **unpowered condensing vH2O2 causes permanent failure within 24 hours!** Rotronic limits: H2O2 **90 ppm** (IN-1) / 880 ppm (HH-1); acetic acid 800–1,000 ppm. Vaisala warns even a **180 °C chemical purge cannot remove tiny molecules like acetic acid or methanol!** _(Honeywell liquid Endo-Spor: +0.4/−0.43%; TI 7.35% single liquid shot: ~−1 pt near 90%.)_Wet spikes during dosing; permanent oxidative shift or sensor death.
**Bleach (NaOCl), Hypochlorous Acid (HOCl) & Virkon S**Hypochlorite, chlorine, **21.41% potassium peroxymonosulfate** _(Virkon S is NOT a quat)_Oxidative polymer attack + halogen corrosion of pins, bond wires, and traces. **Lab data:** Rotronic chlorine limit is tiny—**0.7 to 1.5 ppm**! TI's repeated 4.5% sodium hypochlorite challenge **corroded copper traces and pins** and caused massive negative gain. Honeywell hypochlorite soak: **+0.43 / +1.53% RH**. _(Note: No exact drift curve exists for dilute HOCl spray; treat wetting/chlorine mist as high-risk.)_Permanent gain loss, drift, or dead traces.
**Physan 20 & Quats (QACs)****20% quaternary ammonium** surfactantsDon't evaporate cleanly—leave a tacky, hygroscopic surfactant film right over the sensing window that traps moisture. **Lab data:** Detergents are on Sensirion's avoid list. Honeywell Virex quat soak: +0.3 / +0.8% RH; **Kleenaseptic soak: +2.96 / +4.66% RH** after 60h recovery.Persistent **upward (wet)** drift + sluggish response. Permanent.
**Sulfur Burners & Wettable Sulfur**Elemental sulfur dust, SO2 gasDust plugs filters; SO2 + night-time dew/condensation forms sulfuric acid that turns copper/silver contacts into resistive sulfide crusts (Cu2S, Ag2S). **Lab data:** Rotronic limits **5 ppm SO2** (350 ppm H2S). TI 5 ppm SO2 (21d): ~−0.9 pts at 90%. Vaisala confirms sulfur + dew = **irreversible drift**.Erratic drift → corroded, dead probe. Permanent.
**Foliar IPM Oils, Soaps & Bio-Sprays** (**SNS-209**, **Athena IPM**, neem, horticultural oil, pyrethrin foggers, **Regalia**, **Venerate XC**, Ca/Si sprays)Rosemary (10% ext / 0.23% oil), peppermint/lemongrass/geranium oils (1.5% ea + 0.05% citric), neem/soybean oil, fatty acid soaps, _R. sachalinensis_ 5%, heat-killed _Burkholderia_ A396, mineral salts, fogger carriersHydrophobic oils and fogger carriers clog porous membranes/pores; nutrient sprays leave salty hygroscopic crusts. _(No university spray-cycle curve exists, but surface-film pore clogging is established by every maker; TI's severe smoke coating test wrecked gain from +25 to −50 pts.)_ Always check the SDS for hidden solvents/propellants.Severe lag (15–60 min), hysteresis, **downward (dry) bias** from oil blockage or wet spikes from salt crusts. Permanent.
**Late-Flower Terpenes & Off-Gassing Plastics / Silicone / Tape**Monoterpenes, sesquiterpenes, siloxanes, plasticizers, adhesivesLipophilic terpenes partition into the polymer over weeks (Colorado commercial grow studies confirm heavy indoor monoterpene emissions). **Closest long-term test:** Vaisala's **400-day wood-dryer study** (terpenes, acids, alcohols, ketones) drifted standard sensors **>1% at 0% RH and >2.5% at 75% RH** (vs. 0.5% on chemically resistant probe). TI toluene (298–322 ppm, 21d): ~−2 pts at 90%. **Hidden killer:** Rotronic literally puts an exclamation mark on it—**"silicone damages the sensor!"** Sensirion, TI, and Renesas also ban **PE antistatic bags, pink foam, fresh PVC cases, cable ties, tape, and adhesives**.Gradual sensitivity loss, dry bias at high RH, or permanent offset.
**Ammonia (NH3)** (cleaners, decomposing media)NH3 / NH4OHSensirion lists NH3 as irreversible. Honeywell ammonium hydroxide headspace = **outright failure from 89 hours onward** _(Rotronic lists 5,500 ppm within ±2% on industrial elements—polymers/protocols differ)_.Severe permanent drift / failure.
**Ozone Generators (O3)**O3Rapid oxidative destruction of polymer film and micro-electronics. Sensirion, TI, Bosch = irreversible. Rotronic limit: **1.0–1.5 ppm**.Rapid, catastrophic permanent failure.

#### Myth Busted: Stop Blaming Plant Ethylene (C2H4)

Growers love blaming "plant ethylene" for drifting dry-room sensors—especially since a 2022 Clemson / _Cannabis Business Times_ talk noted ethylene is detectable in dry rooms. **Here is the honest science:** across Vaisala, Rotronic, Honeywell, TI, and Sensirion compatibility guides, **there is zero controlled evidence that biological plant ethylene poisons capacitive RH sensors at grow-room concentrations.**

Ethylene (C2H4) is a tiny, non-polar hydrocarbon—just like ethane, methane, propane, and butane, which Rotronic lists as having **no influence** (and TI notes non-polar vapours have negligible dielectric impact). Growers mixed up plant ethylene with **ethylene oxide (C2H4O, EtO)**—a toxic medical sterilant (Rotronic limit: **3 ppm**) that destroys thermoplastic sensors—and **ethylene glycol**. What actually wrecks your dry-room sensor is the heavy terpene cloud, between-batch sanitizers, and days of >80% RH creep—not plant ethylene.

## The Receipts: What the Chip Makers Quietly Admit (And Where Evidence Ends)

If a grow-controller sales rep tells you their sensor handles grow-room sprays just fine, hand them the handling instructions written by the actual engineers who build the silicon inside their box:

- **Sensirion (SHTxx Handling v9 & Contamination Guide v1.1):** Explicitly bans ketenes, acetone, ethanol, IPA, toluene (_"irreversibly in most cases"_), HCl, H2SO4, HNO3, NH3, H2O2, high ozone, adhesives, tapes, and detergents. Its FAQ openly admits **Sensirion provides no chemical sensitivity chart.**
- **Texas Instruments (HDC1080/2080/302x — SDAA445A, SNAA353A, SNIA025, SNAU265D):** Bans alcohols, ketones, acids, H2O2, O3, NH3, formaldehyde, and adhesive off-gassing. States that **one contamination event can add more error than 10 years of normal aging** (up to 10%+ shift), and its clean-air drift spec explicitly _"Excludes the impact of dust, gas phase solvents and other contaminants."_
- **Bosch Sensortec (BME280/680/688 — BST-BME280-HS006):** Warns that toluene, acetone, ethanol, IPA, ketenes, acids, O3, and H2O2 make **"permanent damage of the sensor readings very likely in most of these cases."** And no—the gas-sensing MOX channel on the BME680/688 does _not_ protect its humidity sensor!
- **TE Connectivity (HTU21D/HTU31):** _"Shall not be in contact with volatile chemicals such as solvents or other organic compounds."_
- **Renesas / IDT (HS300x):** Boasts 0.1% RH/yr clean-air drift with silicon-carbide construction, warns against PE antistatic bags, and provides zero spray-cycle durability data.
- **Silicon Labs (Si7021 — now EOL):** Hilariously markets _"immunity to contaminants"_ in one breath while admitting in the datasheet that drift _"May be impacted by dust, vaporized solvents or other contaminants."_
- **Aosong / ASAIR (DHT22/AM2302, DHT20, AHT10/20/21):** Warns _"vapor from chemical materials may interfere with sensitive-elements and debase sensitivity"_ and DHT20 _"output signal may be high if surrounded by volatile solvents."_ Independent tests by Page & Page (`kandrsmith.org`) revealed massive budget scatter and DHT22 sawtooth anomalies; in a 2-year field test, **3 of 6 DHT22s died**, and a greenhouse study measured **3.18% RH RMSE** on DHT22s. _(Bonus: the AHT20 datasheet even has a translation blunder telling you to "dry" the chip at ">75% RH"—do not follow it!)_
- **Vaisala & Rotronic (The Only Grown-Ups in the Room):** Openly publish continuous ppm tolerance tables, warn against standard probes in H2O2, and engineer active chemical-purge heaters and catalytic peroxide layers because they admit polymer physics has hard limits.

#### Keeping It 100% Honest (What the Data Does _Not_ Prove)

A good grower calls BS on hype from _both_ sides—so let's be crystal clear about what the evidence does **not** claim:

- **Every single spray doesn't instantly nuke every probe.** In Honeywell's liquid soak tests, quat, hypochlorite, peroxide, and IPA all recovered to under 2% RH after 60 hours. Rotronic industrial sensors tolerate thousands of ppm of ethanol and IPA within ±2% RH. In Vaisala's 430-day clean outdoor test, all probes stayed under 1% RH. In clean indoor air, hobbyist BME280/HTU21D/Si7021 units stayed stable for years.
- **No peer-reviewed university study has measured exact %RH drift per cannabis spray cycle** (e.g., 10 cycles of ZeroTol 2.0 or 0.5% neem on a TrolMaster vs. Pulse probe). A Met Office review found mostly wet drift outdoors, not sprayed grow rooms.

*_Why does that honesty make the grow-brand ripoff _worse_, not better?** Because every single chipmaker proves the chemicals are dangerous, **nobody has measured the real-world dose in your room**, the error is completely invisible on your dashboard, and **the companies charging you $300–$800 never did the testing and never warned you to check._*

## The Sensirion SHT45 Reality Check: Why "Swiss Chip + PTFE Cap" Won't Save You

Whenever this topic comes up online, somebody immediately chimes in: _"Doesn't apply to me—I run a Swiss Sensirion SHT45 with a PTFE filter cap!"_

Let's be fair: the **Sensirion SHT45** is genuinely the best compact digital RH chip you can buy under $10. Compared to legacy chips, it's in another league:

Sensor Tier
Example Chips
Clean-Air Accuracy (Typ / Max)
Clean-Air Drift
On-Chip Heater
Realistic Grow-Room Life Before >3% RH Drift

**Budget Hobby / Tent**DHT22, AHT20, BME280, SHTC3±2–3% typ (±5% max)~0.25–0.5% / yrNoneWeeks to 1 cycle (often off out of the box)
**Legacy Horticultural**SHT21, SHT30/31, SHT35, Si7021, HTU21D±1.5–2% _(SHT30 was ±3% pre-2022)_Weak ("plausibility check only")1–3 cycles (one bad fog or sulfur burn can kill it)
**Modern High-Precision****Sensirion SHT45-AD1F** _(~$5.90–$6.90 bare; ~$4.16–$4.55 reel; ~$12.50 breakout)_**±1.0% typ (±2.0% max)**; ±0.1 °C [±0.18 °F]; 4 s τ63****20 / 110 / 200 mW** (up to ~110 °C [230 °F])**3–6+ cycles** _if_ protected from sprays & heater used

**Now here are the four uncomfortable truths the hype leaves out:**

**The "Exceptional VOC Resistance" Line Has Zero Grow-Chemical Proof.** Sensirion's datasheet touts _"exceptional resistance to volatile organic compounds."_ We went hunting for the test data behind that claim. For IPA, ethanol, H2O2, PAA, HOCl, quats, or terpenes: **none exists.** The _only_ published chemical test is 20 hours in saturated acetone at 25 °C [77 °F]. Even after two weeks airing out in clean air, **the SHT4x was STILL +3% to +5% RH out of spec!** _(Yes, it crushed two unnamed competitors that were stuck +10% to +30% RH off—which proves it's tougher, NOT immune.)_
**Filter Membranes Stop Droplets—NOT Vapours.** A water vapour molecule is **~0.27 nm** wide. The SHT45-AD1F's filter membrane blocks dust and liquid droplets down to **200 nm** (>99.99% efficiency, unaltered 4 s response). If water vapour walks through those pores, **so do gas-phase IPA, ethanol, H2O2, PAA, HOCl, SO2, and volatile terpenes.** Sensirion literally states the membrane is **"not selectively filtering"** and **"does not in general prevent contamination with volatile chemicals."** TI says the exact same thing about its HDC3022 ePTFE cap. And foliar oil sprays simply glaze over the outside of the membrane.
**The Quiet 2026 Bait-and-Switch (PCN254901): It Might Not Even Be PTFE Anymore!** Under Product Change Notification **PCN254901** (issued Dec 2025, rolling out starting Feb 2026), Sensirion changed the `-AD1F` filter membrane **under the exact same part number (`SHT45-AD1F-R2`, 3.000.886)**:


**Reel IDs `25` and lower:** 100 µm **PTFE (Teflon)**, rated IP67.
**Reel IDs `26` and higher:** 40 µm **Polyimide (PI)**, rated IP68 _(Datasheet V7.3, June 2026, literally says "Corrected PTFE membrane to polyimide membrane")_.
Retailers are _still_ selling breakout boards as "PTFE." Polyimide is still dust/water-tight (IP68), **but it is not a chemically inert fluoropolymer** and has lower resistance to strong caustics and aggressive polar agents. Demand lot/reel confirmation if you care.


**The 200 mW Decontamination Heater Is Almost NEVER Used.** Sensirion's crown jewel on the SHT4x is its high-power internal heater (ΔT ≥ 60 °C):


Pulsing **200 mW for 1 second once per minute** almost completely eliminates high-RH creep at 90% RH (or 200 mW every 2 s for 2 min + 2 min cool for a clean single read).
Running **110 mW for 80 minutes (~110 °C [230 °F])** fully baked acetone back out of flex-mounted SHT4x chips, restoring them to spec.
**The 5 Catches:** (a) **Almost zero commercial grow controllers actually fire this heater cycle** (only DIY/ESPHome setups do!); (b) battery sensors _can't_ fire a 200 mW heater without killing their batteries in days; (c) rigid FR-4 circuit boards without thermal cutouts sink the heat below desorption temperature; (d) running 80 minutes continuous contradicts the datasheet's own 10% max duty cycle; and (e) **NEVER heat a sensor in contaminated air** (it bakes chemicals _deeper_ into the polymer!), and heat **cannot** remove polymerized neem oil, sticky quats, sulfur corrosion, or peroxide-oxidized polymer chains.





  GRAPHIC 8 · THE SHT45 REALITY CHECK: MEMBRANES, PCN254901 & ACETONE TEST




    WHY FILTER CAPS STOP DROPS — NOT FUMES


    SPRAY
    ≥200 nm
    BLOCKED ✓






    200 nm PORES



    H₂O (0.27 nm)

    IPA / EtOH gas

    H₂O₂ / PAA / Terps


    POLYMER DIE BELOW STILL BREATHES EVERY VAPOUR



    2026 BAIT-AND-SWITCH (PCN254901)
    Same part # SHT45-AD1F-R2 (3.000.886):
    • Reel ≤25 = 100 µm PTFE · Reel ≥26 = 40 µm Polyimide





    SENSIRION ACETONE TEST (20h SATURATED)
    Error at 34% RH ref after 14 days in clean air (Fig. 4 est.)

     height 140px (y=248 down from y=108) -->






    +10 to +30%
    2 Unnamed
    Competitors



    +3 to +5%
    SHT4x (No Heat)
    STILL OUT OF SPEC!



    ≤ ±1% ✓
    SHT4x + Heater
    110 mW × 80 min

    The Catch: Almost ZERO commercial grow controllers
    ever run that 80-min heater cycle (and heat can't fix oil/H₂O₂).




**Verdict on SHT45-AD1F:** Best-in-class sensing engine for the money. It buys you tighter starting accuracy, droplet defense, and a shot at self-cleaning _if_ your firmware uses it. **It buys you margin—not immortality.**

## THE WALL OF SHAME: Forensic Breakdown of 25 Grow & Industrial Sensor Brands

We dug through datasheets, user manuals, support KBs, community teardowns, and **public FCC internal circuit-board photos** for 25 sensor lines across every tier of the market.

**Chip Identification Key:** **Confirmed** = vendor doc, press release, or legible hardware proof · **Probable** = credible teardown or strong indirect evidence · **Unknown** = vendor hides it and FCC photos don't show markings.

#### Master 25-Brand Forensic Matrix

Brand / Model
Approx. Price (USD)
RH Element (Evidence)
Spray / Inlet Defense
Stated Accuracy & Clean-Air Drift
Vendor Chemical / Calibration Disclosure
Post-Spray Risk & Replacement Pain

**Govee** H5074 / H5075 / H5179 / H5100~$9–$35**Confirmed SHTC3 / SHT30** _(Sensirion PR; FCC 2AQA6-H5075 unreadable)_**None** (open plastic grille)±3% RH, ±0.3 °C · Drift: NDNone. Offers **±20% app offset**; coin/AAA battery (no heater).HIGH RISK (±5–12% drift in 1–2 cycles). Cheap enough to toss, never run a dry room on one.
**Inkbird** IBS-TH2 / IHC-200 Wi-Fi~$15–$60**Unknown** _(IHC-200: HTG3535CH-class; IBS-TH2 FCC 2AYZD-IBSTH2 shows rubber boot)_**None** (IPX4 splash / slotted plastic)±3% typ, ±4.5–5% max · Drift: NDIBS-TH2 warns _"Do not use alcohol to clean sensor."_ IHC-200 has **±20% `CA` offset**; notorious 89–95% / `"ER"` condensation lockups & 30–60 min lag.HIGH RISK (±5–15%+ drift). Cheap probe (~$15–$25) or whole unit.
**Vivosun** GrowHub E42 / E42A+~$50–$80 _(~$10–$30 probe)_**Probable** SHT-class (_"Swiss-made"_ claim; unverified)Stainless sleeve; **no verified PTFE**Probe: **±5–6% RH**, ±0.8 °C · GrowHub sheet typo: **`"±0.6 %PH"` (sic)** · Drift: NDZero chemical disclosure; manual covers CO2 cal only. 4–8% unit-to-unit spread brand new; severe night-cycle non-linear drift.HIGH RISK (±6–20% drift). Wide factory error leaves zero margin.
**Spider Farmer** GGS / GGS Pro~$50–$90 (kits)**Unknown** (budget capacitive)Connector cap only; inlet **unknown**±3% RH · Drift: NDZero chemical disclosure; infamous night-cycle non-linear drift; firmware gives a **±20% RH offset**!HIGH RISK (±6–20% drift). Cheap probe (~$15–$30) swap.
**Ecowitt** WH31 / WN31 vs. **WN31EP / WH31-EP**~$11–$20 std / ~$30–$45 `-EP`Std: **Probable SHT30** · `-EP`: **Confirmed Sensirion SHT35** _(vendor manual!)_Std: None · `-EP`: water-resistant capsule (membrane ND)Std: ±5% · **`-EP`: ±1.5–1.8%** · Drift: ND**ONLY consumer brand naming its exact RH chip (`-EP`).** Console offset; no chemical-exposure rating.HIGH RISK (std) / MEDIUM (`-EP`). Great chip, cheap swappable probe.
**AC Infinity** Controller 69 Pro / AI+ UIS Probes~$50–$70 ctrl · **$16–$25 probe****Probable SHT30/3x/4x** _(grower.ch microscope/I2C teardown; FCC 2AXMF-CTR69A controller PCB only)_SAE 316 stainless tube + potted PCB + gasket (AI+); **shipping cap must be removed**; no verified vapour shield or heater purge**Often unlisted!** Users report ±3–6% spread & probes reading ~10 pts highApp offset **−8/+8% or −10/+10%**. Zero chemical or drift disclosure.HIGH RISK (±3–10% drift). **Silver lining:** cheap $16–$25 plug-in swap—treat as disposable!
**SensorPush** HT1 / HT.w / HTP.xw~$50–$55 / ~$70 / ~$90–$100**Probable** _(HT1: Si7021-class, FCC 2AL9X-HT1 low-res; .w/.xw: SHT35/45-class)_HT1: open vents · **.w/.xw: O-ring + ePTFE membrane**±3% / ±2% / **±1.5%** typ _(±4.5% max on HT1/.w)_ · Drift: NDHonestly discloses **+3% reversible offset >80% RH** & salt-bag cal (48–72h). Zero chemical spec; **coin-cell battery = no heater purge**.HIGH RISK (HT1) / MEDIUM (.w/.xw: ±2–6% vapour drift). Non-swappable—must toss **$100 puck**.
**Pulse Grow** One / Pro / Hub THV-1~$149–$199 / ~$420–$499 / ~$69–$99 probe (base extra)One: **Confirmed Sensirion family** _(part hidden)_ · Pro: _"Swiss & Austrian"_ (**Unknown**) · THV-1: **Unknown**Vented plastic body; **no IP67 PTFE cartridge**One: ±3% _(or ND)_ · **Pro: ±1.5% on sales page vs ±3% on tech-spec page!** · **THV-1: ±5%** · Drift: _"good temporal stability"_App offset; support admits if it won't calibrate it _"may be damaged"_ → replace. Zero chemical spec.HIGH RISK (±4–12% drift). **BRUTAL PAIN:** No swappable RH tip on One/Pro—throw away a **$200–$500 unit**!
**TrolMaster** MBS-TH (3-in-1) / MBS-PRO (4-in-1)~$79–$120 / ~$250–$350**Probable SHT3x/4x** _(wired, no FCC filing)_Slotted plastic box; **NOT waterproof**; no heater purge**MBS-TH: ±7% RH!!** · MBS-PRO: ±3% RH · Drift: NDOne of the _only_ brands with a spray warning: _"Do not spray foreign substances or allow water/condensate."_ Offset KB; contamination routinely denied warranty.HIGH RISK (±5–15%+ drift; infamous `r/macrogrowery` deaths after ZeroTol & sulfur). **$80–$350 whole-unit replacement!**
**AROYA Climate One** _(Aspirated Station)_Quote only _(~$500+ / ~$5,000 AROYA GO starter bundle + SaaS!)_**Unknown** _(exact chip & inlet membrane undisclosed)_**Active fan pulling 0.2 m³/min (~7.1 CFM) 24/7** (vacuums 288 m³/day of air—and every spray/fog—straight onto sensor!)**±3% RH (20–80% only!)**, **±0.7 °C [±1.26 °F]** · Drift: NDMarkets _"research-grade ground-truth"_ while hiding chip, membrane, drift & pricing; zero spray-cycle validation, no thermal purge.HIGH RISK (±3–8%+ drift if 7.1 CFM fan runs during IPM/ZeroTol/IPA). **Enterprise ripoff + spray vacuum!**
**AROYA Climate Station** _(METER ATMOS 14 Gen 2)_~$340–$500+ / Quote**Probable Sensirion CMOSens** _(METER docs)_**Aspirated fan housing** + **porous Teflon (PTFE) screen**RH-dependent curve · **±0.25%/yr** (Gen 2)**Best manual in cannabis:** METER explicitly discusses suspected solvent damage, PTFE screen care, Gen-2 board swap & ~$100–$120 recal.MEDIUM — PTFE blocks droplets, **but fan still pulls IPA/H₂O₂/terpene fumes straight through PTFE** unless shut off.
**Growlink** ClimaLINK / ESM-2 / ESM-3~$299–**$799 standalone (ESM-2)****Unknown** (commercial capacitive)**Aspirated multi-sensor box**; filter NDClaims ±1–2% _(spec sheet literally has **"TBD"** fields!)_ · Drift: ND1-yr warranty; zero chemical endurance spec; relies on **GrowlinkOS software offsets**.HIGH RISK (±3–10%+ if aspirated during sprays). **BRUTAL PAIN:** No cheap RH tip—**$799 box** at risk!
**Agrowtek** SXC / SXC+ / SXE / SXHM~$300–$600+ _(~$319 SXC)_**Unknown** (CMOS polymer)**6 CFM fan + open-cell foam dust filter**±2% typ / ±4% max _(0–80% RH; **80% max continuous!**)_ · Drift: NDGood: cal wizards & stores last cal date. Bad: zero vapour defense—**soaked foam filter acts as a chemical sponge**, off-gassing sprays onto the chip for _days_!MED–HIGH (±5–12%+ if fan runs during sprays). Modular assembly swap, not chip-swappable.
**Grow Sensor PRO**Quote**Confirmed SHT45 family** _(exact suffix/filter ND)_Unknown**±1% typ (10–95%)** · Drift: _"minimal"_ (no number)Good component transparency & factory chamber cal; still no public post-spray test.HIGH RISK until filter lot & post-spray protocol verified.
**Grodan** GroSens Climate~$1,000–$1,450+ (sys)**Unknown** _(FCC 2AUKP-CL002: unmarked DFN behind rear vents; older units rootzone-only)_IPX4 splash housing; no inlet filter**±4.5% to ±8% RH!!** · Drift: NDWorst commercial transparency; specs locked behind dealer/e-Gro portal; zero sanitation spec.HIGH RISK. Shockingly wide ±4.5–8% factory tolerance for a $1,000+ ecosystem.
**Link4** iPonic 624 / Pearl DISM / I2C DTH / iGrow~$250 (DTH) / ~$430–$529 / **~$767 (DISM)****Confirmed Sensirion CMOSens** on I2C DTH _(exact chip ND)_Radiation shield / aspirated opt.; inlet filter ND±2–3% RH _(1–3%/yr greenhouse baseline)_Legacy iPonic discontinued; enclosure rating doesn't protect external probe; minimal spray spec.MED–HIGH (±4–12%+ under sulfur/oxidizers). Expensive proprietary module.
**Autogrow / Bluelab** IntelliClimate / EnviroSensor~$300–$400 / **~$830–$980****Unknown**Unknown±2% RH, ±0.5 °C · Drift: NDDual sensors advised >6.1×6.1 m; **no RH cal in EnviroSensor manual** (whole sensor replaced); zero spray spec.MED–HIGH. Nearly **$1,000** hanging unprotected if unbagged.
**Quest & Anden Dehumidifiers** (Onboard & A77)~$30–$80 harnessStandard HVAC capacitive polymer**ZERO** — sits directly in **hundreds of CFM** of sticky return airflow!±3–5% RH · Drift: NDNone. Routinely drifts **5–15%+ RH** in 1 year, fights your main controller, short-cycles, or throws **Quest `E1` fault**.HIGH RISK. **Never trust onboard dehu sensors!** Bypass via external dry-contact controller.
**Onset HOBO** MX2301A _(Ref)_ / **Davis Vantage Pro2**~$220–$230 (HOBO)HOBO: **Unknown** · Davis (2016+): **Confirmed SHT31**Weatherproof replacement caps (HOBO)±2.5% RH, Optional NIST cert; no chemical vapour spec; Davis requires board swap.MEDIUM. Weatherproof ≠ chemical-proof.
**Aranet** TDSPT802 / Heavy Duty / TDSPT409~€100–$200+**Probable SHT-series**IP67 + **PTFE membrane** + ammonia-resistant variant±2% RH · **0.5%/yr "at lab conditions"****BEST chemical disclosure in grow market:** _"Exposure to VOCs, acids or bases, etching substances such as H2O2, NH3, shall be avoided."_ Replaceable probe.MEDIUM (±2–7% vapour drift). Battery wireless = no heater purge.
**Argus Controls** Titan SEN-OSM vs. **SEN-RHT**~$400–$900+**Confirmed field-replaceable NIST `SUB-RHT-RST` tip** _(die OEM ND)_Solar shield; OSM aspirated**±2% RH** (10–90%, ±3% >80%) · Drift: NDRefreshingly honest: warns aspirated Omni is for _"clean ambient air"_ and **not >80% RH or fog**; sells swappable NIST tips for harsh zones.LOW–MED (SEN-RHT). **Correct modular architecture.**
**Priva** Classic Wet/Dry Bulb vs. **E-Measuring Box SPE**~$500–$1,200+**Classic: Confirmed dual 3 kΩ NTC wet/dry bulb (ZERO polymer!)** · E-Box: CapacitiveAspirated + air filter; cotton wick + Aquanex water (Classic)Psychrometer ~±1–2% · E-Box ±2%**Classic:** 0% polymer VOC drift! (Oils/algae foul wick instead; ~$5 swap.) **E-Box:** Dealers explicitly mandate **annual plug-in sensor & filter replacement!**LOW RISK (maintained psychrometer or annual E-Box swap).
**Hoogendoorn** iSii / IIVO Measuring Box~$600–$1,500+**Confirmed PT500 dry/wet bulb** (default) or electronic opt.Aspirated + air filterIndustrial gradePublishes wick, water, comparison & cal procedures; **preventive maintenance at least annually**.LOW RISK (psychrometer) / MEDIUM (electronic).
**Vaisala** (HMP110/HMP7/HM40/PEROXCAP) · **Rotronic** (HC2A-S/HP32) · **E+E****$400–$2,600****HUMICAP 180R/RC / PEROXCAP** · **Hygromer HH1-SK** · **E+E ChemShield**Sintered/PTFE + **160–180 °C chemical purge** + **catalytic H2O2 breakdown** + E+E 24h ARC heat/coating**±0.8% to ±1.5% RH** · **Gold standard:** publishes full ppm limits, weekly chemical purge, and **field-swappable INTERCAP/HUMICAP cartridges**.LOWEST (<1–3%) when purged. Still not invincible to heavy oil/sulfur crusts.
**DIY / Open Hardware** (M5Stack ENV III/IV · Adafruit SHT45 #5665)**$12.50–$20****Confirmed SHT30 / SHT40 / SHT45**Optional PTFE/PI cap±2% / ±1.8% / **±1.0% RH**Full chip transparency, cheap swap, and **ESPHome actually lets you run SHT45 heater purges & anti-creep pulses!**BEST DIY — best DIY reference & modular node.





  GRAPHIC 9 · THE ASPIRATION FAN TRAP & THE PRICE-VS-HONESTY MAP




    HOW ASPIRATED FAN BOXES POISON THEMSELVES
    AROYA Climate One (7.1 CFM!) · Growlink ESM · Agrowtek (6 CFM)



    ZeroTol / Oil
    IPA / Sulfur






    Foam / PTFE
    (vapour walks in!)


    $4 CHIP



    7.1 CFM
    FAN

    AROYA sucks 288,000 L/day (0.2 m³/min)! Leave the
    fan on during sprays = $500–$800 chemical shop-vac!





    PRICE VS. FACTORY TOLERANCE (OUT OF THE BOX)
    Paying more does NOT guarantee tighter accuracy or swappable tips




    ±0%
    ±4%
    ±8%
    $0
    $500
    $1,000
    $1,500


     (451, 221) -->
    SHT45 ($13, ±1%)
     (470, 213) -->
    HTP.xw
     (467, 121) -->
    TrolMaster MBS-TH (±7%!)

    Pulse Pro ($499)
    AROYA Climate One ($500+, Fan)
     (624, 205) -->
    Growlink ($799)
     (690, 225) -->
    Vaisala/Rotronic
     (767, 108) -->
    Grodan ($1,450, ±8%!)
    Green = Swappable / Transparent · Red/Orange = Wide spec or sealed box




🚨 The Enterprise Ripoff Spotlight: AROYA & Growlink
If you want to know how badly commercial cultivators are getting fleeced, look no further than the two biggest "enterprise" names hanging in multi-million-dollar facilities: **AROYA** and **Growlink**.

**Growlink ($299 ClimaLINK → $799 standalone ESM-2) — $800 for a Mystery Chip, a Fan, and a "TBD" Spec Sheet:**
**$799 standalone** is **123× the single-unit price** (and **~175× the factory reel price**) of a flagship Sensirion SHT45-AD1F chip.
What does $800 buy you? An **undisclosed RH chip**, **zero published chemical endurance**, **no active thermal chemical purge**, **no cheap $15–$25 swappable RH tip**, and a spec sheet that literally had **"TBD" fields** left on it!
They strap an **aspiration fan** onto the box—meaning one unbagged ZeroTol fog or sulfur burn vacuums poison straight onto a non-serviceable sensor—and when your $800 box drifts off a cliff, GrowlinkOS hands you… **a software offset menu.** For the cost of **one** Growlink ESM-2, you could buy **60+ Adafruit SHT45 breakouts** and throw a fresh one in every room every quarter for a decade!
**AROYA Climate One & Climate Station (Quote-Only / ~$5,000 AROYA GO Bundles + Recurring SaaS Lock-In) — "National Weather Service" Hype, $9 Govee Accuracy, and a 7.1 CFM Spray Vacuum:**
Read AROYA's own `CLIMATE ONE` sales page and try not to laugh: they call it _"industrial-grade reliability, not fragile hobbyist tech"_, _"flawless moisture tracking"_, _"unquestionable, research-level durability"_, and _"pure, uninterrupted ground-truth data"_—and hide the price behind a **"Book a technical demo"** sales funnel (with entry AROYA GO starter kits running **~$5,000** plus ongoing platform fees).
**Now look at the actual specs printed on that same product:**
**±3% RH accuracy (and only rated 20–80% RH!)** — literally the **exact same ±3% RH tolerance as a $9 Govee puck**, and **3× sloppier than a $6.50 bare Sensirion SHT45 (±1.0% RH)**!
**±0.7 °C [±1.26 °F] temperature accuracy** — **7× worse than a $6.50 SHT45 (±0.1 °C)** and **over 2× worse than a $9 Govee (±0.3 °C)**!
**An active aspiration fan sucking 0.2 m³/min (~7.1 CFM) 24/7** — that's **288,000 liters of room air every single day** pulled straight over an **undisclosed RH chip** with **no disclosed inlet membrane, no published annual drift rate, no spray-cycle validation, and no thermal chemical purge!** Forget to cut PoE power and bag it before ZeroTol fogging, IPA wipe-downs, foliar oil sprays, or sulfur burns, and your "ground-truth" enterprise box turns into a **7.1 CFM chemical shop-vac** poisoning itself on your dime!
Even on AROYA's older **METER ATMOS 14** station (which at least earns credit for a porous PTFE screen, ±0.25%/yr clean-air drift disclosure, and an honest solvent-damage manual), **gas-phase IPA, H2O2, PAA, and terpenes walk straight through PTFE**—and when it drifts, you're paying **~$100–$120 just for a recalibration** or a proprietary Gen-2 board swap on top of enterprise pricing!
**The Brutal Comparison:** Real industrial instrument makers earn their price tags with physics: **Vaisala** gives you a 180 °C chemical purge and catalytic H2O2 destruction; **Priva** and **Hoogendoorn** give you polymer-free wet/dry bulb psychrometers or honest annual plug-in swaps; **Argus SEN-RHT** gives you field-replaceable NIST tips. **AROYA and Growlink charge you industrial money for consumer polymer physics, bolt a fan to it that accelerates chemical poisoning, and lock you into proprietary hardware.**


The Rest of the Hall of Outrage

**TrolMaster** sells the most popular commercial cannabis sensor in North America (MBS-TH) with a **±7% RH factory spec**—wide enough to drive a truck through _before it ever touches a spray_—and wraps a $4 chip inside a **$250–$350 MBS-PRO** with no swappable RH tip.
**Pulse Grow** can't even agree with itself: the **$499 Pulse Pro** claims **±1.5% RH** on the sales page and **±3% RH** on the tech spec page—and if your canopy sprays poison the hidden $4 chip inside, there is no replaceable tip.
**Grodan** sells a **$1,000–$1,450+** climate system with an unmarked chip rated **±4.5% to ±8% RH**.
**Agrowtek** puts a **6 CFM fan behind an open-cell foam dust filter**—turning the filter into a chemical sponge that breathes trapped IPM oils and ZeroTol straight over the chip for _days_—and rates it for **80% RH max continuous**.
**Vivosun** couldn't even proofread `%RH` (`"±0.6 %PH"`), and **Spider Farmer, Inkbird, and Govee** hand you a **±20% RH offset slider**—because they know their probes go sideways.

Meanwhile, look at the **big Dutch greenhouse veterans (Priva & Hoogendoorn)** and **industrial lab leaders (Vaisala, Rotronic, Argus)**: they don't pretend capacitive polymer chips last forever. They either **refuse to use polymers at all** (sticking to wet/dry bulb psychrometers), **bake chemicals out at 180 °C**, **install catalytic peroxide destroyers**, or **build annual plug-in element replacements right into the product.**
That is how an honest instrument is built. What most cannabis brands are selling you is a pretty dashboard glued to a disposable chip—at a 100× markup.

## The Brutal Math: How "Just 5 to 8% Drift" Wrecks Your Yield, Power Bill & Dry Room

Growers argue over `0.05 kPa` on VPD charts and pay six figures for HVACD—then hand the wheel to a probe that drifted 8% two harvests ago.

**The Golden Psychrometric Shortcut:** At 26.0 °C [78.8 °F], **every 1% RH of sensor error shifts VPD by ~0.034 kPa** _(exact: 0.0336 kPa, independent of leaf temp; FAO-56 Tetens and revised Buck equations agree to ~0.001 kPa)._

**Sanity Check on Leaf Temperature:** A **2.0 °C [3.6 °F]** error in your assumed leaf temperature moves Leaf VPD about as much as an **11% RH sensor error**. Fix your RH sensor first because it drifts silently—then verify canopy leaf temperature with an IR gun so you aren't chasing ghosts.

#### Scenario A: Flower Room — When a Wet-Drifting Sensor Starves Your Canopy

**Setup:** 26.0 °C [78.8 °F] air, **60.0% RH controller setpoint**, leaves at 24.5 °C [76.1 °F] (−1.5 °C differential; target Leaf VPD = **1.06 kPa**).

When your sensor drifts **wet (+)**, the controller sees fake humidity and hammers the dehumidifiers until the _drifted_ display hits 60%—pulling the real room drier by the exact sensor error:

Sensor Error (Displayed − True)
Displayed RH
**True Room RH**
**True Air VPD**
**True Leaf VPD** _(24.5 °C leaf)_
**LVPD Error %** _(and at −1 °C / −2 °C leaf)_
Real-World Damage

**0% RH (Honest)**60.0%**60.0%**1.34 kPa**1.06 kPa****0.0%**Dialed in
**+3% RH**60.0%**57.0%**1.45 kPa**1.16 kPa****+9.5%** _(+8.8% / +10.4%)_Extra dehu duty cycle; drifting out of sweet spot
**+5% RH**60.0%**55.0%**1.51 kPa**1.23 kPa****+15.9%** _(+14.6% / +17.4%)_Pushes a 1.0–1.2 kPa room out of band
**+8% RH**60.0%**52.0%**1.61 kPa**1.33 kPa****+25.4%** _(+23.4% / +27.8%)_Stomatal stress, rootzone EC spikes, **wasted kWh** (1.95 g/m³ excess water removal = hundreds/mo)
*_+10.6% RH _(Real NZ F2 case!)***60.0%**49.4%**1.70 kPa**1.41 kPa****+33.7%**Accidental crop-steering dry-back; growers chase fake irrigation/EC issues!

- **Running a VPD Controller Instead of RH?** Doesn't save you! Targeting **1.20 kPa Leaf VPD** at 26 °C with a +8% wet sensor drops true room RH to **50.5%** (at −1 °C leaf) or **45.1%** (at −2 °C leaf), slamming true Leaf VPD to **1.47 kPa**!
- **In Veg, the % Hit Is Even Bigger:** At 25 °C air / 24 °C leaf targeting 70% RH (0.77 kPa), just **+5% RH** spikes VPD to **0.93 kPa (+20%)** on tender young plants. At 26 °C / 24.5 °C targeting 65% RH (0.89 kPa), a **−10% dry drift** crashes LVPD to **0.55 kPa (−38%)**.
- **Flip the Sign in Flower (Oil/Terpene Dry Drift):** In a 25.0 °C [77.0 °F] mid-flower room targeting **55% RH** (1.24 kPa LVPD at 24 °C leaf):
- **−10% dry drift** → true room sits at **65% RH** (LVPD drops to **0.92 kPa**) → weak calcium transport, stretched/larfy buds, high pathogen pressure.
- **−15% dry drift** → true room sits at **70% RH** (LVPD collapses to **0.77 kPa**) → **Botrytis & powdery mildew inside dense colas**, dew-point condensation at lights-off!

#### Scenario B: The Dry & Cure Room — A Razor's Edge Where One Bad Sensor Kills an Entire Harvest

If a lying flower-room sensor quietly bleeds yield and electricity, **a lying dry-room sensor wipes out $20,000 to $250,000+ batches in a single week.**

At equilibrium, your flower's **water activity (aw)** matches the room's Equilibrium Relative Humidity (aw = ERH / 100).

- **ASTM D8196 / D8197-22** sets the commercial safe band for dried cannabis flower at **0.55 to 0.65 aw**.
- Below **0.55 aw**: trichomes turn brittle, curing biochemistry halts, volatile monoterpenes flash off, and you burn **2–5% of sellable harvest weight straight into thin air**.
- Above **0.65 aw**: _Aspergillus_, _Penicillium_, and _Botrytis_ explode—and state microbial compliance tests fail. _(Peer-reviewed warning: Segers et al. 2016 proved xerophilic **Aspergillus penicillioides** can germinate as low as **0.585 aw**! And Birenboim et al. 2024 notes optimal drying curves are cultivar-specific—not a blind "60/60" religion.)_

**Look how narrow that margin is:** Around a 60% RH setpoint, the _entire_ ASTM safe window is only **±5% RH wide**—the exact size of drift you can pick up from a single sanitizing week! _(And a 55% setpoint has ZERO downward margin.)_

Dry Room Setpoint
Sensor Drift
**True Room RH**
**Equilibrium aw**
**Air VPD** _(Drying Force vs. Target)_
Dew Point (°C [°F])
Harvest Outcome

**15.5 °C [59.9 °F], 60%****−15%** _(dry bias)_**75.0%****0.75**0.44 kPa _(×0.63)_11.1 [52.0]**Catastrophic Botrytis / mould wipeout**
**15.5 °C [59.9 °F], 60%****−8%** _(oil/crossover)_**68.0%****0.68**0.56 kPa _(×0.80)_9.6 [49.3]**Aspergillus / failed state microbial compliance**
**15.5 °C [59.9 °F], 60%****−5%****65.0%****0.65**0.62 kPa _(×0.88)_8.9 [48.1]**Standing directly on the mould cliff edge**
**15.5 °C [59.9 °F], 60%****0% (Honest)****60.0%****0.60****0.70 kPa** _(×1.00)_7.8 [46.0]**Ideal slow dry; dead-centre of ASTM D8197**
**15.5 °C [59.9 °F], 60%****+5%** _(wet bias)_**55.0%****0.55**0.79 kPa _(×1.13)_6.5 [43.7]Bottom edge of ASTM band; accelerated dry
**15.5 °C [59.9 °F], 60%****+8%****52.0%****0.52**0.85 kPa _(×1.20)_5.7 [42.3]**Over-dried:** terpene loss, brittle trichomes, **2–5% weight loss**
**15.5 °C [59.9 °F], 55%****+8%****47.0%****0.47**0.93 kPa _(×1.18)_4.2 [39.6]**Severe over-dry:** hay smell, shattered flower
**18.0 °C [64.4 °F], 60%****+5%****55.0%****0.55**0.93 kPa _(×1.13)_8.8 [47.9]High VPD; outer case-hardening while cores stay wet
**18.0 °C [64.4 °F], 55%****+8%****47.0%****0.47**1.09 kPa _(×1.18)_6.5 [43.8]**Severe over-dry**

**Dry-Room Reality Check:** Dry rooms sit right where Sensirion and TI place the contamination **crossover** (high RH + heavy terpenes + between-batch sanitizers), meaning a poisoned probe can lie in _either_ direction. **Never trust the wall screen alone for release:** always measure actual **aw directly on a representative flower sample** with a calibrated water-activity meter before jarring or packaging. Wall RH tells you where the flower is _heading_, not where it _is_.

## Stop Falling for Software Offsets and Toaster-Oven "Reconditioning"

When growers finally catch a drifted probe, they usually try one of two bad fixes:

#### Trap #1: Punching in a Software Offset (`−8%` or `+6%`)

Every consumer app begs you to type in a flat offset. **Don't fall for it.**

1. **Chemical drift is non-linear.** A sensor that reads `−7%` at 55% RH daytime might read `−2%` at 40% RH and `−13%` at 75% RH lights-off. Fixing one point breaks the rest of the curve.
2. **Offsets can't cure lag or blindness.** If oils choked the filter to a 30-minute response lag, offsetting the average still leaves your dehumidifiers swinging wildly.
3. **Poisoned polymers keep moving.** Today's `−7%` offset will be wrong again next week.

#### Trap #2: Baking Probes to "Recondition" Them

Chipmakers publish oven bake-and-rehydrate recipes for **bare silicon chips** suffering _mild, reversible_ creep or volatile solvent sorption:

Chipmaker
Bake Step (Bare Chip Only!)
Rehydration Step

**Sensirion SHTxx**100–105 °C [212–221 °F], 20–30 °C [68–86 °F], ~75% RH (NaCl), **12 h**
**Texas Instruments HDC302x**100 °C, 25 °C, 50% RH, **5 days**
**Bosch BME280**120 °C, 70 °C, 75% RH, **6 h** (+ 1 h rest)
**Renesas HS300x**100 °C, 20–30 °C, 75% RH, **12–14 h**
**Silicon Labs Si7021**125 °C, **≥12 h**30 °C, 75% RH, **≥10 h**
**Aosong DHT22 / DHT20**DHT22: 50–60 °C, 20–30 °C, >70–75% RH, **5–6 h** _(ignore AHT20 datasheet typo!)_
**Vaisala (Industrial Probes)**Up to **160 °C [320 °F] for 1 h** (compatible models only)Per service spec

**Why you should NEVER waste time baking grow probes:** Sensirion itself calls this a **"last resort" for bare chips only**. Stick an assembled plastic grow probe in a 105 °C oven and you will melt the housing, force the cable jacket and epoxy to outgas _even more_ VOCs onto the chip, bake neem oil and quats into a permanent glaze, and accomplish zero against peroxide oxidation or sulfur corrosion.

Do the math: **22+ hours of oven/chamber time + 1 to 2 hours of technician labour ($30–$120)** + a 2-point salt re-check—for an uncertain repair on a **$6 to $25 sensor head**. Only refurbish high-dollar industrial probes (Vaisala/Rotronic/ATMOS) under manufacturer service. For everything else: **scrap it and swap it.**

## Take Back Control: The Grower's Bulletproof Protocol

You cannot trust three room sensors to check each other—if all three sat through the same ZeroTol fog, **all three lie together.** The cure is boring, cheap, and takes 20 minutes per room.

#### Step 1: Lock Down Your "Golden Benchmark" (Your Source of Truth)

Keep **two dedicated reference sensors** (Primary + Vault Backup) that **NEVER live inside a grow room, dry room, trim room, or chemical/nutrient closet.**

- **GMP / Commercial Facilities:** ISO 17025 / NIST-traceable handheld—**Vaisala HM40/HM45** (±1.1% RH, ~$1,000–$2,600) or **Rotronic HP32 + HC2A-S** (±0.8% RH, ~$1,100–$1,900), calibrated annually. Target expanded uncertainty ≤1% RH.
- **Craft / Budget Facilities:** Two clean, dedicated **Sensirion SHT45-AD1F** loggers (verify Reel ID, low-self-heating board) or **SensorPush HTP.xw** (±1.5% RH, ePTFE). If your two references ever disagree by **>1.5% RH**, salt-check both before trusting either.
- **Non-Negotiable Storage Rules:**
- Store in an **airtight borosilicate glass jar with a metal lid** (or sealed stainless box) with isolated, buffered indicating silica gel desiccant in a clean office (20–25 °C [68–77 °F]). _(Avoid ultra-dry storage beyond maker limits; let settle 30 min in room air after desiccant storage before reading.)_
- **NEVER** store in PE antistatic bags, pink foam, soft PVC cases, silicone-gasket plastic tubs, or taped boxes—container off-gassing alone will poison a reference!
- **NEVER** wipe the reference with IPA, ethanol, or disinfectant wipes. Never take it into a room during or immediately after spraying.

#### Step 2: Verify Your Benchmark Quarterly (Two-Point Saturated Salt Check — ASTM E104 / Greenspan 1977)

**Why Boveda calibration kits aren't enough:** Boveda rates its packs at **±2% RH** at a single point. That catches a sensor that's 10 points broken, _not_ a 2.5% drift or a bent slope/gain error. Reagent-grade salt slurries are **~20× tighter** and cost a few dollars.

Make two separate slurries in **small airtight glass or stainless jars** (never plastic—plastics absorb moisture and ruin equilibration) using reagent-grade salt + distilled/DI water (~1 cm wet slush with **visible excess undissolved crystals**). Suspend the sensor clean above the salt—never let it touch liquid.

Jar Temperature
**MgCl2 Target (%RH)**
**NaCl Target (%RH)**

**15 °C [59.0 °F]****33.30 ± 0.21%****75.61 ± 0.18%**
**20 °C [68.0 °F]****33.07 ± 0.18%****75.47 ± 0.14%**
**25 °C [77.0 °F]****32.78 ± 0.16%****75.29 ± 0.12%**
**30 °C [86.0 °F]****32.44 ± 0.14%****75.09 ± 0.11%**

_(Additional 25 °C Greenspan fixed points if needed: LiCl 11.30%, K2CO3 43.16%, Mg(NO3)2 52.89%.)_

- **The #1 Salt-Check Killer — Temperature Mismatch:** Keep jars isothermal (±0.2 °C [±0.36 °F]), out of sunlight, vents, and hands. At 25 °C, a sensor just **0.5 °C warmer** than the NaCl slurry reads **73.08% instead of 75.29%**; **1.0 °C warmer** reads **70.95%**—a massive fake error!
- **Wait Long Enough:** Minimum **12–24 hours** per point _(SensorPush recommends 48–72 hours for sealed pucks)_ until the last 1–2 hours stay flat within **±0.2% RH**.
- **The Two-Point Gain Check:** Run **both** salts. If the error at 33% and the error at 75% differ by **>2.0% RH**, the polymer has **lost gain/bent slope**—trash it!

#### Step 3: Run the 20-Minute In-Room Side-by-Side Check

1. **Wait for Clean Air:** Never bring your Golden Benchmark into a room until full re-entry interval (REI), HVAC ventilation purge, and drying are complete.
2. **Inspect the Room Probe:** Check cap/filter/foam for oil film, salt crust, dust, or moisture droplets.
3. **Co-Locate Properly:** Mount the Golden Benchmark **5–10 cm (2–4 in)** from the working sensor's inlet—exact same height, airflow stream, and light shading (keep out of direct LED/HPS radiation and fan jets). Stand 2–3 ft back—don't breathe on it!
4. **Equilibrate (20–30 Min):** Never wave a meter for 60 seconds. A 1.0 °C temperature lag creates a 3–4% RH fake error. Wait until **ΔT ≤ 0.2–0.5 °C** and RH moves <0.2% over 3 minutes.
5. **Log 5–10 Paired Readings (1 min apart)** and compute mean ΔRH = mean RHroom − mean RHref _(positive = room probe reads wet)_.
6. **Run the Dew-Point Diagnostic Trick:** Compute dew point (Td) for both probes. **If dew points match but RH disagrees, the problem is a temperature error or housing self-heating—NOT a poisoned RH element!**
7. **Check Both Ends of the Day & Lag:** Quarterly, compare at both **lights-on and lights-off** (catches crossover/slope errors). If a graph looks suspiciously flat, test step response—a steady-state check won't catch a blind or sluggish probe.
8. **Dry & Cure Rooms:** **Weekly** + **24 h before every harvest load** + mid-dry + after between-batch cleaning.
9. **Flower / Veg / Mother Rooms:** **Every 1–2 weeks** (monthly absolute minimum) + at room turnover.
10. **Mandatory Event Trigger:** **24 hours after** every foliar spray, H2O2/PAA/HOCl fog, sulfur burn, or deep clean (post-REI/ventilation) — **AND re-check 7 days later** to catch slow-diffuser delayed drift!
11. **Before Every Spray, Fog, Sulfur Burn, or Deep Clean:**
12. Switch control loops to a verified backup/temporary mode and log alarms.
13. **Unplug and remove modular probes** into a clean sealed glass jar.
14. For hardwired stations: **TURN OFF ASPIRATION FANS**, slip an **aluminium foil cap** or clean sealed barrier over the head, and clip a bright red **"REMOVE AFTER REI"** tag on it. _(Avoid cheap outgassing plastic bags for long stretches.)_
15. Keep probes covered/out until **full REI + at least 1 hour of active ventilation purge** completes.
16. **Zero-Solvent Rule:** **NEVER** spray or wipe any sensor housing, radiation shield, or adjacent control panel with IPA or ethanol. Any probe directly wetted by spray or solvent goes straight in the bin.
17. **Smart Mounting:** Mount above/beside the canopy in a shaded, ventilated spot—never buried inside wet colas or directly downstream of fogger/humidifier jets.
18. **Stock Sealed Spares:** Keep **20–25% spare probes** (1 per 4 installed) sealed like your benchmark, pre-qualified in the exact housing you run. Tag every active probe with **Sensor ID, Install Date, and Retirement Date**.
19. **Hard Calendar Retirement (Even If Passing!):** Replace exposed room probes every **6 months (or 3 cycles)** in heavy-IPM veg/mother rooms and every **12 months** in flower and dry rooms—matching what Priva and Hoogendoorn build into industrial greenhouse systems.
20. **Buy Smarter Next Time:** Stop buying $500 sealed boxes with glued-in $4 chips. Standardize on **modular, quick-swap SHT45-AD1F probes** (with verified membrane lot and firmware heater cycles if possible), **swappable-tip industrial probes (Argus SEN-RHT / Vaisala / Rotronic)**, or **polymer-free wet/dry-bulb psychrometers** for harsh rooms.
21. **What exact RH chip part number and revision is inside your probe?** _(If SHT45-AD1F, is it pre-2026 PTFE or post-2026 polyimide under PCN254901?)_
22. **What is the published annual drift rate, and what pre/post accuracy and step-response test data do you have after exposure to IPA, H2O2/PAA, quats, sulfur, and foliar oils?**
23. **Does your firmware actually run the chip's on-board thermal decontamination and anti-creep heater cycles—and how do you keep it from firing in contaminated air?**
24. **Can I swap just the $15–$25 sensing tip when it drifts, or do you expect me to buy a whole new $300–$800 unit every year?**
25. **Why does your app offer a ±10% to ±20% software calibration offset instead of a documented replacement schedule?**

## References

#### Chipmakers & Chemical Contamination Studies

1. **Sensirion AG.** _SHT4x Datasheet V7.3_ (June 2026) & _V6.4_ (Nov 2023); _SHT3x-DIS Datasheet V7_ (2022) & _SHT3x Membrane Datasheet V6_ (July 2026); _PCN254901: Change of Filter Membrane Material PTFE to Polyimide_ (Dec 2025).
2. **Sensirion AG.** _Handling Instructions for SHTxx Humidity Sensors_ V9 (June 2025); _Contamination Guide_ V1.1 (Sept 2024); _Using the Integrated Heater of SHT4x for Heat-Assisted Polymer Decontamination_ (2022/2024); _Creep Mitigation App Note_ (Apr 2022); _Support FAQ_.
3. **Texas Instruments.** _SDAA445A: How Chemical Contamination Impacts Humidity Sensors_ (Aug 2026); _SNAA353A: Accuracy Shift & Drift_ (2021); _SNIA025: Storage & Handling Guidelines_ (2017); _SNAU265D: HDC3x Silicon User's Guide_ (Figs. 2-1 to 2-5); _HDC1080 / HDC2080 / HDC302x Datasheets_.
4. **Honeywell Sensing & Control.** _Humidity Sensors: Chemical Resistivity_, Application Sheet `009068-1-EN` (June 2011, HIH-3602 liquid & vapour tests); _HIH6130/6131 & HIH-4000 Guides_.
5. **Vaisala Oyj.** Ikonen, Stormbom & Ranta-aho, _Chemical Interference Test Results of a Novel Humidity Sensor (HUMICAP 180R)_, ISHM 2006; Ikonen, _Humidity Sensor Chemical Tolerance_, WMO TECO-2008; _Humidity Measurements in Vaporized H2O2 Bio-Decontamination Applications_ (PEROXCAP); _Common Pitfalls in Industrial Humidity Measurements_ (50,000 ppm IPA test); _HM40 User Guide_.
6. **Rotronic AG.** _Contamination & Pollutants Permissible Concentrations_ (IN-1 / HH-1 / HT-1); _Hygromer HH1-SK Manual_; _HP32 / HC2A-S Specs_.
7. **Bosch Sensortec.** _BST-BME280-HS006 Handling, Soldering & Mounting Instructions_ (2018); _BME680 / BME688 Docs_.
8. **TE Connectivity / MEAS** (_HTU21D / HTU31_); **Renesas** (_HS300x Datasheet_); **Silicon Labs** (_Si7021-A20 Datasheet_); **Aosong / ASAIR** (_DHT22/AM2302, DHT20, AHT10/20/21 Datasheets_).

#### Peer-Reviewed Science, Standards & Independent Testing

1. **ASTM International.** _ASTM D8197-22_ (Acceptable Water Activity Range 0.55–0.65 aw for Dry Cannabis Flower); _ASTM D8196-20/22_ (Determination of Water Activity); _ASTM E104_ (Constant RH via Aqueous Salt Solutions).
2. **Greenspan, L. (1977).** _Humidity Fixed Points of Binary Saturated Aqueous Solutions_, J. Res. NBS 81A(1):89–96.
3. **Allen et al. (1998)** _FAO-56 Tetens Saturation Vapour Pressure (Ch. 3, Eq. 11)_ & **Buck Research Instruments** _Revised Buck Saturation Pressure Coefficients_.
4. **Segers, F.J.J. et al. (2016).** _Xerophilic fungus Aspergillus penicillioides germination at low water activity (0.585 aw)_, PubMed `27871132`.
5. **Birenboim et al. (2024).** _In Pursuit of Optimal Quality: Cultivar-Specific Drying Approaches for Medicinal Cannabis_, _Plants_ (2024).
6. **Colorado Cannabis Emissions Study (2023).** _Indoor Monoterpene Emission Rates from Commercial Cannabis Cultivation Facilities in Colorado_, J. Air Waste Manage. Assoc.
7. **Matsuguchi et al. (1998).** _Stability and Reliability of Capacitive-Type RH Sensors Using Crosslinked Polyimide Films_, Sensors and Actuators B; **Farahani et al. (2014)** _Sensors_ 14:7881–7939; *_MDPI _Sensors_ (2019)** 19(3):659; **Ingleby et al. (2013)__ Met Office _Surface Humidity Reports*.
8. **Smith, R.J. / Page & Page.** _Hygrometer Comparison & Calibration Study_ (`kandrsmith.org`).
9. **EPA Labels & Product SDS:** Green Cleaner, ZeroTol 2.0, Physan 20, Virkon S, SNS-209, Athena IPM, Regalia, Venerate XC.
10. **Live Facility Telemetry:** Licensed commercial flower room sensor swap record (New Zealand, Room F2, SHT30 → SHT45, Sept 24, 2026).

#### Brand Datasheets, Manuals & FCC Exhibits

1. TrolMaster (`MBS-TH` / `MBS-PRO` cut sheets & KB); Pulse Grow (One / Pro / `THV-1` manuals & specs); METER Group / AROYA (`ATMOS 14` Gen 2 & Climate One); Growlink (`ClimaLINK` / `ESM-2`); Agrowtek (`SXC` / `SXC+`); AC Infinity (Controller 69 / AI+ manuals & **FCC `2AXMF-CTR69A`**); Spider Farmer (`GGS` manual); Vivosun (`GrowHub` / probe specs); Govee (Sensirion PR & **FCC `2AQA6-H5075`**); SensorPush (`HT1` / `HT.w` / `HTP.xw` & **FCC `2AL9X-HT1`**); Inkbird (`IBS-TH2` / `IHC-200` manuals & **FCC `2AYZD-IBSTH2` / `2AYZD-200WIFI`**); Ecowitt (`WN31` / `WN31EP` manual); Grodan (`GroSens` Climate & **FCC `2AUKP-CL002`**); Link4 (`iPonic 624` / `DISM` / `I2C DTH`); Autogrow / Bluelab (`IntelliClimate`); Argus Controls (`SEN-RHT` / `SEN-OSM`); Priva (Classic & `E-Measuring Box SPE`); Hoogendoorn (`iSii` / `IIVO`); Aranet (`TDSPT802` / `TDSPT409`); Grow Sensor PRO; Onset (`HOBO MX2301A`); Davis Instruments (`Vantage Pro2` KB); DigiKey / Mouser / Adafruit (`SHT45-AD1F-R2` & `#5665`).


