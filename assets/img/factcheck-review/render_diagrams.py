# -*- coding: utf-8 -*-
"""Exact-label educational diagrams for fact-check review pack (SVG)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent


def write(name: str, svg: str) -> None:
    p = OUT / name
    p.write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", p.name, p.stat().st_size)


# ---------------------------------------------------------------------------
# 01 Dryback points vs percent
# ---------------------------------------------------------------------------
write("01-dryback-points-vs-percent.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="52" fill="#e7ecf3" font-size="26" font-weight="700">Dryback = percentage POINTS, not “% of peak”</text>
  <text x="48" y="82" fill="#9aabbc" font-size="15">Crop-steering sensors report how-full % (VWC). The drink-down is high minus low.</text>

  <!-- tank -->
  <rect x="80" y="120" width="160" height="340" rx="12" fill="#1a2332" stroke="#2d3a4d" stroke-width="2"/>
  <rect x="88" y="148" width="144" height="248" fill="#1e3a4a"/>
  <!-- water 58-78 -->
  <rect x="88" y="148" width="144" height="62" fill="#1a2332"/>
  <rect x="88" y="210" width="144" height="186" fill="#2a9d8f"/>
  <line x1="70" y1="210" x2="260" y2="210" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 3"/>
  <line x1="70" y1="396" x2="260" y2="396" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="268" y="216" fill="#38bdf8" font-size="16" font-weight="600">Peak 78%</text>
  <text x="268" y="402" fill="#fbbf24" font-size="16" font-weight="600">Trough 58%</text>
  <text x="120" y="320" fill="#0f1419" font-size="18" font-weight="700">20 pts</text>
  <text x="100" y="490" fill="#9aabbc" font-size="13">Substrate “fullness” gauge</text>

  <!-- callouts -->
  <rect x="420" y="140" width="480" height="120" rx="12" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="440" y="175" fill="#34d399" font-size="18" font-weight="700">Correct: 20 percentage POINTS</text>
  <text x="440" y="205" fill="#e7ecf3" font-size="16">Dryback = 78 − 58 = 20 points</text>
  <text x="440" y="235" fill="#9aabbc" font-size="14">This is what “20-point dryback” means in steering SOPs.</text>

  <rect x="420" y="290" width="480" height="140" rx="12" fill="#1a2332" stroke="#ff8a4c" stroke-width="2"/>
  <text x="440" y="325" fill="#ff8a4c" font-size="18" font-weight="700">Not the same: “20% of peak”</text>
  <text x="440" y="355" fill="#e7ecf3" font-size="16">20% of 78 ≈ 15.6 points (would land near 62%)</text>
  <text x="440" y="385" fill="#9aabbc" font-size="14">Only say “percent of peak” if you mean fractions of the peak reading.</text>
  <text x="440" y="410" fill="#9aabbc" font-size="13">If unclear, always mean points: peak − trough.</text>

  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · educational diagram · Cannabis White Papers</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 02 Moisture % vs water activity
# ---------------------------------------------------------------------------
write("02-moisture-vs-water-activity.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="26" font-weight="700">Moisture content ≠ water activity</text>
  <text x="48" y="78" fill="#9aabbc" font-size="15">Same “11% moisture” can sit anywhere from ruined-too-dry to mould-risk. Steer by aw.</text>

  <!-- left gauge moisture -->
  <rect x="60" y="120" width="380" height="340" rx="14" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="250" y="155" text-anchor="middle" fill="#9aabbc" font-size="14" font-weight="600">MOISTURE CONTENT (%)</text>
  <text x="250" y="210" text-anchor="middle" fill="#e7ecf3" font-size="48" font-weight="700">11%</text>
  <text x="250" y="245" text-anchor="middle" fill="#ff8a4c" font-size="15">cheap meter ±1% error band</text>
  <rect x="100" y="280" width="280" height="28" rx="6" fill="#2d3a4d"/>
  <rect x="100" y="280" width="280" height="28" rx="6" fill="url(#warnGrad)"/>
  <text x="110" y="340" fill="#9aabbc" font-size="13">Same reading can mean:</text>
  <text x="110" y="370" fill="#ff5c5c" font-size="15">aw ~0.53  → too dry, terpenes gone</text>
  <text x="110" y="400" fill="#fbbf24" font-size="15">aw ~0.60  → in the safe band</text>
  <text x="110" y="430" fill="#ff8a4c" font-size="15">aw ~0.66  → mould risk rising</text>

  <!-- right gauge aw -->
  <rect x="500" y="120" width="400" height="340" rx="14" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="700" y="155" text-anchor="middle" fill="#9aabbc" font-size="14" font-weight="600">WATER ACTIVITY (aw)</text>
  <!-- scale bar -->
  <rect x="540" y="200" width="320" height="36" rx="8" fill="#2d3a4d"/>
  <rect x="540" y="200" width="96" height="36" rx="8" fill="#7f1d1d"/>
  <rect x="636" y="200" width="128" height="36" fill="#166534"/>
  <rect x="764" y="200" width="96" height="36" rx="0 8 8 0" fill="#9a3412"/>
  <text x="580" y="255" fill="#ff5c5c" font-size="12">&lt;0.55 dry</text>
  <text x="680" y="255" fill="#34d399" font-size="12">0.55–0.65 ASTM</text>
  <text x="790" y="255" fill="#ff8a4c" font-size="12">&gt;0.65 risk</text>
  <text x="700" y="300" text-anchor="middle" fill="#e7ecf3" font-size="22" font-weight="700">Take-down ~0.60–0.62</text>
  <text x="700" y="335" text-anchor="middle" fill="#9aabbc" font-size="14">Finish cure ~0.58–0.60</text>
  <text x="700" y="380" text-anchor="middle" fill="#9aabbc" font-size="14">Mould risk climbs hard near ~0.70+</text>
  <text x="700" y="420" text-anchor="middle" fill="#34d399" font-size="15" font-weight="600">Use aw for safety + quality</text>

  <defs>
    <linearGradient id="warnGrad" x1="0" x2="1">
      <stop offset="0%" stop-color="#7f1d1d"/>
      <stop offset="50%" stop-color="#ca8a04"/>
      <stop offset="100%" stop-color="#9a3412"/>
    </linearGradient>
  </defs>
  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · ASTM D8197-aligned educational diagram</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 03 Leaf vs canopy light curves
# ---------------------------------------------------------------------------
write("03-leaf-vs-canopy-light.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">Leaf saturation ≠ canopy yield ceiling</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">A single leaf gas-exchange curve can flatten early. Whole-plant flower yield can still rise with more light (e.g. RM2021).</text>

  <!-- panel left -->
  <rect x="48" y="110" width="420" height="360" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="68" y="145" fill="#38bdf8" font-size="16" font-weight="700">Single-leaf photosynthesis</text>
  <!-- axes -->
  <line x1="100" y1="400" x2="420" y2="400" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="100" y1="400" x2="100" y2="180" stroke="#5a6a7a" stroke-width="2"/>
  <text x="250" y="430" fill="#9aabbc" font-size="12">PPFD (µmol m⁻² s⁻¹)</text>
  <text x="70" y="300" fill="#9aabbc" font-size="11" transform="rotate(-90 70 300)">Anet</text>
  <!-- saturating curve path -->
  <path d="M100 390 C160 380, 200 280, 260 230 C300 200, 340 190, 420 185" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="280" cy="215" r="5" fill="#fbbf24"/>
  <text x="290" y="210" fill="#fbbf24" font-size="12">leaf saturates earlier</text>
  <text x="120" y="460" fill="#9aabbc" font-size="12">Ambient CO₂ lowers efficiency of high PPFD at the leaf.</text>

  <!-- panel right -->
  <rect x="500" y="110" width="420" height="360" rx="12" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="520" y="145" fill="#34d399" font-size="16" font-weight="700">Whole-canopy flower yield</text>
  <line x1="552" y1="400" x2="872" y2="400" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="552" y1="400" x2="552" y2="180" stroke="#5a6a7a" stroke-width="2"/>
  <text x="700" y="430" fill="#9aabbc" font-size="12">PPFD (µmol m⁻² s⁻¹)</text>
  <text x="520" y="300" fill="#9aabbc" font-size="11" transform="rotate(-90 520 300)">Yield</text>
  <!-- rising line -->
  <path d="M552 380 L620 340 L690 290 L760 240 L840 195" fill="none" stroke="#34d399" stroke-width="3"/>
  <text x="700" y="200" fill="#34d399" font-size="12">can keep rising ~1500–1800</text>
  <text x="570" y="460" fill="#9aabbc" font-size="12">Not a hard “800 µmol wall” under ambient CO₂ — diminishing returns, not a cliff.</text>

  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · schematic (not raw data plot) · RM2021 vs leaf gas-exchange framing</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 04 Caplan one drought vs daily dryback
# ---------------------------------------------------------------------------
write("04-caplan-vs-daily-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">One late drought study ≠ daily crop-steering drybacks</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">Caplan-style evidence supports carefully timed water deficit — not a copy-paste of multi-week P0–P3 recipes.</text>

  <!-- left -->
  <rect x="48" y="110" width="400" height="340" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="68" y="150" fill="#fbbf24" font-size="17" font-weight="700">A · Single late drought (study style)</text>
  <line x1="90" y1="360" x2="400" y2="360" stroke="#5a6a7a"/>
  <line x1="90" y1="360" x2="90" y2="190" stroke="#5a6a7a"/>
  <path d="M90 220 L180 220 L200 320 L280 320 L300 220 L400 220" fill="none" stroke="#fbbf24" stroke-width="3"/>
  <text x="200" y="300" fill="#ff8a4c" font-size="13">one long dry event</text>
  <text x="68" y="400" fill="#9aabbc" font-size="13">Late flower · carefully timed · measured</text>
  <text x="68" y="425" fill="#9aabbc" font-size="13">May raise cannabinoid concentrations</text>

  <!-- X -->
  <text x="470" y="280" fill="#ff5c5c" font-size="42" font-weight="700" text-anchor="middle">≠</text>
  <text x="470" y="310" fill="#ff5c5c" font-size="14" text-anchor="middle">not the same</text>

  <!-- right -->
  <rect x="520" y="110" width="400" height="340" rx="12" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="540" y="150" fill="#34d399" font-size="17" font-weight="700">B · Daily dryback sawtooth (steering)</text>
  <line x1="560" y1="360" x2="880" y2="360" stroke="#5a6a7a"/>
  <line x1="560" y1="360" x2="560" y2="190" stroke="#5a6a7a"/>
  <path d="M560 240 L590 220 L610 300 L640 220 L660 300 L690 220 L710 300 L740 220 L760 300 L790 220 L810 300 L840 220 L860 300 L880 240"
        fill="none" stroke="#34d399" stroke-width="2.5"/>
  <text x="640" y="330" fill="#9aabbc" font-size="13">many small wet–dry cycles</text>
  <text x="540" y="400" fill="#9aabbc" font-size="13">Facility-specific setpoints · sensor-native %</text>
  <text x="540" y="425" fill="#9aabbc" font-size="13">Related idea, different experiment</text>

  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · educational comparison</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 05 DO saturation curve
# ---------------------------------------------------------------------------
write("05-do-saturation-curve.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">Dissolved oxygen saturation vs temperature</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">Clean freshwater at 1 atm. Warm water still raises pathogen risk even when saturation only falls gently.</text>

  <rect x="80" y="110" width="800" height="360" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <!-- axes -->
  <line x1="140" y1="400" x2="820" y2="400" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="140" y1="400" x2="140" y2="160" stroke="#5a6a7a" stroke-width="2"/>
  <text x="460" y="440" fill="#9aabbc" font-size="14">Water temperature (°C)</text>
  <text x="100" y="290" fill="#9aabbc" font-size="13" transform="rotate(-90 100 290)">DO (mg/L)</text>

  <!-- y ticks -->
  <text x="125" y="405" text-anchor="end" fill="#5a6a7a" font-size="12">0</text>
  <text x="125" y="340" text-anchor="end" fill="#5a6a7a" font-size="12">6</text>
  <text x="125" y="280" text-anchor="end" fill="#5a6a7a" font-size="12">8</text>
  <text x="125" y="220" text-anchor="end" fill="#5a6a7a" font-size="12">9</text>
  <text x="125" y="175" text-anchor="end" fill="#5a6a7a" font-size="12">10</text>
  <!-- x ticks -->
  <text x="200" y="420" text-anchor="middle" fill="#5a6a7a" font-size="12">10</text>
  <text x="380" y="420" text-anchor="middle" fill="#5a6a7a" font-size="12">20</text>
  <text x="560" y="420" text-anchor="middle" fill="#5a6a7a" font-size="12">26</text>
  <text x="740" y="420" text-anchor="middle" fill="#5a6a7a" font-size="12">30</text>

  <!-- correct curve approx: 10C~11.3, 20~9.1, 26~8.1, 30~7.6 mapped to chart -->
  <!-- y: 400 = 0, 160 = 10  => y = 400 - do*24 -->
  <path d="M200 129 L380 182 L560 206 L740 218" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <circle cx="380" cy="182" r="6" fill="#34d399"/>
  <text x="390" y="175" fill="#34d399" font-size="14" font-weight="600">20°C ≈ 9.1 mg/L</text>
  <circle cx="560" cy="206" r="6" fill="#34d399"/>
  <text x="570" y="200" fill="#34d399" font-size="14" font-weight="600">26°C ≈ 8.1 mg/L</text>

  <!-- wrong points crossed out -->
  <circle cx="380" cy="280" r="7" fill="none" stroke="#ff5c5c" stroke-width="2"/>
  <line x1="370" y1="270" x2="390" y2="290" stroke="#ff5c5c" stroke-width="2"/>
  <line x1="390" y1="270" x2="370" y2="290" stroke="#ff5c5c" stroke-width="2"/>
  <text x="250" y="275" fill="#ff5c5c" font-size="13">wrong old claim ~5–6</text>
  <circle cx="560" cy="330" r="7" fill="none" stroke="#ff5c5c" stroke-width="2"/>
  <line x1="550" y1="320" x2="570" y2="340" stroke="#ff5c5c" stroke-width="2"/>
  <line x1="570" y1="320" x2="550" y2="340" stroke="#ff5c5c" stroke-width="2"/>
  <text x="580" y="335" fill="#ff5c5c" font-size="13">wrong ~3–4</text>

  <text x="160" y="455" fill="#9aabbc" font-size="13">Target reservoir ~18–22°C + strong aeration. Risk rises with heat + low DO under root demand.</text>
  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · approximate saturation values for education</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 06 Clean to dirty flow
# ---------------------------------------------------------------------------
write("06-clean-to-dirty-flow.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">Facility flow: people &amp; clean materials go clean → dirty</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">Waste and used PPE only exit dirty → out. Never reverse without re-gowning.</text>

  <!-- rooms -->
  <g font-size="14" font-weight="600">
    <rect x="40" y="160" width="140" height="80" rx="10" fill="#166534" stroke="#34d399"/>
    <text x="110" y="195" text-anchor="middle" fill="#e7ecf3">Gowning</text>
    <text x="110" y="215" text-anchor="middle" fill="#bbf7d0" font-size="12">CLEAN</text>

    <rect x="220" y="160" width="140" height="80" rx="10" fill="#14532d" stroke="#34d399"/>
    <text x="290" y="195" text-anchor="middle" fill="#e7ecf3">Mothers / Prop</text>
    <text x="290" y="215" text-anchor="middle" fill="#bbf7d0" font-size="12">cleaner</text>

    <rect x="400" y="160" width="140" height="80" rx="10" fill="#1e3a5f" stroke="#38bdf8"/>
    <text x="470" y="205" text-anchor="middle" fill="#e7ecf3">Veg</text>

    <rect x="580" y="160" width="140" height="80" rx="10" fill="#713f12" stroke="#fbbf24"/>
    <text x="650" y="205" text-anchor="middle" fill="#e7ecf3">Flower</text>

    <rect x="760" y="160" width="150" height="80" rx="10" fill="#7f1d1d" stroke="#ff5c5c"/>
    <text x="835" y="195" text-anchor="middle" fill="#e7ecf3">Post-harvest</text>
    <text x="835" y="215" text-anchor="middle" fill="#fecaca" font-size="12">DIRTIER</text>
  </g>

  <!-- arrows forward -->
  <defs>
    <marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#34d399"/>
    </marker>
    <marker id="arrR" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#ff5c5c"/>
    </marker>
  </defs>
  <line x1="180" y1="200" x2="215" y2="200" stroke="#34d399" stroke-width="3" marker-end="url(#arr)"/>
  <line x1="360" y1="200" x2="395" y2="200" stroke="#34d399" stroke-width="3" marker-end="url(#arr)"/>
  <line x1="540" y1="200" x2="575" y2="200" stroke="#34d399" stroke-width="3" marker-end="url(#arr)"/>
  <line x1="720" y1="200" x2="755" y2="200" stroke="#34d399" stroke-width="3" marker-end="url(#arr)"/>

  <!-- waste path -->
  <rect x="760" y="320" width="150" height="70" rx="10" fill="#3f1d1d" stroke="#ff5c5c"/>
  <text x="835" y="350" text-anchor="middle" fill="#e7ecf3" font-size="14" font-weight="600">Waste exit</text>
  <text x="835" y="370" text-anchor="middle" fill="#fecaca" font-size="12">used PPE out</text>
  <path d="M835 240 V315" stroke="#ff5c5c" stroke-width="3" marker-end="url(#arrR)"/>

  <!-- ban reverse -->
  <rect x="80" y="320" width="520" height="100" rx="12" fill="#1a2332" stroke="#ff5c5c" stroke-width="2"/>
  <text x="100" y="360" fill="#ff5c5c" font-size="18" font-weight="700">✕ No reverse without re-gowning</text>
  <text x="100" y="390" fill="#9aabbc" font-size="14">Flower → mothers is a contamination path. Cross back only after full de-gown / re-gown.</text>

  <text x="48" y="500" fill="#5a6a7a" font-size="12">Fact-check pack · biosecurity polarity (people/materials vs waste)</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 07 Log reduction table
# ---------------------------------------------------------------------------
write("07-log-reduction-table.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">Log reduction ≠ those old “83% / 58%” mappings</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">Under standard test conditions: 1 log ≈ 90% removed, 2 log ≈ 99%, 3 log ≈ 99.9%.</text>

  <rect x="80" y="120" width="800" height="300" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <!-- header -->
  <rect x="80" y="120" width="800" height="50" rx="12" fill="#121a26"/>
  <text x="140" y="152" fill="#9aabbc" font-size="15" font-weight="600">Log₁₀ reduction</text>
  <text x="400" y="152" fill="#9aabbc" font-size="15" font-weight="600">Approx. removed</text>
  <text x="680" y="152" fill="#9aabbc" font-size="15" font-weight="600">Still remaining</text>

  <!-- rows -->
  <text x="180" y="210" text-anchor="middle" fill="#e7ecf3" font-size="22" font-weight="700">1 log</text>
  <text x="450" y="210" text-anchor="middle" fill="#34d399" font-size="22" font-weight="700">~90%</text>
  <text x="730" y="210" text-anchor="middle" fill="#9aabbc" font-size="22">~10%</text>
  <line x1="100" y1="235" x2="860" y2="235" stroke="#2d3a4d"/>

  <text x="180" y="285" text-anchor="middle" fill="#e7ecf3" font-size="22" font-weight="700">2 log</text>
  <text x="450" y="285" text-anchor="middle" fill="#34d399" font-size="22" font-weight="700">~99%</text>
  <text x="730" y="285" text-anchor="middle" fill="#9aabbc" font-size="22">~1%</text>
  <line x1="100" y1="310" x2="860" y2="310" stroke="#2d3a4d"/>

  <text x="180" y="360" text-anchor="middle" fill="#e7ecf3" font-size="22" font-weight="700">3 log</text>
  <text x="450" y="360" text-anchor="middle" fill="#34d399" font-size="22" font-weight="700">~99.9%</text>
  <text x="730" y="360" text-anchor="middle" fill="#9aabbc" font-size="22">~0.1%</text>

  <rect x="80" y="440" width="800" height="50" rx="10" fill="#3f1d1d" stroke="#ff5c5c"/>
  <text x="480" y="472" text-anchor="middle" fill="#fecaca" font-size="16">✕ Mapping 3 log → 83% or 2 log → 58% is arithmetic error — do not use.</text>

  <text x="48" y="525" fill="#5a6a7a" font-size="12">Fact-check pack · hand hygiene education (neither sterilises hands)</text>
</svg>
''')

# ---------------------------------------------------------------------------
# 08 Veg vs gen dryback polarity
# ---------------------------------------------------------------------------
write("08-veg-vs-gen-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="960" height="540" fill="#0f1419"/>
  <text x="48" y="48" fill="#e7ecf3" font-size="24" font-weight="700">Steering polarity: veg stays wetter; gen drybacks are larger</text>
  <text x="48" y="76" fill="#9aabbc" font-size="14">Matches mainstream crop steering + Caplan-style deficit for generative behaviour — not the inverted “long drybacks in veg” claim.</text>

  <rect x="48" y="120" width="400" height="320" rx="12" fill="#1a2332" stroke="#38bdf8"/>
  <text x="68" y="160" fill="#38bdf8" font-size="18" font-weight="700">Vegetative</text>
  <text x="68" y="188" fill="#9aabbc" font-size="13">Smaller drybacks · higher VWC · moderate EC</text>
  <line x1="90" y1="380" x2="400" y2="380" stroke="#5a6a7a"/>
  <path d="M90 250 L130 240 L150 280 L190 240 L210 280 L250 240 L270 280 L310 240 L330 280 L370 245 L400 250"
        fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="68" y="410" fill="#9aabbc" font-size="13">Encourage roots + leaf area</text>

  <rect x="500" y="120" width="420" height="320" rx="12" fill="#1a2332" stroke="#fbbf24"/>
  <text x="520" y="160" fill="#fbbf24" font-size="18" font-weight="700">Generative</text>
  <text x="520" y="188" fill="#9aabbc" font-size="13">Larger controlled drybacks and/or higher root-zone EC</text>
  <line x1="540" y1="380" x2="880" y2="380" stroke="#5a6a7a"/>
  <path d="M540 230 L580 220 L600 340 L640 220 L660 340 L700 220 L720 340 L760 220 L780 340 L820 225 L860 340 L880 250"
        fill="none" stroke="#fbbf24" stroke-width="3"/>
  <text x="520" y="410" fill="#9aabbc" font-size="13">Bias flower / density (within cultivar limits)</text>

  <text x="48" y="500" fill="#5a6a7a" font-size="12">Fact-check pack · irrigation-manual polarity fix visual</text>
</svg>
''')

print("All SVG diagrams written to", OUT)
