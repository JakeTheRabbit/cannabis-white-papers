# -*- coding: utf-8 -*-
"""v2 diagrams from user review feedback 2026-07-19."""
from pathlib import Path

OUT = Path(__file__).resolve().parent


def write(name: str, svg: str) -> None:
    p = OUT / name
    p.write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", p.name)


# 02 — moisture vs aw + bud cross-section concept
write("02-moisture-vs-water-activity.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1100" height="640" fill="#0f1419"/>
  <text x="40" y="42" fill="#e7ecf3" font-size="24" font-weight="700">Moisture content ≠ water activity — read it on the flower</text>
  <text x="40" y="70" fill="#9aabbc" font-size="14">Same bulk “11% moisture” can span unsafe aw. Water activity is about free water at the tissue scale.</text>

  <!-- LEFT: bud cross section -->
  <rect x="36" y="100" width="420" height="480" rx="14" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="56" y="135" fill="#38bdf8" font-size="16" font-weight="700">A · Bud tissue (schematic cutaway)</text>
  <!-- bud shape -->
  <ellipse cx="240" cy="340" rx="130" ry="160" fill="#1e3a2f" stroke="#2a9d8f" stroke-width="2"/>
  <ellipse cx="240" cy="340" rx="90" ry="120" fill="#234a3a"/>
  <ellipse cx="240" cy="340" rx="45" ry="70" fill="#2f5d48"/>
  <!-- water droplets free vs bound -->
  <circle cx="200" cy="300" r="8" fill="#38bdf8" opacity="0.9"/>
  <circle cx="260" cy="320" r="6" fill="#38bdf8" opacity="0.7"/>
  <circle cx="230" cy="360" r="7" fill="#38bdf8" opacity="0.85"/>
  <circle cx="280" cy="280" r="5" fill="#64748b"/>
  <circle cx="190" cy="380" r="5" fill="#64748b"/>
  <circle cx="250" cy="400" r="4" fill="#64748b"/>
  <text x="56" y="520" fill="#38bdf8" font-size="13">● free water (drives aw / mould risk)</text>
  <text x="56" y="545" fill="#94a3b8" font-size="13">● bound / less available water (still in moisture %)</text>
  <text x="56" y="570" fill="#9aabbc" font-size="12">Micro view is conceptual — aw meters measure vapour equilibrium.</text>

  <!-- RIGHT: gauges -->
  <rect x="480" y="100" width="580" height="220" rx="14" fill="#1a2332" stroke="#ff8a4c"/>
  <text x="500" y="135" fill="#ff8a4c" font-size="16" font-weight="700">B · Cheap moisture meter</text>
  <text x="500" y="175" fill="#e7ecf3" font-size="42" font-weight="700">11% moisture</text>
  <text x="500" y="210" fill="#9aabbc" font-size="14">±1% instrument error common</text>
  <text x="500" y="250" fill="#ff5c5c" font-size="15">can mean aw ~0.53 (too dry) …</text>
  <text x="500" y="280" fill="#fbbf24" font-size="15">… or aw ~0.60 (safe) …</text>
  <text x="500" y="310" fill="#ff8a4c" font-size="15">… or aw ~0.66 (mould risk rising)</text>

  <rect x="480" y="340" width="580" height="240" rx="14" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="500" y="375" fill="#34d399" font-size="16" font-weight="700">C · Water activity (aw) — the safety gauge</text>
  <rect x="520" y="410" width="500" height="40" rx="8" fill="#2d3a4d"/>
  <rect x="520" y="410" width="150" height="40" rx="8" fill="#7f1d1d"/>
  <rect x="670" y="410" width="200" height="40" fill="#166534"/>
  <rect x="870" y="410" width="150" height="40" rx="0 8 8 0" fill="#9a3412"/>
  <text x="560" y="475" fill="#ff5c5c" font-size="13">&lt;0.55 dry</text>
  <text x="720" y="475" fill="#34d399" font-size="13">0.55–0.65 ASTM</text>
  <text x="900" y="475" fill="#ff8a4c" font-size="13">&gt;0.65 risk</text>
  <text x="500" y="520" fill="#e7ecf3" font-size="18" font-weight="600">Take-down ~0.60–0.62  ·  Finish cure ~0.58–0.60</text>
  <text x="500" y="555" fill="#9aabbc" font-size="13">Mould risk climbs hard near ~0.70+. Steer aw, not moisture alone.</text>

  <text x="40" y="620" fill="#5a6a7a" font-size="12">v2 · fact-check pack · educational (not a lab photo of aw measurement)</text>
</svg>
''')

# 03 — real-looking dual graphs with numbers
write("03-leaf-vs-canopy-light.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1100" height="640" fill="#0f1419"/>
  <text x="40" y="40" fill="#e7ecf3" font-size="22" font-weight="700">Leaf gas exchange saturates earlier than whole-canopy flower yield</text>
  <text x="40" y="66" fill="#9aabbc" font-size="13">Illustrative curves with labelled points (directionally consistent with leaf gas-exchange vs canopy yield literature such as RM2021). Not a raw data dump.</text>

  <!-- LEFT chart leaf -->
  <rect x="36" y="90" width="500" height="480" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="56" y="125" fill="#38bdf8" font-size="16" font-weight="700">A · Single-leaf net photosynthesis (relative)</text>
  <!-- grid -->
  <g stroke="#2d3a4d" stroke-width="1">
    <line x1="100" y1="180" x2="480" y2="180"/><line x1="100" y1="250" x2="480" y2="250"/>
    <line x1="100" y1="320" x2="480" y2="320"/><line x1="100" y1="390" x2="480" y2="390"/>
    <line x1="100" y1="460" x2="480" y2="460"/>
  </g>
  <line x1="100" y1="460" x2="480" y2="460" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="100" y1="460" x2="100" y2="170" stroke="#5a6a7a" stroke-width="2"/>
  <!-- points: PPFD 200,500,800,1000,1200,1500  relative Anet ~35,70,90,95,97,98 -->
  <!-- x: 100->480 = 380 for 0-1600, y: 460->170 = 290 for 0-100 -->
  <!-- x=100+ppfd/1600*380, y=460-anet/100*290 -->
  <polyline fill="none" stroke="#38bdf8" stroke-width="3"
    points="147.5,358.5 218.8,257 290,199 337.5,184.5 385,178.7 456.3,175.8"/>
  <g fill="#38bdf8">
    <circle cx="147.5" cy="358.5" r="5"/><circle cx="218.8" cy="257" r="5"/>
    <circle cx="290" cy="199" r="5"/><circle cx="337.5" cy="184.5" r="5"/>
    <circle cx="385" cy="178.7" r="5"/><circle cx="456.3" cy="175.8" r="5"/>
  </g>
  <text x="100" y="490" fill="#5a6a7a" font-size="11">0</text>
  <text x="195" y="490" fill="#5a6a7a" font-size="11">400</text>
  <text x="290" y="490" fill="#5a6a7a" font-size="11">800</text>
  <text x="385" y="490" fill="#5a6a7a" font-size="11">1200</text>
  <text x="456" y="490" fill="#5a6a7a" font-size="11">1600</text>
  <text x="250" y="515" fill="#9aabbc" font-size="12">PPFD (µmol m⁻² s⁻¹)</text>
  <text x="70" y="320" fill="#9aabbc" font-size="11" transform="rotate(-90 70 320)">Relative Anet (0–100)</text>
  <text x="300" y="195" fill="#fbbf24" font-size="12">flattens ~800–1000</text>
  <text x="56" y="545" fill="#9aabbc" font-size="12">Example points: 200→35 · 500→70 · 800→90 · 1200→97 · 1500→98</text>

  <!-- RIGHT canopy yield -->
  <rect x="560" y="90" width="500" height="480" rx="12" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="580" y="125" fill="#34d399" font-size="16" font-weight="700">B · Whole-canopy dry flower yield (relative)</text>
  <g stroke="#2d3a4d" stroke-width="1">
    <line x1="620" y1="180" x2="1000" y2="180"/><line x1="620" y1="250" x2="1000" y2="250"/>
    <line x1="620" y1="320" x2="1000" y2="320"/><line x1="620" y1="390" x2="1000" y2="390"/>
    <line x1="620" y1="460" x2="1000" y2="460"/>
  </g>
  <line x1="620" y1="460" x2="1000" y2="460" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="620" y1="460" x2="620" y2="170" stroke="#5a6a7a" stroke-width="2"/>
  <!-- roughly linear: 200=25, 500=40, 800=55, 1000=65, 1200=78, 1500=92, 1800=100 -->
  <polyline fill="none" stroke="#34d399" stroke-width="3"
    points="667.5,387.5 738.8,344 810,300.5 857.5,271.5 905,233.8 976.3,193.2 1020,170"/>
  <g fill="#34d399">
    <circle cx="667.5" cy="387.5" r="5"/><circle cx="738.8" cy="344" r="5"/>
    <circle cx="810" cy="300.5" r="5"/><circle cx="857.5" cy="271.5" r="5"/>
    <circle cx="905" cy="233.8" r="5"/><circle cx="976.3" cy="193.2" r="5"/>
  </g>
  <text x="620" y="490" fill="#5a6a7a" font-size="11">0</text>
  <text x="715" y="490" fill="#5a6a7a" font-size="11">400</text>
  <text x="810" y="490" fill="#5a6a7a" font-size="11">800</text>
  <text x="905" y="490" fill="#5a6a7a" font-size="11">1200</text>
  <text x="990" y="490" fill="#5a6a7a" font-size="11">1600+</text>
  <text x="760" y="515" fill="#9aabbc" font-size="12">PPFD (µmol m⁻² s⁻¹)</text>
  <text x="900" y="200" fill="#34d399" font-size="12">still rising ~1500–1800</text>
  <text x="580" y="545" fill="#9aabbc" font-size="12">Example relative yield: 200→25 · 800→55 · 1200→78 · 1500→92 · 1800→100</text>

  <text x="40" y="615" fill="#5a6a7a" font-size="12">v2 · Not a hard “800 wall” under ambient CO₂ — diminishing returns at the leaf; canopy yield can keep climbing with support (CO₂, climate, water).</text>
</svg>
''')

# 04 Caplan vs daily with real numbers
write("04-caplan-vs-daily-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 640" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1100" height="640" fill="#0f1419"/>
  <text x="40" y="40" fill="#e7ecf3" font-size="22" font-weight="700">One late drought study ≠ daily crop-steering drybacks</text>
  <text x="40" y="66" fill="#9aabbc" font-size="13">Example VWC (%) traces with labelled points — educational, not a specific facility’s probe calibration.</text>

  <!-- A -->
  <rect x="36" y="90" width="480" height="480" rx="12" fill="#1a2332" stroke="#fbbf24"/>
  <text x="56" y="125" fill="#fbbf24" font-size="16" font-weight="700">A · Single late-flower drought (study-style)</text>
  <line x1="90" y1="480" x2="470" y2="480" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="90" y1="480" x2="90" y2="170" stroke="#5a6a7a" stroke-width="2"/>
  <!-- days 0-14 on x, VWC 70 flat then drop to 35 then recover -->
  <polyline fill="none" stroke="#fbbf24" stroke-width="3"
    points="90,230 180,230 200,230 280,400 360,400 400,250 470,230"/>
  <g fill="#fbbf24">
    <circle cx="90" cy="230" r="4"/><circle cx="200" cy="230" r="4"/>
    <circle cx="280" cy="400" r="4"/><circle cx="360" cy="400" r="4"/>
    <circle cx="470" cy="230" r="4"/>
  </g>
  <text x="95" y="220" fill="#e7ecf3" font-size="12">70%</text>
  <text x="285" y="420" fill="#e7ecf3" font-size="12">~35% trough</text>
  <text x="400" y="240" fill="#e7ecf3" font-size="12">re-wet</text>
  <text x="200" y="510" fill="#9aabbc" font-size="12">Day of late flower →</text>
  <text x="56" y="540" fill="#9aabbc" font-size="13">One long controlled dry event (example ~11 days in literature framing)</text>

  <text x="540" y="330" fill="#ff5c5c" font-size="36" font-weight="700" text-anchor="middle">≠</text>

  <!-- B -->
  <rect x="580" y="90" width="480" height="480" rx="12" fill="#1a2332" stroke="#34d399" stroke-width="2"/>
  <text x="600" y="125" fill="#34d399" font-size="16" font-weight="700">B · Daily dryback sawtooth (steering)</text>
  <line x1="630" y1="480" x2="1020" y2="480" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="630" y1="480" x2="630" y2="170" stroke="#5a6a7a" stroke-width="2"/>
  <!-- peaks 75 troughs 55 = 20 pts over many days -->
  <polyline fill="none" stroke="#34d399" stroke-width="2.5"
    points="630,220 660,220 680,340 710,220 730,340 760,220 780,340 810,220 830,340 860,220 880,340 910,220 930,340 960,220 980,340 1010,220"/>
  <text x="650" y="210" fill="#e7ecf3" font-size="12">peak ~75%</text>
  <text x="680" y="360" fill="#e7ecf3" font-size="12">trough ~55%</text>
  <text x="780" y="400" fill="#34d399" font-size="14" font-weight="600">≈ 20 percentage POINTS each day</text>
  <text x="750" y="510" fill="#9aabbc" font-size="12">Many irrigation days →</text>
  <text x="600" y="540" fill="#9aabbc" font-size="13">Related idea (mild deficit), different experiment / SOP</text>

  <text x="40" y="610" fill="#5a6a7a" font-size="12">v2 · Caplan-style late drought vs commercial daily drybacks — do not cite one as the other</text>
</svg>
''')

# 06 clean flow with post-harvest gown barrier
write("06-clean-to-dirty-flow.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1100" height="680" fill="#0f1419"/>
  <text x="40" y="40" fill="#e7ecf3" font-size="22" font-weight="700">Facility flow: clean → dirty, with a hard wall before post-harvest</text>
  <text x="40" y="68" fill="#9aabbc" font-size="13">Do not walk flower → dry/trim/pack in the same coveralls. Post-harvest is lowest-microbial zone for product.</text>

  <!-- cultivation track -->
  <text x="40" y="110" fill="#38bdf8" font-size="14" font-weight="600">CULTIVATION TRACK (one gowning direction)</text>
  <g font-size="13" font-weight="600">
    <rect x="36" y="130" width="150" height="70" rx="10" fill="#166534" stroke="#34d399"/>
    <text x="111" y="160" text-anchor="middle" fill="#e7ecf3">Gown-in</text>
    <text x="111" y="180" text-anchor="middle" fill="#bbf7d0" font-size="11">CLEAN kit</text>

    <rect x="220" y="130" width="150" height="70" rx="10" fill="#14532d" stroke="#34d399"/>
    <text x="295" y="160" text-anchor="middle" fill="#e7ecf3">Mothers / Prop</text>
    <text x="295" y="180" text-anchor="middle" fill="#bbf7d0" font-size="11">cleanest crop</text>

    <rect x="404" y="130" width="130" height="70" rx="10" fill="#1e3a5f" stroke="#38bdf8"/>
    <text x="469" y="170" text-anchor="middle" fill="#e7ecf3">Veg</text>

    <rect x="568" y="130" width="130" height="70" rx="10" fill="#713f12" stroke="#fbbf24"/>
    <text x="633" y="170" text-anchor="middle" fill="#e7ecf3">Flower</text>
  </g>
  <defs>
    <marker id="aG" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#34d399"/></marker>
    <marker id="aR" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#ff5c5c"/></marker>
    <marker id="aA" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="#fbbf24"/></marker>
  </defs>
  <line x1="186" y1="165" x2="215" y2="165" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>
  <line x1="370" y1="165" x2="399" y2="165" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>
  <line x1="534" y1="165" x2="563" y2="165" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>

  <!-- BARRIER -->
  <rect x="720" y="110" width="28" height="110" fill="#7f1d1d"/>
  <text x="734" y="250" text-anchor="middle" fill="#ff5c5c" font-size="12" font-weight="700" transform="rotate(-90 734 250)">HARD STOP</text>

  <rect x="770" y="120" width="280" height="90" rx="12" fill="#3f1d1d" stroke="#ff5c5c" stroke-width="2"/>
  <text x="910" y="155" text-anchor="middle" fill="#fecaca" font-size="15" font-weight="700">✕ NO same coveralls</text>
  <text x="910" y="180" text-anchor="middle" fill="#fecaca" font-size="13">Flower kit does NOT enter</text>
  <text x="910" y="200" text-anchor="middle" fill="#fecaca" font-size="13">dry / trim / pack rooms</text>

  <!-- exit flower -->
  <rect x="36" y="280" width="660" height="100" rx="12" fill="#1a2332" stroke="#fbbf24"/>
  <text x="56" y="315" fill="#fbbf24" font-size="15" font-weight="700">Leaving flower / cultivation</text>
  <text x="56" y="345" fill="#e7ecf3" font-size="14">1) De-gown dirty kit  ·  2) Exit to grey / locker  ·  3) Fresh clean kit only for post-harvest entry</text>
  <text x="56" y="370" fill="#9aabbc" font-size="13">Product moves in covered totes; people re-gown — two different paths.</text>

  <!-- post harvest track -->
  <text x="40" y="430" fill="#34d399" font-size="14" font-weight="600">POST-HARVEST TRACK (separate clean entry — lowest microbial load on finished flower)</text>
  <g font-size="13" font-weight="600">
    <rect x="36" y="450" width="160" height="70" rx="10" fill="#166534" stroke="#34d399"/>
    <text x="116" y="480" text-anchor="middle" fill="#e7ecf3">Fresh gown-in</text>
    <text x="116" y="500" text-anchor="middle" fill="#bbf7d0" font-size="11">clean PH kit</text>

    <rect x="230" y="450" width="150" height="70" rx="10" fill="#0f3d2e" stroke="#34d399"/>
    <text x="305" y="480" text-anchor="middle" fill="#e7ecf3">Dry room</text>
    <text x="305" y="500" text-anchor="middle" fill="#bbf7d0" font-size="11">low traffic</text>

    <rect x="414" y="450" width="150" height="70" rx="10" fill="#0f3d2e" stroke="#34d399"/>
    <text x="489" y="480" text-anchor="middle" fill="#e7ecf3">Trim / pack</text>
    <text x="489" y="500" text-anchor="middle" fill="#bbf7d0" font-size="11">product contact</text>

    <rect x="598" y="450" width="150" height="70" rx="10" fill="#1e293b" stroke="#64748b"/>
    <text x="673" y="480" text-anchor="middle" fill="#e7ecf3">Vault / ship</text>
    <text x="673" y="500" text-anchor="middle" fill="#94a3b8" font-size="11">finished goods</text>
  </g>
  <line x1="196" y1="485" x2="225" y2="485" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>
  <line x1="380" y1="485" x2="409" y2="485" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>
  <line x1="564" y1="485" x2="593" y2="485" stroke="#34d399" stroke-width="3" marker-end="url(#aG)"/>

  <!-- waste -->
  <rect x="800" y="450" width="240" height="70" rx="10" fill="#3f1d1d" stroke="#ff5c5c"/>
  <text x="920" y="480" text-anchor="middle" fill="#fecaca" font-size="14" font-weight="700">Waste / used PPE exit</text>
  <text x="920" y="502" text-anchor="middle" fill="#fecaca" font-size="12">dirty → out only</text>

  <rect x="36" y="560" width="1000" height="70" rx="12" fill="#1a2332" stroke="#ff5c5c"/>
  <text x="56" y="595" fill="#ff5c5c" font-size="16" font-weight="700">Why: dry, trim and storage fail from microbes that ride on people and clothes from flower.</text>
  <text x="56" y="618" fill="#9aabbc" font-size="13">Treat post-harvest as its own clean room class — not “next door after flower.”</text>

  <text x="40" y="660" fill="#5a6a7a" font-size="12">v2 · review feedback: no flower coveralls into post-harvest</text>
</svg>
''')

# 08 veg/gen with phases and real graph numbers
write("08-veg-vs-gen-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 680" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1100" height="680" fill="#0f1419"/>
  <text x="40" y="40" fill="#e7ecf3" font-size="22" font-weight="700">Crop steering polarity with example VWC phases</text>
  <text x="40" y="66" fill="#9aabbc" font-size="13">Probe-native example numbers (one facility style). Recalibrate for your media — not universal %.</text>

  <!-- phase legend -->
  <rect x="36" y="90" width="1028" height="70" rx="10" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="56" y="120" fill="#9aabbc" font-size="13" font-weight="600">Example phases:</text>
  <text x="56" y="145" fill="#38bdf8" font-size="13">P0/Veg: field capacity ~70–75%, dryback ~10–15 pts  ·  </text>
  <text x="520" y="145" fill="#fbbf24" font-size="13">P1–P2 Generative: peak ~70–75%, dryback ~20–30 pts  ·  </text>
  <text x="900" y="145" fill="#a78bfa" font-size="13">P3 finish: ease</text>

  <!-- main graph -->
  <rect x="36" y="180" width="1028" height="420" rx="12" fill="#1a2332" stroke="#2d3a4d"/>
  <text x="56" y="215" fill="#e7ecf3" font-size="15" font-weight="700">Substrate VWC (%) over days — example continuous crop</text>

  <!-- phase bands background -->
  <rect x="100" y="240" width="280" height="260" fill="#0c4a6e" opacity="0.25"/>
  <rect x="380" y="240" width="400" height="260" fill="#713f12" opacity="0.2"/>
  <rect x="780" y="240" width="240" height="260" fill="#4c1d95" opacity="0.2"/>
  <text x="200" y="265" fill="#38bdf8" font-size="13" font-weight="600">VEG / P0</text>
  <text x="520" y="265" fill="#fbbf24" font-size="13" font-weight="600">GENERATIVE P1–P2</text>
  <text x="860" y="265" fill="#c4b5fd" font-size="13" font-weight="600">P3 / finish</text>

  <line x1="100" y1="500" x2="1020" y2="500" stroke="#5a6a7a" stroke-width="2"/>
  <line x1="100" y1="500" x2="100" y2="240" stroke="#5a6a7a" stroke-width="2"/>
  <!-- y labels -->
  <text x="90" y="505" text-anchor="end" fill="#5a6a7a" font-size="11">40</text>
  <text x="90" y="435" text-anchor="end" fill="#5a6a7a" font-size="11">55</text>
  <text x="90" y="365" text-anchor="end" fill="#5a6a7a" font-size="11">65</text>
  <text x="90" y="295" text-anchor="end" fill="#5a6a7a" font-size="11">75</text>
  <text x="90" y="255" text-anchor="end" fill="#5a6a7a" font-size="11">80</text>

  <!-- veg small drybacks: 72-60 = 12 pts -->
  <polyline fill="none" stroke="#38bdf8" stroke-width="2.5"
    points="110,310 140,310 155,380 185,310 200,380 230,310 245,380 275,310 290,380 320,310 335,380 365,310"/>
  <!-- gen larger: 74-50 = 24 pts -->
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.5"
    points="390,300 420,300 440,450 470,295 490,450 520,295 540,450 570,295 590,450 620,295 640,450 670,295 690,450 720,300 750,450 770,310"/>
  <!-- p3 milder -->
  <polyline fill="none" stroke="#a78bfa" stroke-width="2.5"
    points="800,320 830,320 850,400 880,320 900,400 930,320 950,400 980,330 1000,390 1020,340"/>

  <text x="150" y="530" fill="#38bdf8" font-size="12">~12 pt drybacks · stay wetter</text>
  <text x="500" y="530" fill="#fbbf24" font-size="12">~24 pt drybacks · larger controlled deficit</text>
  <text x="820" y="530" fill="#a78bfa" font-size="12">eased drybacks / lower push</text>
  <text x="500" y="560" fill="#9aabbc" font-size="12" text-anchor="middle">Time (days of crop) →</text>
  <text x="56" y="580" fill="#9aabbc" font-size="13">Example peaks ~72–75% · veg trough ~60% · generative trough ~50% · always media- and probe-specific</text>

  <text x="40" y="650" fill="#5a6a7a" font-size="12">v2 · Veg = smaller drybacks; Generative = larger controlled drybacks (matches F2 / mainstream steering)</text>
</svg>
''')

print("v2 diagrams done")
