# -*- coding: utf-8 -*-
"""Client JS: powerful offline search (ranked keyword + synonym/concept expansion +
prefix + fuzzy + section snippets), mobile drawer, theme toggle, scrollspy."""

JS = r"""(function(){
 var $=function(s,e){return (e||document).querySelector(s);};
 var $$=function(s,e){return Array.prototype.slice.call((e||document).querySelectorAll(s));};
 var MOON='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A8 8 0 1 1 11.2 3a6 6 0 0 0 9.8 9.8z"/></svg>';
 var SUN='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.4 1.4M17.6 17.6L19 19M19 5l-1.4 1.4M6.4 17.6L5 19"/></svg>';
 function curTheme(){return document.documentElement.getAttribute('data-theme')||'light';}
 function paintThemeIcons(t){ $$('[data-action=theme]').forEach(function(b){ b.innerHTML=(t==='dark'?SUN:MOON); }); }
 function setTheme(t){ document.documentElement.setAttribute('data-theme',t); try{localStorage.setItem('cwp-theme',t);}catch(e){} paintThemeIcons(t); }
 paintThemeIcons(curTheme());

 var sb=$('#sidebar'), mask=$('#mask');
 function openMenu(){ if(sb)sb.classList.add('open'); if(mask)mask.classList.add('show'); }
 function closeMenu(){ if(sb)sb.classList.remove('open'); if(mask)mask.classList.remove('show'); }
 if(mask) mask.addEventListener('click',closeMenu);

 /* ---------------- search engine ---------------- */
 var IDX=window.SEARCH_INDEX||[], SYN=window.SEARCH_SYN||{};
 var sm=$('#searchMask'), si=$('#searchInput'), sr=$('#searchResults');
 var sel=-1, cur=[];
 function esc(s){return (s||'').replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
 function rxesc(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
 function toks(q){ var m=(q||'').toLowerCase().match(/[a-z0-9]+/g)||[]; return m.filter(function(t){return t.length>=2;}); }
 function expand(ts){
   var out=[], seen={};
   ts.forEach(function(t){ if(!seen[t]){seen[t]=1; out.push({t:t,w:1,p:true});}
     (SYN[t]||[]).forEach(function(x){ x=x.toLowerCase();
       x.match(/[a-z0-9]+/g).forEach(function(w){ if(w.length>=2&&!seen[w]){seen[w]=1; out.push({t:w,w:0.5,p:false});} });
     });
   });
   return out;
 }
 function lev1(a,b){ if(a===b)return true; var la=a.length,lb=b.length; if(Math.abs(la-lb)>1)return false;
   var i=0,j=0,d=0; while(i<la&&j<lb){ if(a[i]===b[j]){i++;j++;} else { d++; if(d>1)return false;
     if(la>lb)i++; else if(lb>la)j++; else {i++;j++;} } } return (d + (la-i) + (lb-j))<=1; }
 function score(x, terms, fuzzy){
   var title=(x.title||'').toLowerCase(), kw=((x.kw||'')+' '+(x.paper||'')).toLowerCase(),
       body=(x.text||'').toLowerCase(), sc=0, prim=0, primNeed=0;
   terms.forEach(function(o){ if(o.p)primNeed++;
     var hit=0, t=o.t, wb=new RegExp('\\b'+rxesc(t));
     if(title===t) hit=120;
     else if(wb.test(title)) hit=70;
     else if(title.indexOf(t)>=0) hit=42;
     if(kw.indexOf(t)>=0) hit=Math.max(hit,40);
     if(body.indexOf(t)>=0){ var c=body.split(t).length-1; hit=Math.max(hit,14+Math.min(c*3,12)); }
     if(!hit && fuzzy && t.length>=4){
       var pool=(title+' '+kw).split(/[^a-z0-9]+/);
       for(var k=0;k<pool.length;k++){ if(pool[k].length>=4 && lev1(pool[k],t)){ hit=34; break; } }
     }
     if(hit>0){ sc+=hit*o.w; if(o.p)prim++; }
   });
   if(prim===0) return 0;
   if(prim>=primNeed && primNeed>1) sc*=1.3;          /* all query words hit */
   if(x.type==='paper') sc*=1.18; else if(x.type==='term') sc*=1.06;
   return sc;
 }
 function snippet(x, terms){
   var body=x.text||''; if(!body) return '';
   var low=body.toLowerCase(), at=-1;
   for(var i=0;i<terms.length;i++){ var p=low.indexOf(terms[i].t); if(p>=0&&(at<0||p<at)) at=p; }
   var start=at<0?0:Math.max(0,at-60), seg=body.slice(start, start+150);
   if(start>0) seg='…'+seg; if(start+150<body.length) seg=seg+'…';
   var out=esc(seg);
   var pats=terms.map(function(o){return rxesc(o.t);}).filter(Boolean);
   if(pats.length){ out=out.replace(new RegExp('('+pats.join('|')+')','ig'), '<mark>$1</mark>'); }
   return out;
 }
 function search(q){
   var ts=toks(q);
   if(!ts.length) return IDX.filter(function(x){return x.type==='paper';}).slice(0,8)
       .map(function(x){return {x:x,snip:esc((x.text||'').slice(0,120))};});
   var terms=expand(ts);
   function run(fuzzy){
     var r=[];
     for(var i=0;i<IDX.length;i++){ var s=score(IDX[i],terms,fuzzy); if(s>0) r.push({x:IDX[i],s:s}); }
     r.sort(function(a,b){return b.s-a.s;});
     return r;
   }
   var res=run(false);
   if(res.length<4) res=run(true);
   return res.slice(0,16).map(function(o){return {x:o.x,snip:snippet(o.x,terms)};});
 }
 function openSearch(){ if(!sm)return; sm.classList.add('show'); si.value=''; render(''); setTimeout(function(){si.focus();},30); }
 function closeSearch(){ if(sm)sm.classList.remove('show'); }
 function render(q){
   cur=search(q); sel=-1;
   if(!cur.length){ sr.innerHTML='<div class="sr-empty">No matches. Try a broader word, like &ldquo;humidity&rdquo;, &ldquo;pests&rdquo; or &ldquo;feed&rdquo;.</div>'; return; }
   sr.innerHTML=cur.map(function(o,i){ var x=o.x;
     return '<a class="sr-item" data-i="'+i+'" href="'+x.url+'">'+
       '<div class="sr-k">'+esc(x.type)+(x.paper&&x.type!=='paper'?(' &middot; '+esc(x.paper)):'')+'</div>'+
       '<div class="sr-t">'+esc(x.title)+'</div>'+
       (o.snip?('<div class="sr-d">'+o.snip+'</div>'):'')+'</a>';
   }).join('');
 }
 function paint(){ $$('.sr-item').forEach(function(el,i){ el.classList.toggle('sel',i===sel); if(i===sel)el.scrollIntoView({block:'nearest'}); }); }
 function go(i){ var o=cur[i]; if(o) window.location.href=o.x.url; }
 if(si){
   si.addEventListener('input',function(){render(si.value);});
   si.addEventListener('keydown',function(e){
     if(e.key==='ArrowDown'){e.preventDefault();sel=Math.min(sel+1,cur.length-1);paint();}
     else if(e.key==='ArrowUp'){e.preventDefault();sel=Math.max(sel-1,0);paint();}
     else if(e.key==='Enter'){e.preventDefault();go(sel<0?0:sel);}
     else if(e.key==='Escape'){closeSearch();}
   });
 }
 if(sm) sm.addEventListener('click',function(e){ if(e.target===sm)closeSearch(); });

 document.addEventListener('click',function(e){
   var a=e.target.closest('[data-action]'); if(!a)return; e.preventDefault();
   var act=a.getAttribute('data-action');
   if(act==='search') openSearch();
   else if(act==='menu'){ if(sb&&sb.classList.contains('open'))closeMenu(); else openMenu(); }
   else if(act==='theme'){ setTheme(curTheme()==='dark'?'light':'dark'); }
 });
 document.addEventListener('keydown',function(e){
   if((e.ctrlKey||e.metaKey)&&(e.key==='k'||e.key==='K')){e.preventDefault();openSearch();}
 });
 $$('.sidebar .nav a').forEach(function(a){a.addEventListener('click',closeMenu);});

 var fpills=$$('.fpill');
 if(fpills.length){
   var dcards=$$('#paperdir .pcard'), demp=$('#dirEmpty');
   function filt(g){
     fpills.forEach(function(p){p.classList.toggle('on',p.getAttribute('data-filter')===g);});
     var shown=0;
     dcards.forEach(function(c){ var ok=(g==='all'||c.getAttribute('data-group')===g); c.style.display=ok?'':'none'; if(ok)shown++; });
     if(demp) demp.style.display=shown?'none':'';
   }
   fpills.forEach(function(p){p.addEventListener('click',function(){filt(p.getAttribute('data-filter'));});});
 }

 var rlinks=$$('.rail a');
 if(rlinks.length){
   var secs=rlinks.map(function(a){return document.getElementById(a.getAttribute('href').slice(1));}).filter(Boolean);
   var onScroll=function(){
     var y=window.scrollY+130, idx=0;
     for(var i=0;i<secs.length;i++){ if(secs[i].offsetTop<=y) idx=i; }
     rlinks.forEach(function(a,i){a.classList.toggle('on',i===idx);});
   };
   window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
 }
})();
"""
