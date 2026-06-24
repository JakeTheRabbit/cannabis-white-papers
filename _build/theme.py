# -*- coding: utf-8 -*-
"""Variant B theme: charcoal monochrome chrome + serif headlines. Green reserved
for diagrams/data only. Emitted to assets/app.css by the build."""

CSS = r""":root{
  --paper:#FCFCFA; --surface:#FFFFFF; --surface-2:#F4F3EE; --surface-3:#EDECE6;
  --ink:#23231F; --ink-2:#43433D; --muted:#6A6A63; --faint:#9B9B93;
  --line:#E4E3DC; --line-2:#EFEEE8;
  --acc:#2B2B28; --acc-soft:#ECEBE5; --acc-ink:#2B2B28;
  /* data-viz greens (diagrams only) */
  --grn:#1C5B40; --grn-2:#2E7D52; --grn-soft:#EAF2EC; --grn-ink:#103A29;
  --amber:#946513; --amber-soft:#F6EFDC; --red:#A03A2B; --red-soft:#F5E6E2; --blue:#2C5E92; --blue-soft:#E8EFF6;
  --r:10px; --r-lg:16px;
  --sidebar:286px; --rail:226px; --maxw:760px;
  --sans:"Inter",system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --serif:"Iowan Old Style","Palatino Linotype",Georgia,"Times New Roman",serif;
  --mono:ui-monospace,"Cascadia Code","SF Mono",Consolas,monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink-2);font-family:var(--sans);font-size:16.5px;line-height:1.68;overflow-wrap:break-word}
html{overflow-x:hidden}
a{color:inherit;text-decoration:none}
::selection{background:var(--surface-3)}
img,svg{max-width:100%}

/* ---------------- layout ---------------- */
.layout{display:grid;grid-template-columns:var(--sidebar) minmax(0,1fr)}
.sidebar{position:sticky;top:0;height:100vh;border-right:1px solid var(--line);background:var(--surface);
  padding:24px 16px;display:flex;flex-direction:column;gap:3px;overflow-y:auto;z-index:30}
.content{min-width:0}
.doc{display:grid;grid-template-columns:minmax(0,1fr) var(--rail);gap:46px}
.col{padding:58px 56px 130px;max-width:var(--maxw);width:100%;margin:0 auto}
.wide .col{max-width:1080px}
.rail{position:sticky;top:0;height:100vh;padding:62px 22px 40px;overflow-y:auto}

/* ---------------- sidebar / nav ---------------- */
.brand{display:flex;align-items:center;gap:12px;padding:4px 8px 18px;margin-bottom:12px;border-bottom:1px solid var(--line-2)}
.brand .mark{width:34px;height:34px;border-radius:9px;background:var(--acc);color:#fff;display:grid;place-items:center;
  font-family:var(--serif);font-weight:600;font-size:18px;flex:0 0 34px}
.brand .nm{font-weight:600;font-size:14px;letter-spacing:-.01em;line-height:1.25;color:var(--ink)}
.brand .nm small{display:block;font-weight:400;font-size:10px;letter-spacing:.13em;color:var(--faint);margin-top:2px}
.cmdk{display:flex;align-items:center;gap:9px;padding:9px 12px;border:1px solid var(--line);border-radius:10px;
  background:var(--surface-2);color:var(--muted);font-size:13px;margin-bottom:8px;cursor:pointer;width:100%}
.cmdk .kbd{margin-left:auto;font-family:var(--mono);font-size:10.5px;color:var(--faint);border:1px solid var(--line);border-radius:5px;padding:1px 6px;background:var(--surface)}
.navgrp{font-size:10px;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);font-weight:600;padding:16px 10px 6px}
.nav a{display:flex;align-items:center;gap:11px;padding:8px 11px;border-radius:9px;font-size:13.5px;color:var(--ink-2);transition:background .12s,color .12s}
.nav a svg{width:17px;height:17px;color:var(--faint);flex:0 0 17px}
.nav a:hover{background:var(--surface-2)}
.nav a.on{background:var(--acc-soft);color:var(--ink);font-weight:500}
.nav a.on svg{color:var(--acc)}
.nav a.soon{color:var(--faint)}
.nav a .badge-soon{margin-left:auto;font-size:9px;letter-spacing:.04em;text-transform:uppercase;color:var(--faint);border:1px solid var(--line);border-radius:20px;padding:1px 7px}
.nav .seg{flex:1}

/* ---------------- breadcrumb / hero ---------------- */
.crumb{font-size:12.5px;color:var(--faint);margin-bottom:18px;display:flex;gap:7px;align-items:center}
.crumb a:hover{color:var(--muted)}
.crumb .sep{opacity:.5}
.eyebrow{font-size:11px;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);font-weight:600;margin-bottom:15px}
h1.title{font-family:var(--serif);font-size:46px;line-height:1.07;letter-spacing:-.018em;font-weight:600;color:var(--ink);margin-bottom:18px}
.sub{font-size:19px;line-height:1.55;color:var(--muted);max-width:640px;font-weight:400}
.metarow{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}
.pill{display:inline-flex;align-items:center;gap:7px;font-size:12.5px;color:var(--ink-2);border:1px solid var(--line);
  border-radius:7px;padding:5px 11px;background:var(--surface)}
.pill svg{width:14px;height:14px;color:var(--faint)}
.pill.solid{background:var(--acc-soft);border-color:transparent;color:var(--acc-ink);font-weight:500}
.pill.solid svg{color:var(--acc)}
.divider{height:1px;background:var(--line);margin:42px 0}

/* ---------------- prose ---------------- */
.col p{margin:0 0 18px;color:var(--ink-2);font-size:16.5px;line-height:1.72}
.col p strong{color:var(--ink);font-weight:600}
.lead{font-size:18.5px !important;color:var(--ink-2) !important;line-height:1.6 !important}
.sec{scroll-margin-top:20px}
.sec h2{font-family:var(--serif);font-size:30px;letter-spacing:-.01em;font-weight:600;color:var(--ink);margin:56px 0 16px}
.sec h3{font-size:19px;font-weight:600;color:var(--ink);margin:32px 0 10px}
.sec h4{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600;margin:22px 0 7px}
.sec-kicker{font-family:var(--mono);font-size:11.5px;letter-spacing:.13em;text-transform:uppercase;color:var(--faint);font-weight:600;margin:0 0 2px}
.col ul,.col ol{margin:0 0 18px;padding-left:1.3em}
.col li{margin-bottom:.45em;color:var(--ink-2)}
.col ul.tight li,.col ol.tight li{margin-bottom:.18em}
sup.cite{font-size:11px;font-weight:600;color:var(--acc);vertical-align:super;cursor:pointer}
a.xref{color:inherit;border-bottom:1px solid var(--line);text-decoration:none;transition:border-color .12s}
a.xref:hover{border-bottom-color:var(--ink)}
sup.cite a{color:var(--acc)}
code{font-family:var(--mono);font-size:.85em;background:var(--surface-2);border:1px solid var(--line);border-radius:5px;padding:1px 5px;color:var(--ink)}

/* ---------------- index / toc card ---------------- */
.toc-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:22px 26px;margin:6px 0 8px}
.kicker{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);font-weight:600;margin-bottom:16px;display:flex;align-items:center;gap:9px}
.kicker svg{width:14px;height:14px;color:var(--acc)}
.toc{display:grid;grid-template-columns:1fr 1fr;gap:0 32px}
.toc a{display:flex;gap:13px;align-items:baseline;padding:9px 0;font-size:14.5px;color:var(--ink-2);border-bottom:1px solid var(--line-2)}
.toc a:hover{color:var(--ink)}
.toc .n{font-family:var(--mono);font-size:11.5px;color:var(--muted);font-weight:600;min-width:18px}

/* ---------------- callouts ---------------- */
.callout{display:flex;gap:14px;padding:16px 19px;border-radius:var(--r);margin:24px 0;background:var(--surface);border:1px solid var(--line)}
.callout .cic{width:30px;height:30px;border-radius:8px;display:grid;place-items:center;flex:0 0 30px;color:#fff}
.callout .cic svg{width:17px;height:17px}
.callout .ctitle{font-weight:600;color:var(--ink);margin-bottom:2px}
.callout .cbody{font-size:14.8px;color:var(--ink-2);line-height:1.6}
.callout .cbody p:last-child{margin-bottom:0}
.callout.note{background:var(--blue-soft);border-color:#D6E2EF} .callout.note .cic{background:var(--blue)}
.callout.tip{background:var(--grn-soft);border-color:#D6E6DB} .callout.tip .cic{background:var(--grn)}
.callout.warn{background:var(--amber-soft);border-color:#ECDDB8} .callout.warn .cic{background:var(--amber)}
.callout.danger{background:var(--red-soft);border-color:#EAC9C0} .callout.danger .cic{background:var(--red)}
.callout.key{background:var(--surface-2);border-color:var(--line)} .callout.key .cic{background:var(--acc)}

/* ---------------- definition ---------------- */
.defn{padding:13px 18px;border-left:3px solid var(--acc);background:var(--surface-2);border-radius:0 8px 8px 0;margin:14px 0;font-size:15px}
.defn-t{font-family:var(--serif);font-weight:600;color:var(--ink);font-size:16px;margin-right:8px}
.defn-t::after{content:", ";margin-left:8px;color:var(--faint);font-family:var(--sans);font-weight:400}
.defn-b{color:var(--ink-2)}

/* ---------------- table ---------------- */
.tbl-wrap{overflow-x:auto;margin:24px 0;border:1px solid var(--line);border-radius:var(--r-lg)}
.tbl{width:100%;border-collapse:collapse;font-size:14.3px;background:var(--surface)}
.tbl caption{caption-side:top;text-align:left;font-weight:600;color:var(--ink-2);padding:14px 16px 0;font-size:13px}
.tbl th{text-align:left;font-weight:600;color:var(--faint);font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:12px 14px;border-bottom:1.5px solid var(--line);background:var(--surface-2)}
.tbl td{padding:11px 14px;border-top:1px solid var(--line-2);color:var(--ink-2);vertical-align:top}
.tbl tbody tr:hover td{background:var(--surface-2)}
.tbl tfoot td{font-size:12.5px;color:var(--muted);background:var(--surface-2);font-style:italic}
.tbl .num{font-family:var(--mono);white-space:nowrap}
.tag{font-size:11.5px;padding:3px 10px;border-radius:6px;font-weight:500;white-space:nowrap}
.tag.g{background:var(--grn-soft);color:var(--grn-ink)} .tag.w{background:var(--amber-soft);color:var(--amber)} .tag.r{background:var(--red-soft);color:var(--red)}

/* ---------------- figure ---------------- */
.fig{margin:30px 0;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:24px;text-align:center}
.fig svg{height:auto;display:block;margin:0 auto}
.fig figcaption{font-size:13px;color:var(--muted);margin-top:16px;text-align:left;line-height:1.55}
.fignum{font-weight:600;color:var(--ink)}
.fig.photo{padding:0;overflow:hidden}
.fig.photo img{display:block;width:100%;height:auto;border-radius:var(--r-lg) var(--r-lg) 0 0}
.fig.photo figcaption{margin:0;padding:14px 18px}
.fcredit{display:inline-block;margin-left:8px;font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--faint);border:1px solid var(--line);border-radius:20px;padding:1px 8px;vertical-align:middle}
/* image-sequence (progression) figure */
.figseq{padding:20px}
.pseq-t{font-size:14px;font-weight:600;color:var(--ink);margin-bottom:14px;text-align:left}
.pseq{display:flex;align-items:center;gap:6px;flex-wrap:wrap;justify-content:center}
.pseq-step{flex:1 1 150px;min-width:130px;max-width:240px;text-align:center}
.pseq-step img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:10px;border:1px solid var(--line)}
.pseq-lab{font-size:12px;color:var(--ink-2);margin-top:7px;font-weight:500}
.pseq-arr{color:var(--muted);font-size:18px;flex:0 0 auto}
@media(max-width:680px){.pseq-arr{transform:rotate(90deg)}.pseq-step{flex-basis:100%}}
/* key-terms image gallery */
.tgal-wrap{margin:22px 0}
.tgal{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.tgal-item{margin:0}
.tgal-item img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:10px;border:1px solid var(--line);display:block}
.tgal-item figcaption{font-size:12.5px;color:var(--ink-2);margin-top:6px;font-weight:500;line-height:1.3}

/* ---------------- stage cards ---------------- */
.stagecard{border:1px solid var(--line);border-radius:var(--r-lg);margin:18px 0;overflow:hidden;background:var(--surface)}
.stagecard-h{display:flex;align-items:center;gap:14px;padding:14px 18px;background:var(--surface-2);border-bottom:1px solid var(--line)}
.stagenum{flex:0 0 34px;height:34px;border-radius:9px;background:var(--acc);color:#fff;display:grid;place-items:center;font-weight:600;font-family:var(--mono)}
.stagetitle{font-weight:600;font-size:16.5px;flex:1;color:var(--ink)}
.stagedur{font-size:12px;color:var(--muted);background:var(--surface);border:1px solid var(--line);padding:3px 10px;border-radius:20px;white-space:nowrap}
.stagecard-b{padding:16px 18px}
.stagecard-b p:last-child{margin-bottom:0}

/* ---------------- grid / cards / chips / kv / steps ---------------- */
.grid{display:grid;gap:15px;margin:20px 0}
.grid-2{grid-template-columns:1fr 1fr} .grid-3{grid-template-columns:1fr 1fr 1fr}
.card{border:1px solid var(--line);border-radius:var(--r-lg);padding:16px 18px;background:var(--surface)}
.card-tag{font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.card-title{font-weight:600;margin:4px 0 6px;font-size:16px;color:var(--ink)}
.card-body{font-size:14.5px;color:var(--ink-2)} .card-body p:last-child{margin-bottom:0} .card-body ul{margin-bottom:0}
.chip{display:inline-block;font-size:12px;padding:3px 11px;border-radius:20px;background:var(--surface-2);border:1px solid var(--line);color:var(--ink-2)}
.kv{border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;margin:18px 0;background:var(--surface)}
.kv-row{display:flex;border-top:1px solid var(--line-2)} .kv-row:first-child{border-top:none}
.kv-k{flex:0 0 42%;padding:10px 14px;background:var(--surface-2);font-weight:600;font-size:14px;color:var(--ink)}
.kv-v{flex:1;padding:10px 14px;font-size:14px}
.steps{list-style:none;margin:18px 0;padding:0}
.step{display:flex;gap:14px;padding:12px 0;border-top:1px dashed var(--line)} .step:first-child{border-top:none}
.step-n{flex:0 0 28px;height:28px;border-radius:50%;background:var(--acc);color:#fff;display:grid;place-items:center;font-weight:600;font-size:13.5px;font-family:var(--mono)}
.step-t{font-weight:600;margin-bottom:2px;color:var(--ink)} .step-b{font-size:14.5px;color:var(--ink-2)} .step-b p:last-child{margin-bottom:0}

/* ---------------- related ---------------- */
.rel{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:16px}
.relcard{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:16px;transition:border-color .15s,transform .15s,box-shadow .15s}
.relcard:hover{border-color:#CFCEC6;transform:translateY(-2px);box-shadow:0 12px 30px -18px rgba(20,20,15,.3)}
.relcard svg{width:20px;height:20px;color:var(--acc);margin-bottom:10px}
.relcard .tt{font-size:14px;font-weight:600;color:var(--ink);margin-bottom:2px}
.relcard .dd{font-size:12px;color:var(--muted)}

/* ---------------- rail (on this page) ---------------- */
.rail .lbl{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);font-weight:600;margin-bottom:14px}
.rail a{display:block;font-size:13px;color:var(--muted);padding:6px 0 6px 14px;border-left:2px solid var(--line);line-height:1.4}
.rail a:hover{color:var(--ink-2)}
.rail a.on{color:var(--ink);border-left-color:var(--acc);font-weight:500}

/* ---------------- footer / refs ---------------- */
.refs{margin-top:60px;padding-top:26px;border-top:1px solid var(--line)}
.refs h3{font-family:var(--serif);font-size:20px;font-weight:600;color:var(--ink);margin-bottom:14px}
.refs ol{padding-left:1.4em;font-size:13px;color:var(--muted);line-height:1.65}
.refs li{margin-bottom:8px} .refs li.np{opacity:.85}
.refs a{color:var(--acc);text-decoration:underline;text-underline-offset:2px}
.foot{font-size:12.5px;color:var(--faint);margin-top:24px;line-height:1.6}

/* ---------------- landing ---------------- */
.hero-land{padding:74px 0 36px;text-align:center;max-width:760px;margin:0 auto}
.hero-land .eyebrow{margin-bottom:18px}
.hero-land h1{font-family:var(--serif);font-size:54px;line-height:1.05;letter-spacing:-.02em;font-weight:600;color:var(--ink);margin-bottom:20px}
.hero-land .sub{font-size:20px;color:var(--muted);margin:0 auto;max-width:600px}
.hero-stats{display:flex;justify-content:center;gap:34px;margin:34px 0 8px;flex-wrap:wrap}
.hero-stats .s{text-align:center}
.hero-stats .s b{display:block;font-family:var(--serif);font-size:30px;color:var(--ink);font-weight:600}
.hero-stats .s span{font-size:12.5px;color:var(--muted)}
.track{margin:46px 0 0}
.track-h{display:flex;align-items:baseline;gap:12px;margin-bottom:16px}
.track-h h2{font-family:var(--serif);font-size:24px;font-weight:600;color:var(--ink)}
.track-h .ct{font-size:12.5px;color:var(--faint)}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.pgrid.compact{grid-template-columns:repeat(auto-fill,minmax(232px,1fr));gap:10px}
.pcard.sm{padding:12px 14px;gap:11px}
.pcard.sm .pic{width:32px;height:32px;flex:0 0 32px} .pcard.sm .pic svg{width:17px;height:17px}
.pcard.sm .pt{font-size:13.5px;margin-bottom:1px} .pcard.sm .ps{font-size:12px;line-height:1.4}
.filterbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;position:sticky;top:0;z-index:20;
  background:var(--paper);padding:14px 0;margin:8px 0 18px;border-bottom:1px solid var(--line)}
.fpill{font-size:13px;border:1px solid var(--line);border-radius:30px;padding:6px 13px;background:var(--surface);
  color:var(--ink-2);cursor:pointer;display:inline-flex;gap:7px;align-items:center;font-family:var(--sans)}
.fpill:hover{border-color:var(--line-2);color:var(--ink)}
.fpill span{color:var(--faint);font-size:11px;font-family:var(--mono)}
.fpill.on{background:var(--acc);color:var(--paper);border-color:transparent}
.fpill.on span{color:var(--paper);opacity:.7}
.dir-empty{color:var(--muted);font-size:14px;padding:20px 0}
/* ---------------- landing tree index ---------------- */
.hero-land.tight{padding:52px 0 18px;text-align:left;max-width:none;margin:0}
.hero-land.tight h1{font-size:46px;margin-bottom:16px}
.hero-land.tight .sub{margin:0;max-width:780px;font-size:18.5px}
.dirtools{position:sticky;top:0;z-index:20;background:var(--paper);padding:14px 0 10px;margin-bottom:4px;border-bottom:1px solid var(--line)}
.dirtools .filterbar{position:static;border:none;padding:0;margin:0}
.treefilter{display:block;width:100%;max-width:780px;padding:11px 14px;border:1px solid var(--line);border-radius:10px;background:var(--surface);color:var(--ink);font-family:var(--sans);font-size:15px;outline:none;margin-bottom:12px}
.treefilter:focus{border-color:var(--muted)}
.treefilter::placeholder{color:var(--faint)}
.treegroup{margin:24px 0 0}
.tg-h{display:flex;align-items:baseline;gap:10px;margin:0;padding-bottom:7px;border-bottom:1px solid var(--line)}
.tg-h h2{font-family:var(--serif);font-size:21px;font-weight:600;color:var(--ink);margin:0}
.tg-ct{font-family:var(--mono);font-size:12px;color:var(--faint)}
.tg-rows{display:flex;flex-direction:column}
.trow{display:flex;align-items:flex-start;gap:14px;padding:12px 10px;border-bottom:1px solid var(--line-2);border-radius:8px;transition:background .12s;color:inherit}
.trow:last-child{border-bottom:none}
a.trow:hover{background:var(--surface-2)}
.trow-ic{flex:0 0 32px;height:32px;border-radius:9px;background:var(--surface-2);display:grid;place-items:center;color:var(--acc);margin-top:1px}
.trow-ic svg{width:17px;height:17px}
.trow-main{flex:1;min-width:0}
.trow-t{display:block;font-weight:600;color:var(--ink);font-size:15.5px;line-height:1.3}
.trow-b{display:block;color:var(--muted);font-size:13.8px;line-height:1.5;margin-top:3px}
.trow-meta{flex:0 0 auto;font-family:var(--mono);font-size:11px;color:var(--faint);white-space:nowrap;padding-top:4px}
.trow-meta.soon{text-transform:uppercase;letter-spacing:.05em}
.trow.soon{opacity:.5;cursor:default}
@media(max-width:900px){.dirtools{position:static}.hero-land.tight h1{font-size:33px}.trow-meta{display:none}}
.pcard{display:flex;gap:13px;padding:17px;border:1px solid var(--line);border-radius:var(--r-lg);background:var(--surface);transition:border-color .15s,transform .15s,box-shadow .15s;position:relative}
.pcard:hover{border-color:#CFCEC6;transform:translateY(-2px);box-shadow:0 14px 32px -20px rgba(20,20,15,.34)}
.pcard.soon{opacity:.72}
.pcard .pic{width:38px;height:38px;border-radius:10px;background:var(--surface-2);display:grid;place-items:center;flex:0 0 38px}
.pcard .pic svg{width:20px;height:20px;color:var(--acc)}
.pcard .pt{font-size:15px;font-weight:600;color:var(--ink);margin-bottom:2px;line-height:1.25}
.pcard .ps{font-size:12.8px;color:var(--muted);line-height:1.45}
.pcard .soon-tag{position:absolute;top:12px;right:12px;font-size:9px;letter-spacing:.05em;text-transform:uppercase;color:var(--faint);border:1px solid var(--line);border-radius:20px;padding:1px 7px}

/* ---------------- glossary ---------------- */
.gl-letter{font-family:var(--serif);font-size:26px;color:var(--ink);font-weight:600;margin:34px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}
.gl-item{padding:14px 0;border-bottom:1px solid var(--line-2)}
.gl-term{font-weight:600;color:var(--ink);font-size:16px}
.gl-defn{font-size:14.8px;color:var(--ink-2);margin-top:3px;line-height:1.6}
.gl-tags{margin-top:6px;display:flex;gap:6px;flex-wrap:wrap}

/* ---------------- mobile chrome ---------------- */
.mtopbar{display:none;align-items:center;gap:13px;padding:13px 18px;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(252,252,250,.88);backdrop-filter:blur(12px);z-index:40}
.mtopbar .mb{width:30px;height:30px;border-radius:8px;background:var(--acc);color:#fff;display:grid;place-items:center;font-family:var(--serif);font-weight:600;font-size:16px}
.mtopbar .mt{font-weight:600;font-size:14px;flex:1;color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.iconbtn{background:none;border:none;color:var(--muted);cursor:pointer;display:grid;place-items:center;padding:4px}
.iconbtn svg{width:21px;height:21px}
.bottomnav{display:none}
.drawer-mask{display:none}

@media(max-width:1180px){ .doc{grid-template-columns:minmax(0,1fr)} .rail{display:none} }
@media(max-width:900px){
  .layout{grid-template-columns:minmax(0,1fr)}
  .sidebar{position:fixed;left:0;top:0;width:300px;transform:translateX(-100%);transition:transform .25s ease;box-shadow:0 0 60px rgba(0,0,0,.18)}
  .sidebar.open{transform:translateX(0)}
  .drawer-mask{position:fixed;inset:0;background:rgba(20,20,15,.4);z-index:29;border:none}
  .drawer-mask.show{display:block}
  .mtopbar{display:flex}
  .col{padding:30px 20px 120px}
  h1.title{font-size:33px} .hero-land h1{font-size:36px} .sec h2{font-size:25px}
  .toc{grid-template-columns:1fr} .rel{grid-template-columns:1fr} .grid-2,.grid-3{grid-template-columns:1fr}
  .bottomnav{display:flex;position:fixed;left:0;right:0;bottom:0;background:rgba(255,255,255,.92);
    backdrop-filter:blur(16px);border-top:1px solid var(--line);padding:6px 4px;z-index:45;
    padding-bottom:calc(6px + env(safe-area-inset-bottom))}
  .bottomnav a{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10px;color:var(--faint);padding:7px 0;position:relative}
  .bottomnav a svg{width:21px;height:21px}
  .bottomnav a.on{color:var(--acc)}
  .bottomnav a.on::before{content:"";position:absolute;top:0;width:24px;height:2px;border-radius:2px;background:var(--acc)}
}

/* ---------------- search modal ---------------- */
.search-mask{display:none;position:fixed;inset:0;background:rgba(20,20,15,.34);z-index:60;align-items:flex-start;justify-content:center;padding-top:12vh}
.search-mask.show{display:flex}
.search-box{width:min(560px,92vw);background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden;box-shadow:0 30px 80px -30px rgba(0,0,0,.5)}
.search-box input{width:100%;border:none;border-bottom:1px solid var(--line);padding:16px 18px;font-size:16px;font-family:var(--sans);color:var(--ink);outline:none;background:var(--surface)}
.search-results{max-height:54vh;overflow-y:auto}
.sr-item{display:block;padding:11px 18px;border-bottom:1px solid var(--line-2);cursor:pointer}
.sr-item:hover,.sr-item.sel{background:var(--surface-2)}
.sr-t{font-size:14px;font-weight:600;color:var(--ink)}
.sr-k{font-size:11px;color:var(--faint);text-transform:uppercase;letter-spacing:.05em}
.sr-d{font-size:12.5px;color:var(--muted);margin-top:2px}
.sr-empty{padding:22px 18px;color:var(--muted);font-size:14px;text-align:center}
.sr-d mark{background:var(--acc-soft);color:var(--ink);border-radius:3px;padding:0 2px}

/* ---------------- curriculum / learning tree ---------------- */
.curtier{margin:30px 0 0}
.curtier-h{display:flex;align-items:baseline;gap:12px;margin:0 0 4px}
.curtier-h h3{font-family:var(--serif);font-size:21px;font-weight:600;color:var(--ink);margin:0}
.curtier-h .d{font-size:12.5px;color:var(--faint)}
.curlist{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}
@media(max-width:680px){.curlist{grid-template-columns:1fr}}
.curitem{display:flex;align-items:center;gap:11px;padding:10px 13px;border:1px solid var(--line);border-radius:10px;background:var(--surface);font-size:14px;color:var(--ink-2)}
a.curitem:hover{border-color:#CFCEC6;color:var(--ink)}
.curitem .dot{width:7px;height:7px;border-radius:50%;background:var(--acc);flex:0 0 7px}
.curitem.soon{opacity:.62} .curitem.soon .dot{background:var(--line)}
.curitem .soon-tag{margin-left:auto;font-size:9px;letter-spacing:.05em;text-transform:uppercase;color:var(--faint);border:1px solid var(--line);border-radius:20px;padding:1px 7px}
.curitem .arr{margin-left:auto;color:var(--faint)}

/* ---------------- figure palette (themable) ---------------- */
:root{
  --fig-bg:#ffffff; --fig-panel:#f3f7f3; --fig-ink:#16211c; --fig-ink2:#3c4a42; --fig-mut:#697a70; --fig-line:#cdd8d0;
  --fig-green:#2e7d52; --fig-green-d:#1d5638; --fig-green-l:#e7f2eb; --fig-green-xl:#f1f8f3;
  --fig-amber:#b3791a; --fig-amber-l:#fdf3e0; --fig-red:#b5402f; --fig-red-l:#fbe9e6;
  --fig-blue:#2f6fb0; --fig-blue-l:#e9f1f9; --fig-purple:#6b4f9e; --fig-purple-l:#efeaf7;
}

/* ---------------- theme toggle ---------------- */
.brandrow{display:flex;align-items:center;gap:8px;margin-bottom:12px;border-bottom:1px solid var(--line-2);padding-bottom:14px}
.brandrow .brand{flex:1;border-bottom:none;margin-bottom:0;padding-bottom:0}
.themebtn{background:none;border:1px solid var(--line);border-radius:8px;color:var(--muted);cursor:pointer;width:32px;height:32px;display:grid;place-items:center;flex:0 0 32px}
.themebtn:hover{background:var(--surface-2);color:var(--ink)}
.themebtn svg{width:17px;height:17px}

/* ---------------- dark mode ---------------- */
[data-theme="dark"]{
  --paper:#151515; --surface:#1F1F1F; --surface-2:#272727; --surface-3:#313131;
  --ink:#E7E7E7; --ink-2:#C8C8C8; --muted:#9A9A9A; --faint:#717171;
  --line:#2F2F2F; --line-2:#262626;
  --acc:#E7E7E7; --acc-soft:#262626; --acc-ink:#E7E7E7;
  --grn:#46b88a; --grn-d:#8fe0b6; --grn-l:#1c3a2b; --grn-xl:#16271e; --grn-ink:#9fe6c0;
  --amber:#d9a85a; --amber-l:#2a2113; --red:#e08a7d; --red-l:#2c1714;
  --blue:#6aa6e0; --blue-l:#14202e; --purple:#b09ce0; --purple-l:#221c30;
  --grn-soft:#14231b; --amber-soft:#241e12; --red-soft:#291814; --blue-soft:#152030;
  /* Diagrams stay on a LIGHT card in dark mode: keep the light --fig-* values
     from :root (do NOT override). Light strokes on a dark page bloom/halate and
     our SVGs mix themed vars with light-tuned colours, so a consistent light
     diagram card is the safe, no-inversion choice. */
}
[data-theme="dark"] body{background:var(--paper);color:var(--ink-2)}
[data-theme="dark"] .brand .mark,[data-theme="dark"] .stagenum,[data-theme="dark"] .step-n{color:var(--paper)}
[data-theme="dark"] .callout .cic{color:var(--paper)}
[data-theme="dark"] .callout.note{border-color:#1d3346}
[data-theme="dark"] .callout.tip{border-color:#1d3a2a}
[data-theme="dark"] .callout.warn{border-color:#3a3115}
[data-theme="dark"] .callout.danger{border-color:#3d2019}
[data-theme="dark"] .mtopbar{background:rgba(14,15,13,.86)}
[data-theme="dark"] .bottomnav{background:rgba(20,22,18,.92)}
[data-theme="dark"] .tag.g{color:#86d6ad}
[data-theme="dark"] .tag.w{color:#e6c07a}
[data-theme="dark"] .tag.r{color:#ec9b8f}
[data-theme="dark"] .pill.solid{color:var(--acc-ink)}
[data-theme="dark"] .fig svg{border-radius:10px}
"""
