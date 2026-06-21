# -*- coding: utf-8 -*-
"""figs_extra.py, additional inline SVG figures. Palette from figs."""
from figs import (G, GD, GL, GXL, INK, INK2, MUT, LINE, AMB, AMBL, RED, REDL,
                  BLU, BLUL, PUR, PURL, PAPER, PANEL2, FS, MN)

# FIG 9, explant selection trade-off
def fig_explant():
    W=720; H=362
    cols=[("Nodal segment","~10 mm, 1 node",GL,GD,"Easiest","Surface clean only",
           "Keeps vascular tissue, so a viroid stays put. The beginner default for plain cloning."),
          ("Shoot tip","2-5 mm + primordia",GL,GD,"Medium","Partly clean",
           "Cleaner genetics. Cut it too big and ~50% turn fungal."),
          ("Meristem dome","0.2-0.5 mm dome",PURL,PUR,"Hardest","Pathogen-FREE",
           "Needs a dissecting scope. The only route that clears HpLVd. ~5% contaminate.")]
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Explant type trade-off">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="28" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Pick your explant: cleaner means smaller means harder to keep alive</text>')
    cw=222; x0=22; gap=12; top=46
    for i,(t,sz,fill,col,diff,clean,note) in enumerate(cols):
        x=x0+i*(cw+gap)
        p.append(f'<rect x="{x}" y="{top}" width="{cw}" height="270" rx="12" fill="{fill}" stroke="{col}" stroke-width="1.5"/>')
        p.append(f'<rect x="{x}" y="{top}" width="{cw}" height="34" rx="12" fill="{col}"/>')
        p.append(f'<rect x="{x}" y="{top+18}" width="{cw}" height="16" fill="{col}"/>')
        p.append(f'<text x="{x+cw/2}" y="{top+23}" text-anchor="middle" fill="#fff" font-size="14" font-weight="700" style="{FS}">{t}</text>')
        p.append(f'<text x="{x+cw/2}" y="{top+52}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">{sz}</text>')
        midx=x+cw/2; dy=top+98
        if i==0:
            p.append(f'<line x1="{midx}" y1="{dy-26}" x2="{midx}" y2="{dy+26}" stroke="{GD}" stroke-width="5"/>')
            p.append(f'<circle cx="{midx}" cy="{dy}" r="6" fill="{G}"/>')
            p.append(f'<path d="M{midx},{dy} q22,-10 34,2" fill="none" stroke="{G}" stroke-width="2.4"/>')
        elif i==1:
            p.append(f'<line x1="{midx}" y1="{dy+24}" x2="{midx}" y2="{dy-10}" stroke="{GD}" stroke-width="5"/>')
            p.append(f'<path d="M{midx-16},{dy-8} Q{midx},{dy-34} {midx+16},{dy-8} Z" fill="{G}"/>')
            p.append(f'<path d="M{midx},{dy-4} q-20,-6 -28,8" fill="none" stroke="{G}" stroke-width="2.2"/>')
            p.append(f'<path d="M{midx},{dy+4} q20,-4 28,10" fill="none" stroke="{G}" stroke-width="2.2"/>')
        else:
            p.append(f'<path d="M{midx-14},{dy} Q{midx},{dy-24} {midx+14},{dy} Z" fill="{PUR}"/>')
            p.append(f'<circle cx="{midx}" cy="{dy-6}" r="20" fill="none" stroke="{PUR}" stroke-width="1.6" stroke-dasharray="3 3"/>')
        fy=top+150
        for lab,val,c in (("Difficulty",diff,col),("Cleanliness",clean,col)):
            p.append(f'<text x="{x+14}" y="{fy}" fill="{MUT}" font-size="10.5" style="{FS}">{lab}</text>')
            p.append(f'<text x="{x+cw-14}" y="{fy}" text-anchor="end" fill="{c}" font-size="11.5" font-weight="700" style="{FS}">{val}</text>')
            fy+=20
        words=note.split(); line=""; ly=top+200
        for w in words:
            if len(line)+len(w)+1>30:
                p.append(f'<text x="{x+14}" y="{ly}" fill="{INK2}" font-size="10.3" style="{FS}">{line}</text>'); ly+=14; line=w
            else: line=(line+" "+w).strip()
        if line: p.append(f'<text x="{x+14}" y="{ly}" fill="{INK2}" font-size="10.3" style="{FS}">{line}</text>')
    p.append(f'<text x="24" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">&larr; easier / dirtier&nbsp;&nbsp;|&nbsp;&nbsp;harder / cleaner &rarr;</text>')
    p.append('</svg>')
    return "".join(p)

# FIG 10, HLVd clearance per cultivar (bar)
def fig_hlvd_clearance():
    data=[("Valarie",100),("Athena*",94),("FRB1.4",69),("AnnaLee",62),
          ("Wife",50),("Hybrid 9",26),("Hybrid 5",14),("EarlyPearly",14)]
    W=720; H=332; left=54; right=20; top=58; bot=H-58
    n=len(data); plotw=W-left-right; step=plotw/n; bw=step*0.62
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HLVd clearance rate by cultivar">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">HpLVd clearance is brutally genotype-dependent</text>')
    p.append(f'<text x="24" y="46" fill="{MUT}" font-size="11.5" style="{FS}">One meristem + thermotherapy protocol, 13 cultivars. Disease fully eradicated in just 5 of 13.</text>')
    for v in (0,25,50,75,100):
        y=bot-(v/100)*(bot-top)
        p.append(f'<line x1="{left}" y1="{y}" x2="{W-right}" y2="{y}" stroke="{LINE}" stroke-width="0.8" stroke-dasharray="3 4"/>')
        p.append(f'<text x="{left-8}" y="{y+4}" text-anchor="end" fill="{MUT}" font-size="10" style="{MN}">{v}%</text>')
    for i,(name,val) in enumerate(data):
        x=left+i*step+(step-bw)/2
        h=(val/100)*(bot-top)
        col=G if val>=50 else AMB
        p.append(f'<rect x="{x}" y="{bot-h}" width="{bw}" height="{h}" rx="4" fill="{col}" opacity=".9"/>')
        p.append(f'<text x="{x+bw/2}" y="{bot-h-6}" text-anchor="middle" fill="{col}" font-size="11" font-weight="700" style="{FS}">{val}%</text>')
        p.append(f'<text x="{x+bw/2}" y="{bot+15}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{name}</text>')
    p.append(f'<text x="{left}" y="{H-8}" fill="{MUT}" font-size="10.3" style="{FS}">*&ldquo;Athena&rdquo; here is a cannabis STRAIN, not the Athena Ag kit. Source: 13-cultivar thermotherapy study, 2024-25.</text>')
    p.append('</svg>')
    return "".join(p)

# FIG 11, subculture mutation accumulation
def fig_subculture():
    W=720; H=302; left=58; right=24; top=40; bot=H-46
    pts=[(1,8),(2,15),(3,23),(4,30),(5,38),(6,47),(7,58),(8,70),(9,83),(10,96)]
    maxsub=10; maxmut=100; plotw=W-left-right; ploth=bot-top
    def X(s): return left+(s-1)/(maxsub-1)*plotw
    def Y(m): return bot-(m/maxmut)*ploth
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mutation accumulation versus subculture number">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="24" fill="{INK}" font-size="14.5" font-weight="700" style="{FS}">Every subculture adds mutations, reset before clones drift</text>')
    p.append(f'<rect x="{left}" y="{top}" width="{X(5)-left}" height="{ploth}" fill="{GL}" opacity=".55"/>')
    p.append(f'<text x="{(left+X(5))/2}" y="{top+18}" text-anchor="middle" fill="{GD}" font-size="11" font-weight="700" style="{FS}">SAFE &le; 5 cycles</text>')
    p.append(f'<rect x="{X(5)}" y="{top}" width="{X(10)-X(5)}" height="{ploth}" fill="{AMBL}" opacity=".55"/>')
    p.append(f'<text x="{(X(5)+X(10))/2}" y="{top+18}" text-anchor="middle" fill="{AMB}" font-size="11" font-weight="700" style="{FS}">DRIFT RISK</text>')
    p.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bot}" stroke="{LINE}" stroke-width="1.4"/>')
    p.append(f'<line x1="{left}" y1="{bot}" x2="{W-right}" y2="{bot}" stroke="{LINE}" stroke-width="1.4"/>')
    p.append(f'<text x="20" y="{(top+bot)/2}" fill="{MUT}" font-size="10.5" style="{FS}" transform="rotate(-90 20,{(top+bot)/2})" text-anchor="middle">mutations &rarr;</text>')
    for s in range(1,maxsub+1):
        x=X(s); p.append(f'<text x="{x}" y="{bot+16}" text-anchor="middle" fill="{MUT}" font-size="10" style="{MN}">{s}</text>')
    p.append(f'<text x="{(left+W-right)/2}" y="{bot+32}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{FS}">subculture number</text>')
    path="M"+" L".join(f"{X(s)},{Y(m)}" for s,m in pts)
    p.append(f'<path d="{path}" fill="none" stroke="{RED}" stroke-width="3"/>')
    for s,m in pts: p.append(f'<circle cx="{X(s)}" cy="{Y(m)}" r="3.4" fill="{RED}"/>')
    p.append(f'<line x1="{X(5)}" y1="{top}" x2="{X(5)}" y2="{bot}" stroke="{GD}" stroke-width="1.6" stroke-dasharray="5 4"/>')
    p.append('</svg>')
    return "".join(p)

# FIG 12, annotated Athena kit
def fig_athena_kit():
    W=720; H=384
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Athena Culture Kit annotated">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">What is in the Athena Culture Kit, and what they will not tell you</text>')
    p.append(f'<rect x="40" y="44" width="640" height="246" rx="14" fill="{GXL}" stroke="{GD}" stroke-width="2"/>')
    def comp(x,y,w,h,fill,col,label,sub):
        s=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{col}" stroke-width="1.5"/>']
        s.append(f'<text x="{x+w/2}" y="{y+h/2-3}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{label}</text>')
        if sub: s.append(f'<text x="{x+w/2}" y="{y+h/2+13}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{sub}</text>')
        return "".join(s)
    p.append(comp(64,68,180,72,GL,G,"Laminar flow hood","HEPA H13, 0.5-0.9 m/s"))
    p.append(comp(260,68,180,72,GL,G,"One-touch autoclave","sterilize media + tools"))
    p.append(comp(456,68,200,72,GL,G,"Tools + toolbox","scalpel, forceps, lid guide"))
    p.append(comp(64,160,180,72,BLUL,BLU,"SHOOTS media (blue)","multiply shoots"))
    p.append(comp(260,160,180,72,GL,G,"ROOTS media","callus + rooting"))
    p.append(comp(456,160,200,72,AMBL,AMB,"Cleanse + Bleach","surface sterilants"))
    p.append(comp(64,248,592,30,PANEL2,MUT,"~120 vessels out of the box  ·  refills extra: $15/vessel, $30-40/media box, $100 HEPA",""))
    ly=314
    p.append(f'<rect x="40" y="{ly}" width="16" height="16" rx="3" fill="{GL}" stroke="{G}"/>')
    p.append(f'<text x="62" y="{ly+13}" fill="{INK2}" font-size="11.5" style="{FS}">Confirmed specs</text>')
    p.append(f'<rect x="200" y="{ly}" width="16" height="16" rx="3" fill="{AMBL}" stroke="{AMB}"/>')
    p.append(f'<text x="222" y="{ly+13}" fill="{INK2}" font-size="11.5" style="{FS}">Undisclosed / proprietary:</text>')
    p.append(f'<text x="40" y="{ly+36}" fill="{AMB}" font-size="11" style="{FS}">Media base salt (MS? DKW?), the hormones &amp; their doses, the bleach/Cleanse dilutions &amp; soak times, all trade secret.</text>')
    p.append(f'<text x="40" y="{ly+52}" fill="{AMB}" font-size="11" style="{FS}">No qPCR test and no thermotherapy ship in the box, so the kit cannot, by itself, PROVE a plant is clean.</text>')
    p.append('</svg>')
    return "".join(p)

# FIG 13, contamination visual ID
def fig_contam():
    W=720; H=252
    cards=[("BACTERIA",REDL,RED,"Shiny cream/white slime or ooze at the cut base; cloudy medium; sour smell.","Often LATENT, erupts after 1-2 wk"),
           ("FUNGI",AMBL,AMB,"Fuzzy cottony threads; black, green or yellow spore spots spreading fast.","Airborne spores = an air/technique problem"),
           ("YEAST",PURL,PUR,"Cloudy medium, bready smell, glossy raised dots. Doubles in under 90 min.","One slip wrecks a batch overnight"),
           ("ENDOPHYTE",BLUL,BLU,"Looks clean for weeks, then a bloom from INSIDE the tissue.","Rode in with the mother, bleach cannot reach it")]
    cw=168; gap=12; x0=18; top=56
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Contamination identification">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="24" y="26" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Know your enemy: the four ways a jar goes bad</text>')
    p.append(f'<text x="24" y="45" fill="{MUT}" font-size="11.5" style="{FS}">Inspect every vessel daily. When in doubt, pull it out, one bad jar infects the shelf.</text>')
    for i,(t,fill,col,desc,tag) in enumerate(cards):
        x=x0+i*(cw+gap)
        p.append(f'<rect x="{x}" y="{top}" width="{cw}" height="172" rx="11" fill="{fill}" stroke="{col}" stroke-width="1.4"/>')
        p.append(f'<rect x="{x}" y="{top}" width="{cw}" height="28" rx="11" fill="{col}"/>')
        p.append(f'<rect x="{x}" y="{top+14}" width="{cw}" height="14" fill="{col}"/>')
        p.append(f'<text x="{x+cw/2}" y="{top+19}" text-anchor="middle" fill="#fff" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        words=desc.split(); line=""; ly=top+48
        for w in words:
            if len(line)+len(w)+1>24:
                p.append(f'<text x="{x+12}" y="{ly}" fill="{INK2}" font-size="10.4" style="{FS}">{line}</text>'); ly+=14; line=w
            else: line=(line+" "+w).strip()
        if line: p.append(f'<text x="{x+12}" y="{ly}" fill="{INK2}" font-size="10.4" style="{FS}">{line}</text>')
        words=tag.split(); line=""; tl=[]
        for w in words:
            if len(line)+len(w)+1>26: tl.append(line); line=w
            else: line=(line+" "+w).strip()
        if line: tl.append(line)
        ystart=top+172-12*len(tl)-8
        for k,ln in enumerate(tl):
            p.append(f'<text x="{x+12}" y="{ystart+k*12}" fill="{col}" font-size="9.6" font-weight="700" style="{FS}">{ln}</text>')
    p.append('</svg>')
    return "".join(p)
