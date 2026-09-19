"""Editable, source-labelled slab diagrams. No generated equipment imagery.

All coordinates are drawing coordinates, not installation dimensions. Numeric
examples are labelled calculations; none is a validated controller setpoint.
"""
from html import escape
import re

INK = '#e7eee9'
MUTED = '#b8c8c0'
GREEN = '#76dab0'
BLUE = '#81c6e8'
AMBER = '#f0c67c'
SLAB = '#4a4935'

CSS = '''<style id="slab-technical-styles">
.slab-plate{padding:0;text-align:left;margin:32px 0;border:1px solid var(--fig-line);border-radius:12px;overflow:hidden;background:var(--fig-bg)}
.slab-plate header{padding:16px 20px;border-bottom:1px solid var(--fig-line)}
.slab-plate header p{margin:0 0 5px;font:700 .72rem/1.4 var(--sans);letter-spacing:.06em;text-transform:uppercase;color:var(--fig-green)}
.slab-plate h3{margin:0;font-size:1.2rem}
.slab-drawing{overflow-x:auto;background:#14201b;scrollbar-color:#6a8c7c #14201b}
.slab-drawing svg{display:block;width:100%;min-width:0;height:auto;max-width:none}
.slab-drawing:focus-visible{outline:3px solid #76dab0;outline-offset:-3px}
.slab-plate figcaption{padding:16px 20px;font-size:.92rem;line-height:1.6}
.slab-plate .slab-scroll{display:none}
@media(max-width:650px){.slab-drawing svg{min-width:600px}.slab-plate .slab-scroll{display:block;margin:8px 0 0;font:400 .8rem/1.4 var(--sans);color:var(--mut)}}
@media print{.slab-drawing svg{min-width:0}.slab-plate{break-inside:avoid}}
</style>'''


def text(x, y, lines, size=22, color=INK, anchor='start', weight=400):
    if isinstance(lines, str):
        lines = lines.split('|')
    spans = ''.join(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.35}">{escape(s)}</tspan>' for i, s in enumerate(lines))
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{spans}</text>'


def rect(x, y, w, h, fill='none', stroke=MUTED, rx=0, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2" {extra}/>'


def line(x1, y1, x2, y2, color=MUTED, width=2, dash=''):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'


def arrow(x1, y1, x2, y2, color=BLUE):
    import math
    a = math.atan2(y2-y1, x2-x1)
    p = [(x2-11*math.cos(a+s), y2-11*math.sin(a+s)) for s in (-.45,.45)]
    return line(x1,y1,x2,y2,color,3) + f'<path d="M{p[0][0]} {p[0][1]} L{x2} {y2} L{p[1][0]} {p[1][1]}" fill="none" stroke="{color}" stroke-width="3"/>'


def circle(x,y,r,fill='none',stroke=GREEN):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def plant(x, y):
    # Botanical symbol, deliberately not a claim about cultivar morphology.
    return line(x,y,x,y-48,GREEN,3)+f'<path d="M{x} {y-24} Q{x-28} {y-51} {x-32} {y-35} Q{x-15} {y-15} {x} {y-24} M{x} {y-35} Q{x+24} {y-61} {x+31} {y-46} Q{x+18} {y-29} {x} {y-35}" fill="{GREEN}"/>'


def roots(x,y,depth=75,spread=34):
    # Branching adventitious roots; all segments stay inside the drawn media.
    out=''
    for d in (-1,0,1):
        end=x+d*spread
        out+=f'<path d="M{x+d*5} {y} Q{end} {y+depth*.4} {end} {y+depth}" fill="none" stroke="{INK}" stroke-width="1.6"/>'
        out+=line(x+d*spread*.65,y+depth*.55,end+d*12,y+depth*.78,INK,1.4)
    return out


def assembly(y=160):
    # 1 m x 75 mm longitudinal slab section; 150 mm block width/height.
    out=rect(80,y+84,560,42,SLAB,AMBER)
    for x in (145,325,505):
        out+=rect(x,y,84,84,SLAB,AMBER)+plant(x+42,y)+roots(x+42,y,115,22)
    return out


def plate(key, title, kind, body, height, caption):
    desc=escape(re.sub(r'<[^>]+>', '', caption))
    return (f'<figure class="fig slab-plate technical-plate" data-concept="{key}" id="visual-{key}">'
            f'<header><p>{escape(kind)}</p><h3>{escape(title)}</h3></header>'
            f'<div class="slab-drawing" tabindex="0" role="region" aria-label="{escape(title)} diagram, scroll horizontally on small screens">'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {height}" role="img" aria-labelledby="{key}-title {key}-desc" style="font-family:Arial,sans-serif">'
            f'<title id="{key}-title">{escape(title)}</title><desc id="{key}-desc">{desc}</desc>'
            f'<rect width="720" height="{height}" fill="#14201b"/>{body}</svg></div>'
            f'<figcaption>{caption}<span class="slab-scroll">Scroll the diagram sideways for full-size labels.</span></figcaption></figure>')


def steps(key,title,kind,rows,caption):
    body=''
    for i,(heading,detail) in enumerate(rows):
        y=24+i*115
        body+=rect(24,y,672,94,'#1b2c24','#496354',8)+circle(57,y+30,17,GREEN,GREEN)
        body+=text(57,y+37,str(i+1),20,'#14201b','middle',700)+text(91,y+32,heading,23,GREEN,weight=700)
        body+=text(91,y+61,detail,20)
        if i<len(rows)-1: body+=arrow(57,y+96,57,y+112,GREEN)
    return plate(key,title,kind,body,28+len(rows)*115,caption)


def figures():
    f={}
    b=text(36,44,'One substrate · two readings',25,GREEN,weight=700)
    for x,val,label in [(55,70,'Peak'),(250,50,'Trough')]:
        b+=rect(x,85,110,165,'#23362c','#6e8c7b')+rect(x,250-val*2,110,val*2,'#355c6e',BLUE)
        b+=text(x+55,282,f'{label} {val}%',22,anchor='middle')
    b+=arrow(174,166,238,166)+text(421,124,'70 − 50 = 20',27,GREEN,weight=700)+text(421,157,'percentage points',21)
    b+=text(421,205,'20 ÷ 70 × 100',25,AMBER)+text(421,240,'≈ 28.6% relative',23,AMBER)
    b+=text(36,338,'VWC is water volume / substrate volume.',22)+text(36,371,'The bars show readings, not a physical waterline.',20,MUTED)
    f['dryback-terminology']=plate('dryback-terminology','Dryback: points and relative percent','Calculated example',b,402,'A fall from 70% to 50% VWC is 20 percentage points, or approximately 28.6% of the starting water content. These example readings are not crop targets; the peak is not automatically field capacity.')

    b=text(36,40,'LONGITUDINAL SECTION · assumed geometry',21,GREEN)+assembly(125)
    b+=line(80,285,640,285)+line(80,276,80,294)+line(640,276,640,294)+text(360,318,'1,000 mm slab length',22,anchor='middle')
    b+=text(36,365,'3 blocks sit on openings in the wrapper.',22)+text(36,398,'Roots cross the contact face into solid substrate.',22)
    b+=text(36,442,'Slab example: 1,000 × 150 × 75 mm = 11.25 L',21,AMBER)
    b+=text(36,475,'Block example: 150 mm wide; verify actual volume.',20,MUTED)
    f['three-plant-slab']=plate('three-plant-slab','Three blocks share one slab','Geometry example · not an installation drawing',b,510,'Side section through a three-plant slab. Substrate remains continuous beneath every block; roots are conceptual. The slab dimensions give 11.25 L. The runtime example separately assumes a 3.6 L block: a literal 150 mm cube is 3.375 L, so use the actual product volume. Drain openings must follow the selected wrapper/product procedure. <a href="#ref-2">[2]</a>')

    b=text(36,36,'PLAN · 7.6 m × 1.2 m table',24,GREEN,weight=700)
    b+=rect(70,83,580,92,'#20362b','#82988b')
    for row in range(2):
        for s in range(7):
            x=93+s*75; y=91+row*65
            b+=rect(x,y,71,11,SLAB,AMBER)
            for p in range(3): b+=circle(x+12+p*23,y+5.5,2.6,GREEN,GREEN)
    b+=rect(94,122,525,14,'#304e43',GREEN,6)+circle(78,129,12,'#304e43',GREEN)
    b+=arrow(62,129,112,129,GREEN)+line(619,122,619,136,GREEN,4)
    b+=line(100,115,610,115,AMBER,3)+line(100,144,610,144,AMBER,3)
    b+=text(36,220,'14 slabs × 3 plants = 42 plants per table',23)+text(36,252,'Seven 1 m slabs leave 0.3 m at each end.',21,MUTED)
    b+=text(36,306,'CROSS-SECTION · vertical spacing schematic',21,GREEN)
    b+=rect(90,336,540,44,'#274d38',GREEN,12)+text(360,365,'Continuous trained canopy',23,INK,'middle')
    b+=line(85,493,635,493,MUTED,4)
    for x in (120,535): b+=rect(x,459,65,33,SLAB,AMBER)+rect(x,406,65,53,SLAB,AMBER)
    b+=circle(360,451,33,'#304e43',GREEN)+text(360,459,'air',18,INK,'middle')
    for x in (260,460):
        b+=line(x,493,x,433,MUTED,3)+rect(x-24,425,48,8,AMBER,AMBER)+arrow(x,420,x,388,AMBER)
    b+=text(36,543,'Centre lane: air tube + supported light bars',22)
    b+=text(36,578,'Clear below the canopy; foliage closes above it.',21,MUTED)
    f['clear-centre-layout']=plate('clear-centre-layout','Equipment below a continuous canopy','Counted layout · schematic hardware',b,614,'Two outside root rows carry 14 slabs and 42 plants. Dots mark plants; gold bars mark upward-directed lights. The central perforated tube has a dedicated inlet fan and capped far end; outlet sizing is intentionally unspecified. Cross-section heights and mounting are schematic. Canopy closure depends on cultivar, veg time and training. Three-row layouts carry 21 slabs / 63 plants; use them if the centre cannot close uniformly. Confirm clearances and airflow on the installation.')

    b=text(36,40,'TRACE THE CONNECTED WATER PATH',22,GREEN)
    b+=rect(55,85,610,26,'#334139',MUTED)+text(360,73,'Pressurised lateral',21,anchor='middle')
    b+=line(145,111,145,142,BLUE,5)+rect(128,142,34,36,'#294d5d',BLUE,6)+text(195,165,'Pressure-compensating emitter',22)
    b+=line(145,178,145,230,BLUE,5)+line(145,230,325,230,BLUE,5)+line(325,230,325,270,BLUE,5)
    b+=text(365,237,'Microtube → distributor',21,BLUE)
    b+=rect(170,275,340,115,SLAB,AMBER)+text(550,319,'Block',21,AMBER)
    b+=line(212,270,465,270,BLUE,5)
    for x in (212,296,380,465): b+=line(x,270,x,310,BLUE,3)+arrow(x,312,x,339,BLUE)
    b+=text(36,440,'Distributor symbol only: use a real ring or stakes.',21)
    b+=text(36,474,'Verify block fit, connections and caught total flow.',21,MUTED)
    f['dripper-delivery-chain']=plate('dripper-delivery-chain','A complete delivery path','Functional schematic · no invented product rendering',b,512,'Supply passes through the emitter and microtube to a supported distributor at the block. Branches are symbols, not a NetBow construction drawing or a specified outlet count. Match the actual ring/stake model, operating pressure and block fit to its documentation; measure the combined output delivered to each plant. <a href="#ref-19">[19]</a>')

    b=text(36,40,'COLLECT FOR THE SAME MEASURED INTERVAL',22,GREEN)
    for x,label in [(125,'Near'),(345,'Middle'),(565,'Far')]:
        b+=line(x,74,x,119,BLUE,4)+arrow(x,120,x,158,BLUE)+rect(x-55,172,110,90,'#203d48',BLUE)
        for j in range(4):b+=line(x-55,188+j*17,x-38,188+j*17,MUTED)
        b+=text(x,295,label,22,anchor='middle')
    b+=text(36,344,'Record mL at each outlet; label the test duration.',22)
    b+=text(36,392,'Worked runtime example',24,GREEN,weight=700)
    b+=text(36,429,'7.35 L × 0.03 × 1,000 = 220.5 mL',24)
    b+=text(36,467,'220.5 ÷ (4,000 ÷ 3,600) ≈ 198 s = 3:18',23)
    b+=text(36,511,'4 L/h is an example measured total per plant.',20,MUTED)
    f['shot-volume-runtime']=plate('shot-volume-runtime','Catch-test first, calculate runtime second','Measurement method + calculated example',b,546,'Use labelled graduated vessels or tared weighing cups at representative outlets across the active zone. Compare collections made over the same time at operating pressure. No measured uniformity result is asserted here. The runtime uses unrounded 220.5 mL and an assumed 7.35 L allocation; replace both allocation and flow with verified values.')

    b='<defs><linearGradient id="slab-moisture-gradient" gradientUnits="userSpaceOnUse" x1="0" y1="95" x2="0" y2="290"><stop offset="0" stop-color="#766744"/><stop offset="1" stop-color="#376d87"/></linearGradient></defs>'
    b+=text(36,40,'SECTION · draining, hydraulically connected media',21,GREEN)
    b+=rect(165,200,390,90,'url(#slab-moisture-gradient)',AMBER)+rect(288,95,126,105,'url(#slab-moisture-gradient)',AMBER)
    b+=plant(351,95)+roots(351,95,179,42)
    b+=arrow(251,105,251,184,BLUE)+text(36,115,'Block feed',20,BLUE)
    b+=arrow(440,182,440,246,BLUE)+text(473,167,'Redistribution',19,BLUE)
    b+=arrow(410,95,410,52,GREEN)+text(452,70,'Plant uptake',19,GREEN)
    b+=line(152,295,592,295,MUTED,2,'6 5')+arrow(555,281,615,281,BLUE)+text(485,330,'Drain boundary',20)
    b+=text(36,372,'Colour = qualitative moisture overlay.',22)+text(36,406,'It is not a material layer or a measured waterline.',21,MUTED)
    b+=text(36,452,'Retained water and outlet height change this profile.',21,AMBER)
    f['connected-water-column']=plate('connected-water-column','Contact, redistribution and drainage','Conceptual section · conditional behaviour',b,490,'Block and slab exchange water through their contact face. Under draining conditions the upper media can become drier while the slab remains wet; irrigation and uptake also affect the profile. This is not a fixed gradient or guaranteed day-by-day outcome. Grodan describes retained water changing block drying in its staged-drainage method. <a href="#ref-3">[3]</a>')

    b=text(36,40,'PLAN · record location relative to plants and outlets',21,GREEN)
    b+=rect(65,85,590,110,SLAB,AMBER)
    for x in (100,285,470): b+=rect(x,102,80,76,'#63583c',AMBER)+circle(x+40,140,8,GREEN,GREEN)
    b+=rect(229,124,11,38,'#283e35',GREEN)
    for y in (130,143,156):b+=line(240,y,274,y,INK,3)
    b+=text(36,239,'One representative location shown; compare across slabs.',20)
    b+=text(36,295,'SECTION · needles fully embedded in substrate',21,GREEN)
    b+=rect(170,329,400,118,SLAB,AMBER)
    b+=rect(147,354,23,66,'#283e35',GREEN)
    for y in (363,387,411):b+=line(170,y,290,y,INK,4)
    b+=rect(174,340,151,95,'none',GREEN,18,'stroke-dasharray="6 5"')
    b+=text(359,365,'Local sensing region',20,GREEN)+text(359,396,'not the whole slab',20)
    b+=text(36,493,'Record depth, orientation, model and calibration.',21)
    b+=text(36,528,'Air gaps or exposed needles invalidate this depiction.',20,AMBER)
    f['sensor-placement']=plate('sensor-placement','A sensor measures its local substrate','Placement schematic · consult the selected sensor manual',b,566,'Three-needle probe symbol; dimensions and sensing outline are schematic. Place representative control probes in comparable rooted zones, recording depth and distance from drippers and drains. Use additional locations for diagnosis when appropriate. METER warns that air gaps bias VWC low; orientation changes the depth sampled. <a href="#ref-18">[18]</a>')

    f['slab-preparation']=steps('slab-preparation','Prepare one repeatable starting condition','Select the manufacturer procedure before opening the wrapper',[
        ('Check support and drainage','Check the tray plane and planned drain route.'),
        ('Saturate with the intended solution','Fill through the intended openings; record EC and pH.'),
        ('Hold for the specified soak','Use the selected slab manufacturer’s procedure.'),
        ('Make the specified drainage opening','Location and stage depend on the selected method.'),
        ('Seat the block on exposed fibre','No wrapper bridging; inspect the contact face.')],
        'Charging happens with the saturation solution, not as an unexplained later step. Grodan’s staged method uses an initial opening above the seal and later definitive drainage; it is not the same as a generic set of bottom slits. Select and record one applicable procedure rather than combining their cut patterns. <a href="#ref-2">[2]</a> <a href="#ref-3">[3]</a>')

    b=''
    for i,(label,depth) in enumerate([('Block rooted',76),('Interface crossed',121),('Slab colonising',158)]):
        x=38+i*231
        b+=text(x+95,20,label,21,GREEN,'middle',700)+rect(x,165,192,75,SLAB,AMBER)+rect(x+53,75,86,90,SLAB,AMBER)
        b+=plant(x+96,75)+roots(x+96,75,depth,15+i*12)
    b+=text(36,292,'Keep the same block–slab assembly throughout.',22)
    b+=text(36,328,'Inspect roots, block hydration and repeatable uptake.',21)
    b+=text(36,365,'Progression is conceptual; no fixed day count.',20,MUTED)
    f['rooting-in-progression']=plate('rooting-in-progression','Roots cross the contact face','Conceptual stages · plant-led assessment',b,403,'The same assembly is shown at three establishment stages. Roots are drawn within continuous substrate, with multiple roots appropriate to a clone-based example. Root inspection and observed uptake inform the transition; these panels do not prescribe a transplant irrigation schedule.')

    # One reproducible synthetic daily example replaces three overlapping plots.
    events=[(2,6),(3,6),(4,6),(5,2),(7,2),(9,2)]
    samples=[(0,53),(2,50),(2,56),(3,55),(3,61),(4,60),(4,66),(5,64),(5,66),(7,64),(7,66),(9,64),(9,66),(12,62),(18,57),(24,53)]
    px=lambda h:90+h*23
    py=lambda v:297-(v-45)*6
    b=text(36,35,'SYNTHETIC DAY · clock hours after lights-on',21,GREEN)
    for start,end,label,color in [(0,2,'P0','#2c4538'),(2,4,'P1','#304e43'),(4,9,'P2','#2c4538'),(9,24,'P3','#24352d')]:
        b+=rect(px(start),59,(end-start)*23,30,color,color)+text((px(start)+px(end))/2,80,label,18,INK,'middle')
    b+=rect(px(12),95,276,232,'#101a15','#101a15')
    for v in (45,55,65):b+=line(90,py(v),642,py(v),'#486152',1,'4 5')+text(75,py(v)+6,str(v),18,MUTED,'end')
    b+=text(36,125,'VWC',18)+text(36,148,'(%)',18)
    b+='<polyline points="'+' '.join(f'{px(h)},{py(v)}' for h,v in samples)+f'" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    for h,_ in events:b+=line(px(h),103,px(h),120,BLUE,4)
    for h in (0,4,8,12,16,20,24):b+=text(px(h),350,str(h),18,MUTED,'middle')
    b+=text(90,385,'Light',20,AMBER)+text(px(12)+8,385,'Dark',20,MUTED)
    b+=text(36,429,'P3 starts after the last irrigation, before lights-off.',21)
    b+=text(36,462,'This guide ends P3 at lights-on; P0 then begins.',21)
    b+=text(36,503,'Blue ticks = irrigation events. Values are illustrative.',20,BLUE)
    f['p0-p1-p2-p3-states']=plate('p0-p1-p2-p3-states','One day, explicit phase boundaries','Synthetic trace · not room history or controller targets',b,542,'A constructed 24-hour example with a 12-hour light period. P0 is lights-on to first irrigation; P1 refills; P2 maintains; P3 runs from the final event to the next lights-on. Total between-irrigation dryback spans P3 plus the following P0. The trace and event timing illustrate this convention only. EC requires its own measured trace and method; no universal inverse EC curve is asserted.')

    f['crop-stage-arc']=steps('crop-stage-arc','Observe development before changing stage','Decision guide · no universal calendar',[
        ('Established vegetative growth','Roots established; uptake is repeatable.'),
        ('Flower setting','Observe early flower sites and ongoing stretch.'),
        ('Flower bulking','Stretch slows; track flower expansion.'),
        ('Maturity assessment','Use cultivar-specific flower observations and records.')],
        'Stage labels describe observations. They do not prove that a particular irrigation bias will produce the pictured outcome. Yellow leaves alone do not establish harvest readiness. Apply the separately attributed programme only within validated room and cultivar limits. <a href="#ref-13">[13]</a> <a href="#ref-16">[16]</a>')

    b=text(36,38,'SIDE VIEW · complete shared-slab collection',21,GREEN)+assembly(118)
    # Supply connects to every block; drain follows a different coloured path.
    b+=line(90,51,620,51,BLUE,4)
    for x in (187,367,547):b+=line(x-25,51,x-25,145,BLUE,3)
    b+=text(90,82,'Supply',19,BLUE)
    b+=line(65,285,665,285,AMBER,4)+line(65,255,65,285,AMBER,4)+line(665,255,665,340,AMBER,4)+line(665,340,604,340,AMBER,4)
    for x in (145,360,615):b+=arrow(x,246,x,278,AMBER)
    b+=rect(100,244,30,41,'#65786c',MUTED)+rect(520,244,30,41,'#65786c',MUTED)
    b+=text(80,324,'Slab raised above collection tray',20)
    b+=rect(562,348,82,95,'#203d48',BLUE)+arrow(604,339,604,367,AMBER)
    for j in range(4):b+=line(562,365+j*17,578,365+j*17,MUTED)
    b+=text(36,390,'All slab drains → tray → outlet → collector',21,AMBER)
    b+=text(36,476,'Runoff % = collected drain mL / applied mL × 100',22)
    b+=text(36,513,'Use the same slab and collection interval for both.',20,MUTED)
    f['measurement-runoff-layout']=plate('measurement-runoff-layout','Measure the whole three-plant slab','Collection schematic · no measured result claimed',b,552,'Three blocks sit on one slab supported above a runoff tray. Gold shows the complete drain path to a graduated collector; blue shows feed tubing. Slit positions are schematic, not a cutting specification. Capture all relevant drainage without allowing the slab to sit in standing runoff. Dividing slab totals by three gives an average, not individual plant measurements. <a href="#ref-15">[15]</a>')

    f['ec-correction-finish']=steps('ec-correction-finish','Separate EC correction from finishing','Measurement-led checks',[
        ('Identify the EC measurement','Feed, runoff, bulk or estimated pore-water EC?'),
        ('Check comparability','Same method, comparable VWC, calibration and time.'),
        ('Investigate before correcting','Verify delivery, drainage, feed and crop demand.'),
        ('Make and verify one bounded change','Track the next response; stop at the defined endpoint.'),
        ('Treat finishing as a separate procedure','Name the product protocol and crop-specific endpoint.')],
        'EC is reported in mS/cm (numerically equal to dS/m); solution colour is not an EC measurement. A substrate sensor’s bulk EC and estimated pore-water EC are different quantities. The cited Athena finish is a product procedure, not a universal flushing requirement. <a href="#ref-18">[18]</a> <a href="#ref-17">[17]</a>')

    f['climate-demand-response']=steps('climate-demand-response','Check demand across the table','Observation plan · no predicted airflow gain',[
        ('Measure at relevant locations','Canopy light, air conditions and plant response.'),
        ('Compare substrate response','Look at VWC slope, delivery and collected runoff.'),
        ('Check spatial differences','Repeat near, middle and far along the table.'),
        ('Respond to the observed change','Adjust within validated limits; confirm the result.')],
        'Higher environmental demand does not guarantee higher uptake in a stressed plant. Use comparable observations before changing irrigation. For perforated air tubes, measure static pressure and air movement at repeatable positions; a second tube has no quantified benefit here without measurements or a specified model.')

    f['troubleshooting-ladder']=steps('troubleshooting-ladder','Use a check that separates possible causes','Diagnostic sequence',[
        ('One plant wilts','Catch-test its outlet; inspect block contact and roots.'),
        ('High runoff with little wet-up','Inspect bypass flow, drainage and probe contact.'),
        ('EC trends upward','Compare like-for-like EC; check feed and runoff.'),
        ('Sensors disagree','Check location, calibration and actual delivery.'),
        ('Correct the identified fault','Verify recovery; log the action and response.')],
        'These checks narrow possibilities rather than proving one cause from a symptom. Restore a failed outlet or address acute plant stress promptly. Observe a complete grow-day after elective steering changes when appropriate; do not wait a day to correct a verified failure.')

    b=text(36,43,'Electrical input → eventual room heat',25,GREEN,weight=700)
    b+=text(36,102,'BTU/h = watts × 3.412',30)+text(36,157,'800 W ≈ 2,730 BTU/h',30,AMBER)
    b+=text(36,215,'Boundary: electrical energy retained inside the room.',20)
    b+=text(36,255,'Circulation redistributes heat.',22)+text(36,290,'Cooling or exhaust removes it across that boundary.',21)
    f['room-heat']=plate('room-heat','Account for the electrical load','Calculated conversion · explicit room boundary',b,331,'This conversion assumes the electrical input ultimately remains as heat within the room boundary. Account separately for remote drivers or energy leaving that boundary. No leaf-temperature reduction or local heat-index benefit is predicted from fan count.')
    return f


FIGURES=figures()
