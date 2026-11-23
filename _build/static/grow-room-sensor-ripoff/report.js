// Verbatim calculator + brand filter from the standalone report.
// 1. Live FAO-56 Tetens Psychrometric Drift Calculator
function es(T) { return 0.61078 * Math.exp((17.27 * T) / (T + 237.3)); }
function dew(T, rh) {
  const ea = Math.max(0.01, es(T) * (rh / 100));
  const ln = Math.log(ea / 0.61078);
  return (237.3 * ln) / (17.27 - ln);
}
function toF(c) { return (c * 9/5 + 32).toFixed(1); }
function setPreset(t, dt, rh, err) {
  document.getElementById('in-t').value = t;
  document.getElementById('in-dt').value = dt;
  document.getElementById('in-rh').value = rh;
  document.getElementById('in-err').value = err;
  updateCalc();
}
function updateCalc() {
  const T = parseFloat(document.getElementById('in-t').value);
  const dT = parseFloat(document.getElementById('in-dt').value);
  const setRH = parseFloat(document.getElementById('in-rh').value);
  const err = parseFloat(document.getElementById('in-err').value);
  const Tleaf = T - dT;
  const trueRH = Math.max(10, Math.min(99, setRH - err));
  const targetVPD = Math.max(0.01, es(Tleaf) - es(T) * (setRH / 100));
  const trueVPD = Math.max(0.01, es(Tleaf) - es(T) * (trueRH / 100));
  const pct = ((trueVPD / targetVPD) - 1) * 100;
  const td = dew(T, trueRH);

  document.getElementById('lbl-t').textContent = `${T.toFixed(1)} °C [${toF(T)} °F]`;
  document.getElementById('lbl-dt').textContent = dT === 0 ? '0.0 °C (Air / Dry Room)' : `−${dT.toFixed(1)} °C [−${(dT*1.8).toFixed(1)} °F]`;
  document.getElementById('lbl-rh').textContent = `${setRH}% RH`;
  const errEl = document.getElementById('lbl-err');
  errEl.textContent = (err > 0 ? `+${err.toFixed(1)}% RH (Reads Wet)` : err < 0 ? `${err.toFixed(1)}% RH (Reads Dry)` : '0.0% RH (Honest)');
  errEl.style.color = Math.abs(err) <= 2 ? '#22c55e' : Math.abs(err) <= 4 ? '#f59e0b' : '#ef4444';

  document.getElementById('out-trh').textContent = `${trueRH.toFixed(1)}%`;
  document.getElementById('out-aw').innerHTML = `Eq. Water Activity: <strong>${(trueRH/100).toFixed(2)} a<sub>w</sub></strong>`;
  document.getElementById('out-vpd').textContent = `${trueVPD.toFixed(2)} kPa`;
  document.getElementById('out-vpdpct').textContent = `Target ${targetVPD.toFixed(2)} kPa (${pct >= 0 ? '+' : ''}${pct.toFixed(1)}%)`;
  document.getElementById('out-td').textContent = `${td.toFixed(1)} °C`;
  document.getElementById('out-tdf').textContent = `${toF(td)} °F`;

  const v = document.getElementById('out-verdict');
  if (Math.abs(err) <= 2) {
    v.style.background = 'rgba(34,197,94,0.14)'; v.style.border = '1px solid rgba(34,197,94,0.45)'; v.style.color = '#4ade80';
    v.textContent = '✓ PASS ZONE: Within ±2% RH combined benchmark uncertainty. Keep logging on schedule.';
  } else if (T <= 19) {
    if (trueRH < 55) {
      v.style.background = 'rgba(249,115,22,0.16)'; v.style.border = '1px solid rgba(249,115,22,0.5)'; v.style.color = '#fb923c';
      v.textContent = `⚠ DRY ROOM OVER-DRYING (${(trueRH/100).toFixed(2)} a_w): Below the 0.55 ASTM floor! Stripping monoterpenes, brittle trichomes, and burning 2–5% of sellable weight.`;
    } else if (trueRH >= 65) {
      v.style.background = 'rgba(239,68,68,0.18)'; v.style.border = '1px solid rgba(239,68,68,0.55)'; v.style.color = '#f87171';
      v.textContent = `🚨 DRY ROOM MOULD DANGER (${(trueRH/100).toFixed(2)} a_w): At or past the 0.65 ASTM mould cliff! High probability of Aspergillus/Botrytis and failed compliance testing.`;
    } else {
      v.style.background = 'rgba(245,158,11,0.16)'; v.style.border = '1px solid rgba(245,158,11,0.5)'; v.style.color = '#fbbf24';
      v.textContent = `⚠ DRY ROOM FLAG: Sensor is off by ${Math.abs(err).toFixed(1)}%. Replace immediately if >2–3% RH in dry/cure rooms.`;
    }
  } else {
    if (err > 0) {
      v.style.background = 'rgba(239,68,68,0.16)'; v.style.border = '1px solid rgba(239,68,68,0.5)'; v.style.color = '#fca5a5';
      v.textContent = `🔥 OVER-DEHUMIDIFYING: Controller sees fake wet air and pulls room to ${trueRH.toFixed(1)}% RH — spiking Leaf VPD by +${pct.toFixed(1)}%, burning kWh and driving EC/stomatal stress.`;
    } else {
      v.style.background = 'rgba(59,130,246,0.16)'; v.style.border = '1px solid rgba(59,130,246,0.5)'; v.style.color = '#93c5fd';
      v.textContent = `🦠 HIDDEN HUMIDITY / MOULD RISK: Sensor reads dry so controller lets room climb to ${trueRH.toFixed(1)}% RH — slashing Leaf VPD by ${pct.toFixed(1)}% and inviting Botrytis/PM at lights-off.`;
    }
  }
}
updateCalc();

// 2. Searchable & Filterable 25-Brand Wall of Shame
let currentTier = 'all';
function setTier(t, btn) {
  currentTier = t;
  document.querySelectorAll('.tier-pills .tier-pill').forEach(p => p.classList.remove('active'));
  btn.classList.add('active');
  filterBrands();
}
function filterBrands() {
  const q = (document.getElementById('brand-search').value || '').toLowerCase().trim();
  const rows = document.querySelectorAll('#brand-table tbody tr');
  rows.forEach(tr => {
    const txt = tr.textContent.toLowerCase();
    const r = tr.getAttribute('data-risk') || 'high';
    const tierOk = (currentTier === 'all') || (currentTier === r);
    const qOk = !q || txt.includes(q);
    tr.style.display = (tierOk && qOk) ? '' : 'none';
  });
}
