# -*- coding: utf-8 -*-
"""figs.py, hand-authored inline SVG figures. Themed greens. Explicit viewBox."""

# palette, CSS vars so figures follow light/dark theme (defined in theme.py)
G = "var(--fig-green)"; GD = "var(--fig-green-d)"; GL = "var(--fig-green-l)"; GXL = "var(--fig-green-xl)"
INK = "var(--fig-ink)"; INK2 = "var(--fig-ink2)"; MUT = "var(--fig-mut)"; LINE = "var(--fig-line)"
AMB = "var(--fig-amber)"; AMBL = "var(--fig-amber-l)"; RED = "var(--fig-red)"; REDL = "var(--fig-red-l)"
BLU = "var(--fig-blue)"; BLUL = "var(--fig-blue-l)"; PUR = "var(--fig-purple)"; PURL = "var(--fig-purple-l)"
PAPER = "var(--fig-bg)"; PANEL2 = "var(--fig-panel)"
FS = "font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif"
MN = "font-family:ui-monospace,Consolas,monospace"

# ----------------------------------------------------------------------------
# FIG 1, end-to-end pipeline (vertical, 8 stages)
# ----------------------------------------------------------------------------
def fig_pipeline():
    stages = [
        ("0", "Mother prep", "Condition a healthy donor; flush, scout pests, push clean new growth", "~2-4 wk", GL),
        ("1", "Explant + sterilize", "Cut nodal segments / shoot tips; surface-sterilize to kill surface microbes", "1 day", GL),
        ("2", "Initiation", "Place explant on initiation medium; it wakes up and grows in the jar", "2-4 wk", GL),
        ("M", "Meristem cleanup", "Dissect the 0.2-0.5 mm meristem dome under scope = pathogen-free tissue", "4-8 wk", PURL),
        ("3", "Multiplication", "Cytokinin medium makes one shoot become many; subculture every 4-6 wk", "8-16 wk", GL),
        ("I", "Index / test", "RT-qPCR test for HpLVd & friends; keep only confirmed-clean lines", "1-2 wk", BLUL),
        ("4", "Rooting", "Auxin medium (or ex-vitro dip) grows roots on a shoot", "2-4 wk", GL),
        ("5", "Acclimatize", "Step humidity down over ~2-3 wk; harden plantlet to room air", "2-3 wk", GL),
    ]
    W = 760; rowh = 78; top = 16; H = top + rowh*len(stages) + 30
    parts = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="End-to-end tissue culture pipeline">']
    parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{PAPER}"/>')
    cx = 62
    # connector spine
    parts.append(f'<line x1="{cx}" y1="{top+26}" x2="{cx}" y2="{top+rowh*(len(stages)-1)+26}" stroke="{LINE}" stroke-width="3"/>')
    for i,(num,title,desc,dur,fill) in enumerate(stages):
        y = top + i*rowh
        node = GD if fill in (GL,) else (PUR if fill==PURL else BLU)
        parts.append(f'<circle cx="{cx}" cy="{y+26}" r="22" fill="{node}"/>')
        parts.append(f'<text x="{cx}" y="{y+32}" text-anchor="middle" fill="#fff" font-size="16" font-weight="700" style="{MN}">{num}</text>')
        bx = cx+44
        parts.append(f'<rect x="{bx}" y="{y+4}" width="{W-bx-90}" height="{rowh-14}" rx="9" fill="{fill}" stroke="{LINE}"/>')
        parts.append(f'<text x="{bx+16}" y="{y+27}" fill="{INK}" font-size="15.5" font-weight="700" style="{FS}">{title}</text>')
        parts.append(f'<text x="{bx+16}" y="{y+47}" fill="{INK2}" font-size="12" style="{FS}">{desc}</text>')
        parts.append(f'<text x="{W-22}" y="{y+30}" text-anchor="end" fill="{node}" font-size="11.5" font-weight="700" style="{FS}">{dur}</text>')
    parts.append('</svg>')
    return "".join(parts)

# ----------------------------------------------------------------------------
# FIG 2, shoot apex anatomy: why the meristem is clean
# ----------------------------------------------------------------------------
def fig_meristem():
    W=720; H=430
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Shoot tip anatomy showing pathogen-free meristem dome">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # title strip
    p.append(f'<text x="24" y="30" fill="{INK}" font-size="15" font-weight="700" style="{FS}">Longitudinal section of a shoot tip</text>')
    # stem with vascular tissue (carries viroid) -- drawn as upward tapering shape
    cx=250; base=H-40
    p.append(f'<path d="M{cx-70},{base} L{cx-34},120 Q{cx},70 {cx+34},120 L{cx+70},{base} Z" fill="{GXL}" stroke="{G}" stroke-width="2"/>')
    # vascular bundles (red = pathogen highway)
    for dx in (-40,-13,13,40):
        p.append(f'<path d="M{cx+dx},{base-6} C{cx+dx*0.7},220 {cx+dx*0.5},170 {cx+int(dx*0.35)},140" fill="none" stroke="{RED}" stroke-width="3.4" opacity=".85"/>')
    # leaf primordia
    for sgn,yy in ((-1,150),(1,168),(-1,196),(1,214)):
        x0=cx; y0=yy
        p.append(f'<path d="M{x0},{y0} q{sgn*70},-26 {sgn*96},10 q{-sgn*40},6 {-sgn*96},-10 Z" fill="{GL}" stroke="{G}" stroke-width="1.5"/>')
    # meristem dome (clean zone) -- green highlight at very tip
    p.append(f'<path d="M{cx-30},122 Q{cx},74 {cx+30},122 Z" fill="{G}"/>')
    p.append(f'<circle cx="{cx}" cy="104" r="44" fill="none" stroke="{GD}" stroke-width="2" stroke-dasharray="5 4"/>')
    # callouts (right side)
    lx=470
    def cl(y,color,t1,t2):
        s=[f'<circle cx="{lx-12}" cy="{y-4}" r="6" fill="{color}"/>']
        s.append(f'<text x="{lx+4}" y="{y}" fill="{INK}" font-size="13.5" font-weight="700" style="{FS}">{t1}</text>')
        s.append(f'<text x="{lx+4}" y="{y+18}" fill="{INK2}" font-size="11.5" style="{FS}">{t2}</text>')
        return "".join(s)
    p.append(cl(96, G, "Meristem dome (0.2-0.5 mm)", "Rapidly dividing cells. No vascular"))
    p.append(f'<text x="{lx+4}" y="132" fill="{INK2}" font-size="11.5" style="{FS}">tissue yet &rarr; pathogens can\'t reach &rarr; CLEAN.</text>')
    p.append(cl(178, GL, "Leaf primordia", "Baby leaves wrapped around the dome."))
    p.append(cl(248, RED, "Vascular tissue", "Phloem highway. Carries HpLVd, viruses,"))
    p.append(f'<text x="{lx+4}" y="284" fill="{INK2}" font-size="11.5" style="{FS}">bacteria up from the infected plant.</text>')
    # dissect line
    p.append(f'<line x1="{cx-60}" y1="128" x2="{cx+150}" y2="128" stroke="{PUR}" stroke-width="2" stroke-dasharray="6 4"/>')
    p.append(f'<text x="{cx+150}" y="124" fill="{PUR}" font-size="11.5" font-weight="700" style="{FS}">&#9986; excise here</text>')
    # legend bottom
    p.append(f'<text x="24" y="{H-14}" fill="{MUT}" font-size="11" style="{FS}">The smaller the piece you cut, the cleaner it is, and the harder it is to keep alive. Meristem culture trades survival for purity.</text>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 3, HpLVd dudding impact (healthy vs infected)
# ----------------------------------------------------------------------------
def fig_hplvd():
    W=720; H=360
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Healthy versus hop latent viroid dudded plant comparison">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    def plant(ox, healthy):
        s=[]
        col = G if healthy else AMB
        leafcol = GL if healthy else "#efe2c4"
        # pot
        s.append(f'<path d="M{ox-44},{H-60} L{ox+44},{H-60} L{ox+34},{H-20} L{ox-34},{H-20} Z" fill="#c9b59b" stroke="{MUT}"/>')
        # stem
        stemtop = 90 if healthy else 150
        s.append(f'<line x1="{ox}" y1="{H-60}" x2="{ox}" y2="{stemtop}" stroke="{col}" stroke-width="6"/>')
        # buds / colas
        if healthy:
            s.append(f'<ellipse cx="{ox}" cy="{stemtop-6}" rx="26" ry="44" fill="{G}" opacity=".9"/>')
            s.append(f'<ellipse cx="{ox-40}" cy="150" rx="16" ry="30" fill="{G}" opacity=".85"/>')
            s.append(f'<ellipse cx="{ox+40}" cy="150" rx="16" ry="30" fill="{G}" opacity=".85"/>')
        else:
            s.append(f'<ellipse cx="{ox}" cy="{stemtop-4}" rx="13" ry="20" fill="{AMB}" opacity=".75"/>')
            s.append(f'<ellipse cx="{ox-30}" cy="190" rx="8" ry="14" fill="{AMB}" opacity=".7"/>')
            s.append(f'<ellipse cx="{ox+30}" cy="190" rx="8" ry="14" fill="{AMB}" opacity=".7"/>')
        # fan leaves
        for sgn,yy,sz in (((-1,150,1.0),(1,170,1.0),(-1,210,0.85),(1,230,0.85)) if healthy else ((-1,200,0.6),(1,220,0.6),(-1,240,0.5),(1,255,0.5))):
            pass
        leaves = ((-1,150,1.0),(1,170,1.0),(-1,210,0.85),(1,230,0.85)) if healthy else ((-1,205,0.6),(1,225,0.55),(-1,250,0.5))
        for sgn,yy,sz in leaves:
            w=int(46*sz); hh=int(12*sz)
            s.append(f'<path d="M{ox},{yy} q{sgn*w},{-hh} {sgn*int(w*1.4)},{hh} q{-sgn*int(w*0.6)},{hh} {-sgn*int(w*1.4)},{-hh} Z" fill="{leafcol}" stroke="{col}" stroke-width="1.3"/>')
        return "".join(s)
    # left healthy
    p.append(plant(190, True))
    p.append(f'<rect x="60" y="20" width="260" height="30" rx="15" fill="{GL}"/>')
    p.append(f'<text x="190" y="40" text-anchor="middle" fill="{GD}" font-size="14" font-weight="700" style="{FS}">CLEAN MOTHER</text>')
    # right dudded
    p.append(plant(530, False))
    p.append(f'<rect x="400" y="20" width="260" height="30" rx="15" fill="{AMBL}"/>')
    p.append(f'<text x="530" y="40" text-anchor="middle" fill="{AMB}" font-size="14" font-weight="700" style="{FS}">HpLVd "DUDDED"</text>')
    # divider
    p.append(f'<line x1="360" y1="60" x2="360" y2="{H-20}" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="4 5"/>')
    # symptom callouts
    syms=["Stunted height","Smaller, looser buds","~30% less yield","Reduced cannabinoids/terpenes","Brittle stems, odd leaves"]
    for i,t in enumerate(syms):
        yy=80+i*30
        p.append(f'<text x="600" y="{yy}" fill="{AMB}" font-size="11.5" style="{FS}">&#8226; {t}</text>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 4, surface sterilization timeline
# ----------------------------------------------------------------------------
def fig_sterilize():
    steps=[
        ("Trim","Cut explant; strip large leaves","",GL,GD),
        ("Wash","Soapy water + running tap, 10-20 min","tap",BLUL,BLU),
        ("70% EtOH","Dunk 30-60 s (lipid/surface kill)","30-60 s",GL,GD),
        ("Bleach","0.5-1% NaOCl + drop Tween, 8-15 min, swirl","8-15 min",AMBL,AMB),
        ("Rinse x3","Sterile distilled water, 3-5 min each","x3",BLUL,BLU),
        ("Trim ends","Cut off bleach-damaged tissue in hood","",PURL,PUR),
        ("Plate","Place on initiation medium, seal","",GL,GD),
    ]
    W=760; bw=98; gap=8; H=190
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Surface sterilization sequence">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    x0=12
    for i,(t,d,badge,fill,col) in enumerate(steps):
        x=x0+i*(bw+gap)
        p.append(f'<rect x="{x}" y="46" width="{bw}" height="98" rx="10" fill="{fill}" stroke="{LINE}"/>')
        p.append(f'<circle cx="{x+bw/2}" cy="40" r="15" fill="{col}"/>')
        p.append(f'<text x="{x+bw/2}" y="45" text-anchor="middle" fill="#fff" font-size="13" font-weight="700" style="{MN}">{i+1}</text>')
        p.append(f'<text x="{x+bw/2}" y="74" text-anchor="middle" fill="{INK}" font-size="12.5" font-weight="700" style="{FS}">{t}</text>')
        # wrap desc into <=14 char lines
        words=d.split(); line=""; ly=92
        for w in words:
            if len(line)+len(w)+1>15:
                p.append(f'<text x="{x+bw/2}" y="{ly}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{line}</text>')
                ly+=12; line=w
            else:
                line=(line+" "+w).strip()
        if line:
            p.append(f'<text x="{x+bw/2}" y="{ly}" text-anchor="middle" fill="{INK2}" font-size="9.6" style="{FS}">{line}</text>')
        if i<len(steps)-1:
            ax=x+bw+gap/2
            p.append(f'<text x="{ax-1}" y="99" text-anchor="middle" fill="{MUT}" font-size="15" font-weight="700">&rarr;</text>')
    p.append(f'<text x="12" y="172" fill="{MUT}" font-size="11" style="{FS}">Everything from step 3 onward happens inside the still-air box / flow hood with sterilized tools. Times scale with tissue toughness.</text>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 5, classic 5 stages of micropropagation (horizontal)
# ----------------------------------------------------------------------------
def fig_5stages():
    st=[("0","Donor","Select & condition the mother plant",GL),
        ("I","Initiation","Establish a clean, growing culture",GL),
        ("II","Multiplication","Multiply shoots, cycle after cycle",GL),
        ("III","Rooting","Induce roots on shoots",GL),
        ("IV","Acclimatization","Harden to the outside world",GL)]
    W=760; H=160; bw=140; gap=12; x0=14
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The five classic stages of micropropagation">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    for i,(n,t,d,fill) in enumerate(st):
        x=x0+i*(bw+gap)
        grad = GD if i%2==0 else G
        p.append(f'<rect x="{x}" y="36" width="{bw}" height="96" rx="12" fill="{fill}" stroke="{G}" stroke-width="1.4"/>')
        p.append(f'<rect x="{x}" y="36" width="{bw}" height="26" rx="12" fill="{grad}"/>')
        p.append(f'<rect x="{x}" y="50" width="{bw}" height="12" fill="{grad}"/>')
        p.append(f'<text x="{x+14}" y="54" fill="#fff" font-size="13" font-weight="700" style="{MN}">Stage {n}</text>')
        p.append(f'<text x="{x+bw/2}" y="84" text-anchor="middle" fill="{INK}" font-size="13.5" font-weight="700" style="{FS}">{t}</text>')
        words=d.split(); line=""; ly=104
        for w in words:
            if len(line)+len(w)+1>18:
                p.append(f'<text x="{x+bw/2}" y="{ly}" text-anchor="middle" fill="{INK2}" font-size="10.5" style="{FS}">{line}</text>'); ly+=13; line=w
            else: line=(line+" "+w).strip()
        if line: p.append(f'<text x="{x+bw/2}" y="{ly}" text-anchor="middle" fill="{INK2}" font-size="10.5" style="{FS}">{line}</text>')
        if i<len(st)-1:
            p.append(f'<text x="{x+bw+gap/2-1}" y="90" text-anchor="middle" fill="{G}" font-size="18" font-weight="700">&rarr;</text>')
    p.append(f'<text x="14" y="24" fill="{INK}" font-size="13" font-weight="700" style="{FS}">The Murashige model, every plant-TC workflow on earth maps to these five stages.</text>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 6, project timeline (gantt, weeks)
# ----------------------------------------------------------------------------
def fig_timeline():
    rows=[("Mother prep",0,3,G),("Sterilize + initiate",3,4,G),
          ("Meristem excision",6,2,PUR),("Grow-out + index (RT-qPCR)",8,4,BLU),
          ("Multiplication cycles",10,10,G),("Rooting",20,3,G),
          ("Acclimatization",23,3,G),("Re-establish mother",26,4,GD)]
    weeks=32; W=760; left=180; right=24; H=40+len(rows)*34+34
    plotw=W-left-right
    def wx(w): return left + w/weeks*plotw
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Project timeline in weeks">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # week gridlines
    for w in range(0,weeks+1,4):
        x=wx(w)
        p.append(f'<line x1="{x}" y1="34" x2="{x}" y2="{H-24}" stroke="{LINE}" stroke-width="1"/>')
        p.append(f'<text x="{x}" y="26" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">wk {w}</text>')
    for i,(t,s,d,c) in enumerate(rows):
        y=40+i*34
        p.append(f'<text x="{left-10}" y="{y+18}" text-anchor="end" fill="{INK2}" font-size="12" style="{FS}">{t}</text>')
        bx=wx(s); bw=wx(s+d)-wx(s)
        p.append(f'<rect x="{bx}" y="{y+5}" width="{bw}" height="20" rx="6" fill="{c}" opacity=".88"/>')
        p.append(f'<text x="{bx+bw/2}" y="{y+19}" text-anchor="middle" fill="#fff" font-size="10.5" font-weight="700" style="{FS}">{d}w</text>')
    p.append(f'<text x="{left}" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Indicative for a careful beginner. Multiplication and indexing overlap. Total &asymp; 6-8 months explant &rarr; proven-clean mother.</text>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 7, still-air box aseptic workflow / zones
# ----------------------------------------------------------------------------
def fig_lab():
    W=720; H=380
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Aseptic work zone layout">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # box outline
    p.append(f'<rect x="40" y="50" width="640" height="280" rx="14" fill="{GXL}" stroke="{GD}" stroke-width="2"/>')
    p.append(f'<text x="360" y="38" text-anchor="middle" fill="{INK}" font-size="14" font-weight="700" style="{FS}">Inside the still-air box / flow hood, the sterile work zone</text>')
    # hand holes
    p.append(f'<ellipse cx="200" cy="330" rx="48" ry="14" fill="{PANEL2}" stroke="{LINE}"/>')
    p.append(f'<ellipse cx="520" cy="330" rx="48" ry="14" fill="{PANEL2}" stroke="{LINE}"/>')
    p.append(f'<text x="360" y="350" text-anchor="middle" fill="{MUT}" font-size="11" style="{FS}">arm openings</text>')
    def item(x,y,w,h,fill,col,label,sub):
        s=[f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{fill}" stroke="{col}" stroke-width="1.5"/>']
        s.append(f'<text x="{x+w/2}" y="{y+h/2-2}" text-anchor="middle" fill="{INK}" font-size="12" font-weight="700" style="{FS}">{label}</text>')
        s.append(f'<text x="{x+w/2}" y="{y+h/2+14}" text-anchor="middle" fill="{INK2}" font-size="9.8" style="{FS}">{sub}</text>')
        return "".join(s)
    # center sterile field
    p.append(item(290,150,150,90,GL,G,"STERILE FIELD","work only here"))
    p.append(f'<circle cx="365" cy="178" r="3" fill="{GD}"/>')
    # alcohol lamp / bead sterilizer
    p.append(item(80,90,150,60,REDL,RED,"Flame / bead","sterilize tools 5-10 s"))
    # 70% alcohol spray
    p.append(item(80,180,150,60,BLUL,BLU,"70% alcohol","wipe surfaces + gloves"))
    # tools
    p.append(item(80,270,150,46,PANEL2,MUT,"Scalpel + forceps","in alcohol jar"))
    # media vessels
    p.append(item(490,90,150,60,GL,G,"Sterile media jars","sealed until use"))
    # explant dish
    p.append(item(490,180,150,60,GL,G,"Explant dish","sterile petri / tile"))
    # waste
    p.append(item(490,270,150,46,AMBL,AMB,"Discard pile","trimmings + waste"))
    # flow arrows tools->field
    p.append(f'<path d="M232,118 C265,150 270,170 288,182" fill="none" stroke="{MUT}" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
    p.append(f'<path d="M488,118 C455,150 450,170 442,182" fill="none" stroke="{MUT}" stroke-width="1.6" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
    p.append(f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="{MUT}"/></marker></defs>')
    p.append('</svg>')
    return "".join(p)

# ----------------------------------------------------------------------------
# FIG 8, acclimatization humidity step-down
# ----------------------------------------------------------------------------
def fig_acclim():
    W=720; H=300; left=58; right=20; top=30; bot=H-46
    pts=[(0,98),(3,95),(6,88),(9,78),(12,68),(15,58),(18,50),(21,45)]
    days=21
    plotw=W-left-right; ploth=bot-top
    def X(d): return left + d/days*plotw
    def Y(h): return bot - (h-40)/60*ploth   # 40..100 % range
    p=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Humidity step-down during acclimatization">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    p.append(f'<text x="{left}" y="20" fill="{INK}" font-size="13" font-weight="700" style="{FS}">Acclimatization: step the humidity down, never drop it in one go</text>')
    # axes
    p.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bot}" stroke="{LINE}" stroke-width="1.5"/>')
    p.append(f'<line x1="{left}" y1="{bot}" x2="{W-right}" y2="{bot}" stroke="{LINE}" stroke-width="1.5"/>')
    for hh in (40,60,80,100):
        y=Y(hh)
        p.append(f'<line x1="{left}" y1="{y}" x2="{W-right}" y2="{y}" stroke="{LINE}" stroke-width="0.8" stroke-dasharray="3 4"/>')
        p.append(f'<text x="{left-8}" y="{y+4}" text-anchor="end" fill="{MUT}" font-size="10.5" style="{MN}">{hh}%</text>')
    for d in (0,3,6,9,12,15,18,21):
        x=X(d)
        p.append(f'<text x="{x}" y="{bot+16}" text-anchor="middle" fill="{MUT}" font-size="10.5" style="{MN}">d{d}</text>')
    # area + line
    path="M"+" L".join(f"{X(d)},{Y(h)}" for d,h in pts)
    p.append(f'<path d="{path} L{X(21)},{bot} L{X(0)},{bot} Z" fill="{GL}" opacity=".6"/>')
    p.append(f'<path d="{path}" fill="none" stroke="{GD}" stroke-width="3"/>')
    for d,h in pts:
        p.append(f'<circle cx="{X(d)}" cy="{Y(h)}" r="3.4" fill="{GD}"/>')
    # annotations
    p.append(f'<text x="{X(0)+6}" y="{Y(98)-8}" fill="{GD}" font-size="10.5" style="{FS}">dome shut</text>')
    p.append(f'<text x="{X(9)-6}" y="{Y(78)-10}" fill="{GD}" font-size="10.5" style="{FS}">crack vents wider daily</text>')
    p.append(f'<text x="{X(21)-4}" y="{Y(45)-10}" text-anchor="end" fill="{GD}" font-size="10.5" style="{FS}">dome off, ambient air</text>')
    p.append(f'<text x="{left}" y="{H-8}" fill="{MUT}" font-size="11" style="{FS}">Roots and a working wax cuticle take ~2-3 weeks to form. Too-fast drying = wilt + death.</text>')
    p.append('</svg>')
    return "".join(p)
