# -*- coding: utf-8 -*-
"""v3 diagrams from overridden review JSON 2026-07-19 12:44."""
from pathlib import Path

OUT = Path(__file__).resolve().parent


def write(name: str, svg: str) -> None:
    (OUT / name).write_text(svg.strip() + "\n", encoding="utf-8")
    print("wrote", name)


# --- 03: publication-style dual graphs ---
write("03-leaf-vs-canopy-light.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1200" height="720" fill="#0b0f14"/>
  <text x="48" y="44" fill="#f1f5f9" font-size="26" font-weight="700">Leaf saturation ≠ canopy flower-yield ceiling</text>
  <text x="48" y="74" fill="#94a3b8" font-size="14">Illustrative relative curves with labelled axes and points. Direction matches leaf gas-exchange vs whole-canopy yield literature (e.g. Rodriguez-Morrison et al. 2021). Not a raw data replot.</text>

  <!-- LEFT -->
  <rect x="40" y="100" width="540" height="540" rx="14" fill="#111827" stroke="#334155"/>
  <text x="60" y="140" fill="#38bdf8" font-size="18" font-weight="700">A. Single-leaf net photosynthesis</text>
  <text x="60" y="165" fill="#64748b" font-size="13">Relative Anet (ambient CO₂), index 0–100</text>

  <!-- y grid + labels: 100 at y=200, 0 at y=560; x: 0@120, 1600@520 -->
  <g stroke="#1e293b" stroke-width="1">
    <line x1="120" y1="200" x2="520" y2="200"/>
    <line x1="120" y1="290" x2="520" y2="290"/>
    <line x1="120" y1="380" x2="520" y2="380"/>
    <line x1="120" y1="470" x2="520" y2="470"/>
    <line x1="120" y1="560" x2="520" y2="560"/>
  </g>
  <line x1="120" y1="560" x2="520" y2="560" stroke="#64748b" stroke-width="2"/>
  <line x1="120" y1="560" x2="120" y2="200" stroke="#64748b" stroke-width="2"/>
  <text x="108" y="565" text-anchor="end" fill="#94a3b8" font-size="12">0</text>
  <text x="108" y="475" text-anchor="end" fill="#94a3b8" font-size="12">25</text>
  <text x="108" y="385" text-anchor="end" fill="#94a3b8" font-size="12">50</text>
  <text x="108" y="295" text-anchor="end" fill="#94a3b8" font-size="12">75</text>
  <text x="108" y="205" text-anchor="end" fill="#94a3b8" font-size="12">100</text>
  <text x="120" y="590" fill="#94a3b8" font-size="12">0</text>
  <text x="220" y="590" fill="#94a3b8" font-size="12">400</text>
  <text x="320" y="590" fill="#94a3b8" font-size="12">800</text>
  <text x="420" y="590" fill="#94a3b8" font-size="12">1200</text>
  <text x="500" y="590" fill="#94a3b8" font-size="12">1600</text>
  <text x="280" y="620" fill="#cbd5e1" font-size="13">PPFD (µmol·m⁻²·s⁻¹)</text>
  <text x="48" y="400" fill="#94a3b8" font-size="12" transform="rotate(-90 48 400)">Relative Anet</text>

  <!-- saturating: 200→35, 400→60, 600→80, 800→90, 1000→95, 1200→97, 1500→98 -->
  <!-- x = 120 + ppfd/1600*400; y = 560 - anet/100*360 -->
  <polyline fill="none" stroke="#38bdf8" stroke-width="3.5"
    points="170,434 220,344 270,272 320,236 370,218 420,210.8 495,207.2"/>
  <g fill="#38bdf8">
    <circle cx="170" cy="434" r="5"/><circle cx="220" cy="344" r="5"/>
    <circle cx="270" cy="272" r="5"/><circle cx="320" cy="236" r="5"/>
    <circle cx="370" cy="218" r="5"/><circle cx="420" cy="210.8" r="5"/>
    <circle cx="495" cy="207.2" r="5"/>
  </g>
  <text x="325" y="225" fill="#fbbf24" font-size="13" font-weight="600">~90 at 800</text>
  <text x="400" y="200" fill="#fbbf24" font-size="13">plateau ~95–98</text>
  <text x="140" y="455" fill="#e2e8f0" font-size="11">200→35</text>
  <text x="60" y="640" fill="#64748b" font-size="12">Start 200 PPFD · Mid 800 · End 1500 — leaf response flattens early</text>

  <!-- RIGHT -->
  <rect x="620" y="100" width="540" height="540" rx="14" fill="#111827" stroke="#166534" stroke-width="2"/>
  <text x="640" y="140" fill="#4ade80" font-size="18" font-weight="700">B. Whole-canopy dry flower yield</text>
  <text x="640" y="165" fill="#64748b" font-size="13">Relative yield index 0–100 (ambient CO₂ room)</text>

  <g stroke="#1e293b" stroke-width="1">
    <line x1="700" y1="200" x2="1100" y2="200"/>
    <line x1="700" y1="290" x2="1100" y2="290"/>
    <line x1="700" y1="380" x2="1100" y2="380"/>
    <line x1="700" y1="470" x2="1100" y2="470"/>
    <line x1="700" y1="560" x2="1100" y2="560"/>
  </g>
  <line x1="700" y1="560" x2="1100" y2="560" stroke="#64748b" stroke-width="2"/>
  <line x1="700" y1="560" x2="700" y2="200" stroke="#64748b" stroke-width="2"/>
  <text x="688" y="565" text-anchor="end" fill="#94a3b8" font-size="12">0</text>
  <text x="688" y="475" text-anchor="end" fill="#94a3b8" font-size="12">25</text>
  <text x="688" y="385" text-anchor="end" fill="#94a3b8" font-size="12">50</text>
  <text x="688" y="295" text-anchor="end" fill="#94a3b8" font-size="12">75</text>
  <text x="688" y="205" text-anchor="end" fill="#94a3b8" font-size="12">100</text>
  <text x="700" y="590" fill="#94a3b8" font-size="12">0</text>
  <text x="800" y="590" fill="#94a3b8" font-size="12">400</text>
  <text x="900" y="590" fill="#94a3b8" font-size="12">800</text>
  <text x="1000" y="590" fill="#94a3b8" font-size="12">1200</text>
  <text x="1080" y="590" fill="#94a3b8" font-size="12">1600</text>
  <text x="860" y="620" fill="#cbd5e1" font-size="13">PPFD (µmol·m⁻²·s⁻¹)</text>
  <text x="640" y="400" fill="#94a3b8" font-size="12" transform="rotate(-90 640 400)">Relative yield</text>

  <!-- nearly linear: 200→22, 400→35, 600→48, 800→58, 1000→68, 1200→78, 1500→92, 1800→100 -->
  <polyline fill="none" stroke="#4ade80" stroke-width="3.5"
    points="750,480.8 800,434 850,387.2 900,351.2 950,315.2 1000,279.2 1075,228.8 1120,200"/>
  <g fill="#4ade80">
    <circle cx="750" cy="480.8" r="5"/><circle cx="800" cy="434" r="5"/>
    <circle cx="850" cy="387.2" r="5"/><circle cx="900" cy="351.2" r="5"/>
    <circle cx="950" cy="315.2" r="5"/><circle cx="1000" cy="279.2" r="5"/>
    <circle cx="1075" cy="228.8" r="5"/>
  </g>
  <text x="905" y="345" fill="#86efac" font-size="13" font-weight="600">58 at 800</text>
  <text x="1020" y="220" fill="#86efac" font-size="13">~92 at 1500</text>
  <text x="755" y="505" fill="#e2e8f0" font-size="11">200→22</text>
  <text x="640" y="640" fill="#64748b" font-size="12">Still climbing past 800 — not a hard wall under ambient CO₂</text>

  <text x="48" y="700" fill="#475569" font-size="12">v3 · Educational relative indices · always pair light increases with climate, water and CO₂ capacity</text>
</svg>
''')

# --- 04 with proper time axes ---
write("04-caplan-vs-daily-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 700" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1200" height="700" fill="#0b0f14"/>
  <text x="48" y="42" fill="#f1f5f9" font-size="24" font-weight="700">One late drought study ≠ daily crop-steering drybacks</text>
  <text x="48" y="70" fill="#94a3b8" font-size="14">Both plots: Y = substrate VWC (%), X = time. Example educational traces — recalibrate for your probe/media.</text>

  <!-- A -->
  <rect x="40" y="100" width="540" height="520" rx="14" fill="#111827" stroke="#ca8a04"/>
  <text x="60" y="140" fill="#fbbf24" font-size="17" font-weight="700">A. Single late-flower drought (study-style)</text>
  <text x="60" y="165" fill="#64748b" font-size="13">One long controlled dry event, then re-wet</text>

  <g stroke="#1e293b"><line x1="100" y1="220" x2="520" y2="220"/><line x1="100" y1="300" x2="520" y2="300"/>
  <line x1="100" y1="380" x2="520" y2="380"/><line x1="100" y1="460" x2="520" y2="460"/><line x1="100" y1="540" x2="520" y2="540"/></g>
  <line x1="100" y1="540" x2="520" y2="540" stroke="#64748b" stroke-width="2"/>
  <line x1="100" y1="540" x2="100" y2="220" stroke="#64748b" stroke-width="2"/>
  <!-- VWC scale 30-80: y=540 at 30, y=220 at 80 → span 320 for 50% -->
  <text x="90" y="545" text-anchor="end" fill="#94a3b8" font-size="11">30%</text>
  <text x="90" y="465" text-anchor="end" fill="#94a3b8" font-size="11">45%</text>
  <text x="90" y="385" text-anchor="end" fill="#94a3b8" font-size="11">60%</text>
  <text x="90" y="305" text-anchor="end" fill="#94a3b8" font-size="11">70%</text>
  <text x="90" y="225" text-anchor="end" fill="#94a3b8" font-size="11">80%</text>
  <!-- x: day 0 to 16 over 100-520 -->
  <text x="100" y="565" fill="#94a3b8" font-size="11">Day 0</text>
  <text x="205" y="565" fill="#94a3b8" font-size="11">Day 4</text>
  <text x="310" y="565" fill="#94a3b8" font-size="11">Day 8</text>
  <text x="415" y="565" fill="#94a3b8" font-size="11">Day 12</text>
  <text x="500" y="565" fill="#94a3b8" font-size="11">Day 16</text>
  <text x="250" y="595" fill="#cbd5e1" font-size="13">Time (days of late flower)</text>
  <text x="55" y="400" fill="#94a3b8" font-size="12" transform="rotate(-90 55 400)">VWC (%)</text>

  <!-- 70% flat days 0-3, drop to 35 by day 11, hold, rewet day 14-16 to 70 -->
  <!-- y for 70% = 540 - (70-30)/50*320 = 540-256 = 284; 35% = 540 - 32 = 508 -->
  <polyline fill="none" stroke="#fbbf24" stroke-width="3.5"
    points="100,284 180,284 200,284 310,508 390,508 450,350 520,284"/>
  <circle cx="100" cy="284" r="5" fill="#fbbf24"/>
  <circle cx="310" cy="508" r="5" fill="#fbbf24"/>
  <circle cx="520" cy="284" r="5" fill="#fbbf24"/>
  <text x="110" y="275" fill="#fef3c7" font-size="12">70%</text>
  <text x="320" y="530" fill="#fef3c7" font-size="12">~35% trough</text>
  <text x="430" y="340" fill="#fef3c7" font-size="12">re-wet → 70%</text>
  <text x="60" y="620" fill="#94a3b8" font-size="12">≈ one multi-day drought (literature-style), not daily pulses</text>

  <text x="600" y="380" fill="#f87171" font-size="42" font-weight="700" text-anchor="middle">≠</text>
  <text x="600" y="415" fill="#f87171" font-size="14" text-anchor="middle">not the same</text>

  <!-- B -->
  <rect x="640" y="100" width="520" height="520" rx="14" fill="#111827" stroke="#16a34a" stroke-width="2"/>
  <text x="660" y="140" fill="#4ade80" font-size="17" font-weight="700">B. Daily dryback sawtooth (steering)</text>
  <text x="660" y="165" fill="#64748b" font-size="13">Many small wet–dry cycles (example 20-point drybacks)</text>

  <g stroke="#1e293b"><line x1="700" y1="220" x2="1110" y2="220"/><line x1="700" y1="300" x2="1110" y2="300"/>
  <line x1="700" y1="380" x2="1110" y2="380"/><line x1="700" y1="460" x2="1110" y2="460"/><line x1="700" y1="540" x2="1110" y2="540"/></g>
  <line x1="700" y1="540" x2="1110" y2="540" stroke="#64748b" stroke-width="2"/>
  <line x1="700" y1="540" x2="700" y2="220" stroke="#64748b" stroke-width="2"/>
  <text x="690" y="545" text-anchor="end" fill="#94a3b8" font-size="11">30%</text>
  <text x="690" y="465" text-anchor="end" fill="#94a3b8" font-size="11">45%</text>
  <text x="690" y="385" text-anchor="end" fill="#94a3b8" font-size="11">60%</text>
  <text x="690" y="305" text-anchor="end" fill="#94a3b8" font-size="11">70%</text>
  <text x="690" y="225" text-anchor="end" fill="#94a3b8" font-size="11">80%</text>
  <text x="700" y="565" fill="#94a3b8" font-size="11">Day 0</text>
  <text x="800" y="565" fill="#94a3b8" font-size="11">Day 2</text>
  <text x="900" y="565" fill="#94a3b8" font-size="11">Day 4</text>
  <text x="1000" y="565" fill="#94a3b8" font-size="11">Day 6</text>
  <text x="1085" y="565" fill="#94a3b8" font-size="11">Day 8</text>
  <text x="850" y="595" fill="#cbd5e1" font-size="13">Time (days of irrigation cycle)</text>
  <text x="655" y="400" fill="#94a3b8" font-size="12" transform="rotate(-90 655 400)">VWC (%)</text>

  <!-- peak 75 y=284-ish: 75% = 540-(45/50)*320=252; trough 55 = 540-(25/50)*320=380 -->
  <!-- wait use same scale: 30@540, 80@220, y=540-(v-30)/50*320 -->
  <!-- 75%: 540-288=252; 55%: 540-160=380 -->
  <polyline fill="none" stroke="#4ade80" stroke-width="3"
    points="700,252 740,252 760,380 800,252 820,380 860,252 880,380 920,252 940,380 980,252 1000,380 1040,252 1060,380 1100,252"/>
  <text x="710" y="245" fill="#bbf7d0" font-size="12">peak 75%</text>
  <text x="770" y="400" fill="#bbf7d0" font-size="12">trough 55%</text>
  <text x="860" y="430" fill="#4ade80" font-size="14" font-weight="700">20 percentage POINTS / day</text>
  <text x="660" y="620" fill="#94a3b8" font-size="12">Related idea (mild deficit), different experiment from panel A</text>

  <text x="48" y="680" fill="#475569" font-size="12">v3 · Explicit time axis (days) + VWC % axis on both panels</text>
</svg>
''')

# --- 06: even clearer PH barrier ---
write("06-clean-to-dirty-flow.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 760" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1200" height="760" fill="#0b0f14"/>
  <text x="40" y="42" fill="#f1f5f9" font-size="24" font-weight="700">Two gowning systems: cultivation ≠ post-harvest</text>
  <text x="40" y="72" fill="#94a3b8" font-size="14">Post-harvest (dry / trim / pack) needs the lowest microbial load. Flower coveralls never enter those rooms.</text>

  <!-- CULT track -->
  <rect x="36" y="100" width="1128" height="220" rx="14" fill="#111827" stroke="#334155"/>
  <text x="56" y="135" fill="#38bdf8" font-size="16" font-weight="700">TRACK 1 — CULTIVATION (direction: cleaner → dirtier crop rooms)</text>
  <g font-size="13" font-weight="600">
    <rect x="56" y="160" width="160" height="80" rx="10" fill="#14532d" stroke="#22c55e"/>
    <text x="136" y="195" text-anchor="middle" fill="#f0fdf4">Gown-in A</text>
    <text x="136" y="218" text-anchor="middle" fill="#86efac" font-size="12">cultivation kit</text>
    <rect x="260" y="160" width="160" height="80" rx="10" fill="#166534" stroke="#22c55e"/>
    <text x="340" y="195" text-anchor="middle" fill="#f0fdf4">Mothers / Prop</text>
    <text x="340" y="218" text-anchor="middle" fill="#86efac" font-size="12">clean stock</text>
    <rect x="464" y="160" width="140" height="80" rx="10" fill="#1e3a5f" stroke="#38bdf8"/>
    <text x="534" y="205" text-anchor="middle" fill="#e0f2fe">Veg</text>
    <rect x="648" y="160" width="140" height="80" rx="10" fill="#713f12" stroke="#f59e0b"/>
    <text x="718" y="205" text-anchor="middle" fill="#fef3c7">Flower</text>
    <rect x="832" y="160" width="200" height="80" rx="10" fill="#3f1d1d" stroke="#ef4444"/>
    <text x="932" y="195" text-anchor="middle" fill="#fecaca">De-gown A / exit</text>
    <text x="932" y="218" text-anchor="middle" fill="#fca5a5" font-size="12">dirty kit off</text>
  </g>
  <defs>
    <marker id="g" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#22c55e"/></marker>
  </defs>
  <line x1="216" y1="200" x2="255" y2="200" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <line x1="420" y1="200" x2="459" y2="200" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <line x1="604" y1="200" x2="643" y2="200" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <line x1="788" y1="200" x2="827" y2="200" stroke="#ef4444" stroke-width="3" marker-end="url(#g)"/>
  <text x="56" y="280" fill="#94a3b8" font-size="13">People and plant work stay on this track. Product leaves in covered totes — not on dirty clothes into the dry room.</text>

  <!-- WALL -->
  <rect x="36" y="340" width="1128" height="70" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
  <text x="600" y="372" text-anchor="middle" fill="#fecaca" font-size="18" font-weight="700">✕ HARD BARRIER — no continuous walk flower → dry/trim in the same coveralls</text>
  <text x="600" y="398" text-anchor="middle" fill="#fca5a5" font-size="13">Locker / grey zone: change into a separate clean post-harvest kit (or dedicated PH staff only)</text>

  <!-- PH track -->
  <rect x="36" y="430" width="1128" height="220" rx="14" fill="#111827" stroke="#166534" stroke-width="2"/>
  <text x="56" y="465" fill="#4ade80" font-size="16" font-weight="700">TRACK 2 — POST-HARVEST (lowest microbial load on finished flower)</text>
  <g font-size="13" font-weight="600">
    <rect x="56" y="490" width="180" height="80" rx="10" fill="#14532d" stroke="#22c55e"/>
    <text x="146" y="525" text-anchor="middle" fill="#f0fdf4">Gown-in B</text>
    <text x="146" y="548" text-anchor="middle" fill="#86efac" font-size="12">fresh PH kit only</text>
    <rect x="280" y="490" width="160" height="80" rx="10" fill="#0f3d2e" stroke="#22c55e"/>
    <text x="360" y="525" text-anchor="middle" fill="#f0fdf4">Dry room</text>
    <text x="360" y="548" text-anchor="middle" fill="#86efac" font-size="12">low traffic</text>
    <rect x="484" y="490" width="160" height="80" rx="10" fill="#0f3d2e" stroke="#22c55e"/>
    <text x="564" y="525" text-anchor="middle" fill="#f0fdf4">Trim / pack</text>
    <text x="564" y="548" text-anchor="middle" fill="#86efac" font-size="12">product contact</text>
    <rect x="688" y="490" width="160" height="80" rx="10" fill="#1e293b" stroke="#64748b"/>
    <text x="768" y="525" text-anchor="middle" fill="#e2e8f0">Vault / ship</text>
    <text x="768" y="548" text-anchor="middle" fill="#94a3b8" font-size="12">finished goods</text>
    <rect x="892" y="490" width="220" height="80" rx="10" fill="#3f1d1d" stroke="#ef4444"/>
    <text x="1002" y="525" text-anchor="middle" fill="#fecaca">Waste / used PPE</text>
    <text x="1002" y="548" text-anchor="middle" fill="#fca5a5" font-size="12">dirty → exit only</text>
  </g>
  <line x1="236" y1="530" x2="275" y2="530" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <line x1="440" y1="530" x2="479" y2="530" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <line x1="644" y1="530" x2="683" y2="530" stroke="#22c55e" stroke-width="3" marker-end="url(#g)"/>
  <text x="56" y="610" fill="#94a3b8" font-size="13">Why: drying and trimming fail when flower-room microbes ride in on people. Separate kit = product protection.</text>

  <text x="40" y="690" fill="#475569" font-size="12">v3 · Explicit two-kit model: Gown-in A (cultivation) vs Gown-in B (post-harvest)</text>
  <text x="40" y="720" fill="#475569" font-size="12">Never treat post-harvest as “the next room after flower” in the same suit.</text>
</svg>
''')

# --- 08: proper continuous graph ---
write("08-veg-vs-gen-dryback.svg", r'''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720" font-family="Segoe UI, system-ui, sans-serif">
  <rect width="1200" height="720" fill="#0b0f14"/>
  <text x="48" y="40" fill="#f1f5f9" font-size="24" font-weight="700">Crop-steering VWC: vegetative vs generative drybacks</text>
  <text x="48" y="68" fill="#94a3b8" font-size="14">Example continuous sensor trace. Y = volumetric water content (%). X = crop day. Probe-native example — not universal media %.</text>

  <rect x="40" y="95" width="1120" height="560" rx="14" fill="#111827" stroke="#334155"/>

  <!-- phase bands -->
  <rect x="120" y="160" width="280" height="380" fill="#0c4a6e" opacity="0.22"/>
  <rect x="400" y="160" width="480" height="380" fill="#713f12" opacity="0.18"/>
  <rect x="880" y="160" width="240" height="380" fill="#4c1d95" opacity="0.18"/>
  <text x="200" y="185" fill="#38bdf8" font-size="14" font-weight="700">VEG / P0</text>
  <text x="560" y="185" fill="#fbbf24" font-size="14" font-weight="700">GENERATIVE P1–P2</text>
  <text x="950" y="185" fill="#c4b5fd" font-size="14" font-weight="700">P3 FINISH</text>

  <!-- grid -->
  <g stroke="#1e293b" stroke-width="1">
    <line x1="120" y1="220" x2="1120" y2="220"/>
    <line x1="120" y1="300" x2="1120" y2="300"/>
    <line x1="120" y1="380" x2="1120" y2="380"/>
    <line x1="120" y1="460" x2="1120" y2="460"/>
    <line x1="120" y1="540" x2="1120" y2="540"/>
  </g>
  <line x1="120" y1="540" x2="1120" y2="540" stroke="#64748b" stroke-width="2"/>
  <line x1="120" y1="540" x2="120" y2="160" stroke="#64748b" stroke-width="2"/>

  <!-- Y: 40% at 540, 80% at 180 → 360 span for 40% -->
  <text x="108" y="545" text-anchor="end" fill="#94a3b8" font-size="12">40%</text>
  <text x="108" y="465" text-anchor="end" fill="#94a3b8" font-size="12">50%</text>
  <text x="108" y="385" text-anchor="end" fill="#94a3b8" font-size="12">60%</text>
  <text x="108" y="305" text-anchor="end" fill="#94a3b8" font-size="12">70%</text>
  <text x="108" y="225" text-anchor="end" fill="#94a3b8" font-size="12">80%</text>
  <text x="50" y="380" fill="#94a3b8" font-size="13" transform="rotate(-90 50 380)">VWC (%)</text>

  <!-- X days 0-42: 120 to 1120 = 1000px / 42 ≈ 23.81 px/day -->
  <text x="120" y="570" fill="#94a3b8" font-size="12">Day 0</text>
  <text x="310" y="570" fill="#94a3b8" font-size="12">Day 8</text>
  <text x="500" y="570" fill="#94a3b8" font-size="12">Day 16</text>
  <text x="690" y="570" fill="#94a3b8" font-size="12">Day 24</text>
  <text x="880" y="570" fill="#94a3b8" font-size="12">Day 32</text>
  <text x="1060" y="570" fill="#94a3b8" font-size="12">Day 42</text>
  <text x="580" y="600" fill="#cbd5e1" font-size="14">Time (crop day)</text>

  <!-- Helper: y(v) = 540 - (v-40)/40*360 = 540 - (v-40)*9 -->
  <!-- veg days 0-12: peak 74 trough 62 = 12 pts -->
  <!-- gen days 12-32: peak 74 trough 50 = 24 pts -->
  <!-- p3 days 32-42: peak 70 trough 58 = 12 pts -->
  <polyline fill="none" stroke="#38bdf8" stroke-width="2.8"
    points="120,234 150,234 165,342 190,234 205,342 230,234 245,342 270,234 285,342 310,234 325,342 350,234 365,342 390,240"/>
  <polyline fill="none" stroke="#fbbf24" stroke-width="2.8"
    points="400,234 430,234 450,450 480,234 500,450 530,234 550,450 580,234 600,450 630,234 650,450 680,234 700,450 730,234 750,450 780,234 800,450 830,240 860,450 880,250"/>
  <polyline fill="none" stroke="#a78bfa" stroke-width="2.8"
    points="890,270 920,270 940,378 970,270 990,378 1020,270 1040,378 1070,280 1090,360 1120,300"/>

  <!-- callouts -->
  <rect x="140" y="620" width="300" height="28" rx="6" fill="#0c4a6e"/>
  <text x="150" y="640" fill="#7dd3fc" font-size="13">Veg dryback ≈ 12 pts (74%→62%)</text>
  <rect x="460" y="620" width="340" height="28" rx="6" fill="#713f12"/>
  <text x="470" y="640" fill="#fcd34d" font-size="13">Generative dryback ≈ 24 pts (74%→50%)</text>
  <rect x="820" y="620" width="300" height="28" rx="6" fill="#4c1d95"/>
  <text x="830" y="640" fill="#ddd6fe" font-size="13">Finish: eased drybacks / lower push</text>

  <text x="48" y="700" fill="#475569" font-size="12">v3 · Complete axes (VWC % vs crop day) · phase bands · example point sizes match mainstream steering polarity</text>
</svg>
''')

print("v3 SVGs written")
