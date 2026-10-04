# -*- coding: utf-8 -*-
"""Build a single-file HTML review page: original text vs STE text for every rewritten unit.

  ste_review_build.py [--out FILE] [--only substr]

Reads  work/<module>/units.original.txt  and  work/<module>/units.txt  (+ REPORT.md when present).
Open the output in any browser (no network needed).  Left column = paper list, right = table of
before / after with a filter, a 'changed only' switch and per-paper statistics.
"""
import argparse
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ste_common import read_units, html_to_text  # noqa: E402

PLACE = re.compile(r"⟦c:([^⟧]+)⟧")


def show(s):
    s = PLACE.sub(lambda m: "[cite]", s)
    s = re.sub(r"⟦[^⟧]*⟧", "[code]", s)
    s = html_to_text(s) if "<" in s or "&" in s else s
    return s


def collect(only=None):
    work = os.path.join(HERE, "work")
    papers = []
    for d in sorted(os.listdir(work)):
        p = os.path.join(work, d)
        if not (d.startswith("paper_") and os.path.isdir(p)):
            continue
        if only and only not in d:
            continue
        a, b = os.path.join(p, "units.original.txt"), os.path.join(p, "units.txt")
        if not (os.path.exists(a) and os.path.exists(b)):
            continue
        _, ou = read_units(a)
        _, nu = read_units(b)
        new = {u.id: u for u in nu}
        rows, changed, wb, wa = [], 0, 0, 0
        for u in ou:
            n = new.get(u.id)
            if not n:
                continue
            bt, at = show(u.text), show(n.text)
            ch = u.text != n.text
            changed += ch
            wb += len(bt.split())
            wa += len(at.split())
            rows.append([u.id, u.kind, u.ctx, bt, at, 1 if ch else 0])
        rep = ""
        rp = os.path.join(p, "REPORT.md")
        if os.path.exists(rp):
            rep = open(rp, encoding="utf-8").read()[:6000]
        papers.append({"module": d, "n": len(rows), "changed": changed, "wb": wb, "wa": wa, "rows": rows, "report": rep})
    return papers


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>STE rewrite review</title>
<style>
:root{--bg:#fafaf8;--fg:#1d1d1b;--mut:#6b6b66;--line:#dcdcd6;--chg:#eef7ee;--side:#f1f1ed;--acc:#2f6f3f}
@media (prefers-color-scheme:dark){:root{--bg:#161614;--fg:#e8e8e3;--mut:#9a9a92;--line:#33332f;--chg:#1b2a1d;--side:#1d1d1a;--acc:#6fbf80}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,Segoe UI,sans-serif;display:flex;height:100vh}
#side{width:290px;min-width:290px;background:var(--side);border-right:1px solid var(--line);overflow:auto;padding:12px}
#side h1{font-size:15px;margin:0 0 8px}#side input{width:100%;padding:6px 8px;margin:4px 0 10px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
#side a{display:block;padding:5px 7px;border-radius:6px;color:var(--fg);text-decoration:none;font-size:13px;cursor:pointer}
#side a:hover,#side a.on{background:var(--chg)}#side small{color:var(--mut);float:right}
#main{flex:1;overflow:auto;padding:16px 20px}
h2{margin:0 0 4px;font-size:20px}.stats{color:var(--mut);margin-bottom:10px}
table{border-collapse:collapse;width:100%;table-layout:fixed}th,td{border-top:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left;word-wrap:break-word}
th{position:sticky;top:0;background:var(--bg);z-index:1}td.k{width:120px;color:var(--mut);font-size:12px}tr.c td.a{background:var(--chg)}
.bar{display:flex;gap:14px;align-items:center;margin:8px 0 12px;flex-wrap:wrap}.bar input[type=text]{padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg);min-width:240px}
details{margin:10px 0}pre{white-space:pre-wrap;background:var(--side);padding:10px;border-radius:6px;font-size:12.5px}
</style></head><body>
<div id="side"><h1>STE rewrite review</h1><div style="color:var(--mut);font-size:12px">ASD-STE100 Issue 9. Original vs rewritten text, per paper.</div>
<input id="pf" placeholder="Filter papers"><div id="plist"></div></div>
<div id="main"><div id="view"></div></div>
<script>
const DATA=__DATA__;
const plist=document.getElementById('plist'),view=document.getElementById('view'),pf=document.getElementById('pf');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
function renderList(){const q=pf.value.toLowerCase();plist.innerHTML='';
 DATA.forEach((p,i)=>{if(q&&!p.module.toLowerCase().includes(q))return;const a=document.createElement('a');
  a.innerHTML=esc(p.module.replace('paper_',''))+'<small>'+p.changed+'/'+p.n+'</small>';a.onclick=()=>show(i);a.dataset.i=i;plist.appendChild(a)})}
function show(i){const p=DATA[i];[...plist.children].forEach(a=>a.classList.toggle('on',a.dataset.i==i));
 view.innerHTML='<h2>'+esc(p.module)+'</h2><div class="stats">'+p.changed+' of '+p.n+' units changed &middot; words '+p.wb+' &rarr; '+p.wa+'</div>'+
 (p.report?'<details><summary>Agent report</summary><pre>'+esc(p.report)+'</pre></details>':'')+
 '<div class="bar"><input type="text" id="qf" placeholder="Search text"><label><input type="checkbox" id="co" checked> changed only</label></div><table><thead><tr><th style="width:120px">Unit</th><th>Before</th><th>After (STE)</th></tr></thead><tbody id="tb"></tbody></table>';
 const draw=()=>{const q=document.getElementById('qf').value.toLowerCase(),co=document.getElementById('co').checked;let h='';
  p.rows.forEach(r=>{if(co&&!r[5])return;if(q&&!(r[3]+' '+r[4]).toLowerCase().includes(q))return;
   h+='<tr class="'+(r[5]?'c':'')+'"><td class="k">'+r[0]+'<br>'+esc(r[1])+'<br>'+esc(r[2])+'</td><td>'+esc(r[3])+'</td><td class="a">'+esc(r[4])+'</td></tr>'});
  document.getElementById('tb').innerHTML=h};
 document.getElementById('qf').oninput=draw;document.getElementById('co').onchange=draw;draw();}
pf.oninput=renderList;renderList();if(DATA.length)show(0);
</script></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "work", "ste-review.html"))
    ap.add_argument("--only")
    a = ap.parse_args()
    papers = collect(a.only)
    data = json.dumps(papers, ensure_ascii=False).replace("</", "<\\/")
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(PAGE.replace("__DATA__", data))
    print("wrote", a.out, len(papers), "papers,", os.path.getsize(a.out) // 1024, "KB")


if __name__ == "__main__":
    main()
