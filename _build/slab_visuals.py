"""Editable, source-labelled slab diagrams. No generated equipment imagery.

All coordinates are drawing coordinates, not installation dimensions. Numeric
examples are labelled calculations; none is a validated controller setpoint.
"""
from html import escape
from pathlib import Path
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
#visual-sensor-placement .slab-drawing svg{min-width:1000px}
.slab-drawing:focus-visible{outline:3px solid #76dab0;outline-offset:-3px}
.slab-plate figcaption{padding:16px 20px;font-size:.92rem;line-height:1.6}
.slab-plate .slab-scroll{display:none}
@media(max-width:650px){.slab-drawing svg{min-width:600px}.slab-plate .slab-scroll{display:block;margin:8px 0 0;font:400 .8rem/1.4 var(--sans);color:var(--mut)}}
@media print{.slab-drawing svg,#visual-sensor-placement .slab-drawing svg{min-width:0}.slab-plate{break-inside:avoid}}
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
            f'<div class="slab-drawing" tabindex="0" role="region" aria-label="{escape(title)} diagram. Move it to the side on small screens.">'
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {height}" role="img" aria-labelledby="{key}-title {key}-desc" style="font-family:Arial,sans-serif">'
            f'<title id="{key}-title">{escape(title)}</title><desc id="{key}-desc">{desc}</desc>'
            f'<rect width="720" height="{height}" fill="#14201b"/>{body}</svg></div>'
            f'<figcaption>{caption} <span class="slab-scroll">Move the diagram to the side to see the labels at full size.</span></figcaption></figure>')


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
    b=text(36,44,'Example VWC readings',25,GREEN,weight=700)
    for x,val,label in [(55,70,'Peak'),(250,50,'Trough')]:
        b+=rect(x,85,110,165,'#23362c','#6e8c7b')+rect(x,250-val*2,110,val*2,'#355c6e',BLUE)
        b+=text(x+55,282,f'{label} {val}%',22,anchor='middle')
    b+=arrow(174,166,238,166)+text(421,124,'70 − 50 = 20',27,GREEN,weight=700)+text(421,157,'percentage points',21)
    b+=text(421,205,'20 ÷ 70 × 100',25,AMBER)+text(421,240,'≈ 28.6% of start',23,AMBER)
    b+=text(36,338,'VWC = volume of water ÷ volume of substrate.',22)+text(36,371,'The bars show measured VWC values.',20,MUTED)
    f['dryback-terminology']=plate('dryback-terminology','Absolute dryback and relative dryback','Calculated example',b,402,'When the VWC decreases from 70% to 50%, the absolute dryback is 20 percentage points. The relative dryback is approximately 28.6% of the start water content. These values are only an example. To find the field capacity, make a different measurement of the drainage.')

    b=text(36,40,'SECTION ALONG THE SLAB · example size',21,GREEN)+assembly(125)
    b+=line(80,285,640,285)+line(80,276,80,294)+line(640,276,640,294)+text(360,318,'1,000 mm slab length',22,anchor='middle')
    b+=text(36,365,'3 blocks go on openings in the wrapper.',22)+text(36,398,'Roots go from the block into the slab, a solid substrate.',22)
    b+=text(36,442,'Slab example: 1,000 × 150 × 75 mm = 11.25 L',21,AMBER)
    b+=text(36,475,'Block example: 150 mm wide. Measure the volume.',20,MUTED)
    f['three-plant-slab']=plate('three-plant-slab','Three-block slab cross-section','Example dimensions',b,510,'Side section of a slab with three plants. The substrate is continuous below each block, and the roots are only a symbol. The dimensions of the slab give 11.25 L, and a cube of 150 mm is 3.375 L. For the block, this paper uses a different value of 3.6 L for the volume of the product. The drain openings must agree with the procedure for the wrapper and the product that you select. <a href="#ref-2">[2]</a>')

    def table_plan(top, crosswise=False):
        out=rect(72,top,590,155,'#20362b','#82988b')
        # Seven overhead-light bays, each with three slabs / nine plants.
        for col in range(7):
            x=100+col*76
            out+=rect(x-3,top+4,76,147,'none','#71877b',extra='stroke-dasharray="4 5"')
            for row in range(3):
                y=top+14+row*57
                out+=rect(x,y,70,12,SLAB,AMBER,extra='data-layout-slab="true"')
                for dot in range(3):out+=circle(x+12+dot*23,y+6,2.6,GREEN,GREEN)
        for y in (top+48,top+105):
            out+=rect(94,y-10,541,20,'#304e43',GREEN,8)
            out+=circle(79,y,12,'#304e43',GREEN)+arrow(61,y,109,y,GREEN)
            out+=line(635,y-9,635,y+9,GREEN,3)
            for x in range(130,620,40):out+=circle(x,y+7,1.5,GREEN,GREEN)
            if not crosswise:out+=line(101,y,628,y,AMBER,5)
        if crosswise:
            for col in range(7):
                x=135+col*76
                out+=line(x,top+5,x,top+149,AMBER,5)
        return out

    b=text(36,36,'THREE ROWS · 7.6 m × 1.2 m table',24,GREEN,weight=700)
    b+=text(36,73,'21 slabs × 3 plants = 63 plants for each table',23)
    b+=text(36,107,'7 top lights × 9 plants for each light',22)
    b+=text(36,152,'A · LEDs along the table above the air socks',22,AMBER)
    b+=table_plan(175)
    b+=text(36,365,'B · LEDs across the table at equal intervals',22,AMBER)
    b+=table_plan(390,True)
    b+=text(36,578,'A 200 mm inlet fan supplies each air sock.',21)
    b+=text(36,610,'Dashed lines = top lights. Gold lines = under-canopy LEDs.',19,MUTED)
    b+=text(36,659,'CROSS-SECTION · layout A',22,GREEN)
    b+=rect(84,684,566,40,'#274d38',GREEN,12)+text(367,711,'Continuous canopy',22,INK,'middle')
    b+=line(80,853,654,853,MUTED,4)
    for x in (114,334,554):
        b+=rect(x,827,52,26,SLAB,AMBER)+rect(x,775,52,52,SLAB,AMBER)
    for x in (249,469):
        b+=circle(x,819,33,'#304e43',GREEN)+text(x,826,'air',18,INK,'middle')
        b+=line(x-45,853,x-45,768,MUTED,2)+line(x+45,853,x+45,768,MUTED,2)
        b+=line(x-45,768,x+45,768,MUTED,2)
        b+=rect(x-7,760,14,6,AMBER,AMBER)+arrow(x,754,x,731,AMBER)
    b+=text(36,897,'Small LED bars in the center above each air sock.',21)
    b+=text(36,930,'Keep the fabric clear of the fixtures and their supports.',20,MUTED)
    f['clear-centre-layout']=plate('clear-centre-layout','Three-row slab layout and LED alternatives','Specified layout · the heights are not accurate',b,963,
        'Each table has three rows of seven slabs, with 63 plants for seven top lights and nine plants for each light. '
        'Two air socks with holes go between the rows, and a 200 mm fan supplies each air sock. '
        'Alternative A has two LED lines along the table above the air socks, and alternative B has bars across the table at equal intervals. '
        'The seven bars show the spacing and are not a specified number of fixtures. In the two alternatives, the LEDs send light up below the canopy. '
        'Install the fixtures on supports that do not touch the air socks. Examine the clearance of the inflated air socks. '
        'After you put seven slabs of 1 m on the table of 7.6 m, a space of 300 mm stays at each end. The dimensions and the light areas show the specified layout. '
        'Measure the light at the canopy and the airflow.')

    b=text(36,40,'SUPPLY, DRIPPER AND DISTRIBUTOR',22,GREEN)
    b+=rect(55,85,610,26,'#334139',MUTED)+text(360,73,'Lateral with pressure',21,anchor='middle')
    b+=line(145,111,145,142,BLUE,5)+rect(128,142,34,36,'#294d5d',BLUE,6)+text(195,165,'Pressure-compensating dripper',22)
    b+=line(145,178,145,230,BLUE,5)+line(145,230,325,230,BLUE,5)+line(325,230,325,270,BLUE,5)
    b+=text(365,237,'Microtube → distributor',21,BLUE)
    b+=rect(170,275,340,115,SLAB,AMBER)+text(550,319,'Block',21,AMBER)
    b+=line(212,270,465,270,BLUE,5)
    for x in (212,296,380,465): b+=line(x,270,x,310,BLUE,3)+arrow(x,312,x,339,BLUE)
    b+=text(36,440,'The distributor is only a symbol. Use a ring or stakes.',21)
    b+=text(36,474,'Examine the fit and the connections. Catch the total flow.',21,MUTED)
    f['dripper-delivery-chain']=plate('dripper-delivery-chain','Drip irrigation components','Component diagram',b,512,'The supply flows through the dripper and the microtube to a distributor on the block. The distributor in the drawing is a symbol. The number of outlets and the dimensions are different for different products. Examine the model of the ring or stake, the operating pressure and the fit on the block. Make sure that they agree with the documentation of the product. Measure the total output that each plant gets. <a href="#ref-19">[19]</a>')

    b=text(36,40,'COLLECT FOR THE SAME MEASURED TIME',22,GREEN)
    for x,label in [(125,'Near'),(345,'Middle'),(565,'Far')]:
        b+=line(x,74,x,119,BLUE,4)+arrow(x,120,x,158,BLUE)+rect(x-55,172,110,90,'#203d48',BLUE)
        for j in range(4):b+=line(x-55,188+j*17,x-38,188+j*17,MUTED)
        b+=text(x,295,label,22,anchor='middle')
    b+=text(36,344,'Record the mL at each outlet. Write the time of the test.',22)
    b+=text(36,392,'Example of shot time',24,GREEN,weight=700)
    b+=text(36,429,'7.35 L × 0.03 × 1,000 = 220.5 mL',24)
    b+=text(36,467,'220.5 ÷ (4,000 ÷ 3,600) ≈ 198 s = 3:18',23)
    b+=text(36,511,'4 L/h is an example total, measured for each plant.',20,MUTED)
    f['shot-volume-runtime']=plate('shot-volume-runtime','Dripper flow rate and irrigation time','Measure and calculate',b,546,'At typical outlets across the active zone, use vessels with labels and volume marks. Or use a container on a scale with the tare set. Compare the volumes that you collect in the same time at the operating pressure. The vessels in the drawing show where you collect the water. The shot time uses 220.5 mL and not a rounded value. It also uses a volume of 7.35 L for each plant. Replace the volume and the flow rate with values that you measure.')

    b='<defs><linearGradient id="slab-moisture-gradient" gradientUnits="userSpaceOnUse" x1="0" y1="95" x2="0" y2="290"><stop offset="0" stop-color="#766744"/><stop offset="1" stop-color="#376d87"/></linearGradient></defs>'
    b+=text(36,40,'SECTION · connected media that drain',21,GREEN)
    b+=rect(165,200,390,90,'url(#slab-moisture-gradient)',AMBER)+rect(288,95,126,105,'url(#slab-moisture-gradient)',AMBER)
    b+=plant(351,95)+roots(351,95,179,42)
    b+=arrow(251,105,251,184,BLUE)+text(36,115,'Block feed',20,BLUE)
    b+=arrow(440,182,440,246,BLUE)+text(473,167,'Water movement',19,BLUE)
    b+=arrow(410,95,410,52,GREEN)+text(452,70,'Plant uptake',19,GREEN)
    b+=line(152,295,592,295,MUTED,2,'6 5')+arrow(555,281,615,281,BLUE)+text(485,330,'Drain boundary',20)
    b+=text(36,372,'Color = water content, without numbers.',22)+text(36,406,'The colors show where there is more or less water.',21,MUTED)
    b+=text(36,452,'Water in the slab and outlet height change the profile.',21,AMBER)
    f['connected-water-column']=plate('connected-water-column','Block and slab water distribution','Cross-section without numbers',b,490,'Water moves between the block and the slab through their contact face. When the media drain, the top media can become drier and the slab can stay wet. The irrigation and the uptake also change the profile. The profile is different for different irrigation and drainage conditions. In its staged-drainage method, Grodan shows that water that the slab keeps changes the drying of the block. <a href="#ref-3">[3]</a>')

    sensor_caption = ('MT22: put the sensor into the long side of the slab, near the middle block and not below the block. '
        'The housing is 88 mm long, and it goes along the slab. The three rods of 53 mm go into the slab across its width, all at one height. '
        'Put the housing flat against the slab and hold the cable. The template gives centerline heights of 37.5 mm '
        'for a slab of 75 mm and 50 mm for a slab of 100 mm. The heights are from the bottom of the substrate. '
        'The heights are positions to compare, and you must make sure that they are correct in your facility. '
        '<a href="assets/slab-sensor/MT22-placement-template-A4-actual-size.pdf" target="_blank" rel="noopener">Get the A4 template of two pages</a>. '
        'Make a paper copy of the template at 100% (setting: "Actual size"). Measure the two scale bars. Make sure that each bar is 100 mm. Write the spacing of the pins of the sensor on the template. '
        '<a href="assets/slab-sensor/mt22-placement.svg" target="_blank" rel="noopener">Open the drawing at full size</a> · '
        '<a href="https://github.com/JakeTheRabbit/TDR-Sensor/blob/main/docs/PLACEMENT.md">Notes on the position of the TDR-Sensor</a> · '
        '<a href="assets/slab-sensor/LICENSE">AGPL-3.0 license</a>.')
    sensor_svg = (Path(__file__).parent / 'static/slab-sensor/mt22-placement.svg').read_text(encoding='utf-8')
    sensor_svg = sensor_svg.replace('id="arrow"', 'id="mt22-arrow"').replace('url(#arrow)', 'url(#mt22-arrow)')
    sensor_svg = sensor_svg.replace('id="wool"', 'id="mt22-wool"').replace('url(#wool)', 'url(#mt22-wool)')
    sensor_svg = sensor_svg.replace('<svg ', '<svg role="img" aria-labelledby="mt22-title mt22-desc" ', 1)
    sensor_svg = sensor_svg.replace('<defs>', '<title id="mt22-title">MT22 rockwool slab sensor position</title>'
        '<desc id="mt22-desc">Views from the top, the end and the side. Three rods go into the long side of the slab, '
        'near the middle block, in a horizontal direction. The long housing of the sensor goes along the length of the slab. Use the PDF to make a paper copy at 100%.</desc><defs>', 1)
    shell = plate('sensor-placement', 'MT22 sensor position and paper template', 'TDR-Sensor position drawing', '', 1100, sensor_caption)
    f['sensor-placement'] = re.sub(r'<svg.*?</svg>', lambda _: sensor_svg, shell, count=1, flags=re.S)

    f['slab-preparation']=steps('slab-preparation','Prepare the slab','Steps to prepare',[
        ('Examine surface and drainage','Examine the tray and the direction of the runoff.'),
        ('Saturate with the nutrient solution','Fill through the openings. Record the EC and the pH.'),
        ('Soak for the specified time','Obey the procedure of the slab manufacturer.'),
        ('Make the specified drainage opening','Position and stage change with the method.'),
        ('Put the block on the fiber','No plastic below the block. Examine the contact face.')],
        'Saturation gives water and nutrients at the same time. The staged-drainage method of Grodan uses a first opening above the seal, and then drainage openings below it. Select and record one procedure that you can use, and do not mix the openings of different procedures. <a href="#ref-2">[2]</a> <a href="#ref-3">[3]</a>')

    b=''
    for i,(label,depth) in enumerate([('Roots in block',76),('Roots at interface',121),('Roots in slab',158)]):
        x=38+i*231
        b+=text(x+95,20,label,21,GREEN,'middle',700)+rect(x,165,192,75,SLAB,AMBER)+rect(x+53,75,86,90,SLAB,AMBER)
        b+=plant(x+96,75)+roots(x+96,75,depth,15+i*12)
    b+=text(36,292,'The block–slab assembly is the same in all stages.',22)
    b+=text(36,328,'Examine roots, block water content and stable uptake.',21)
    b+=text(36,365,'The growth rate changes with the crop and conditions.',20,MUTED)
    f['rooting-in-progression']=plate('rooting-in-progression','Root growth from block into slab','Drawing of root growth',b,403,'The drawing shows the same assembly in three stages of root establishment. The roots are in continuous substrate. The drawing shows many roots because the example is a plant from a clone. The roots and the water uptake show when the crop can go to the cycle of each day for plants after root establishment.')

    # One reproducible synthetic daily example replaces three overlapping plots.
    events=[(2,6),(3,6),(4,6),(5,2),(7,2),(9,2)]
    samples=[(0,53),(2,50),(2,56),(3,55),(3,61),(4,60),(4,66),(5,64),(5,66),(7,64),(7,66),(9,64),(9,66),(12,62),(18,57),(24,53)]
    px=lambda h:90+h*23
    py=lambda v:297-(v-45)*6
    b=text(36,35,'EXAMPLE DAY · hours after lights-on',21,GREEN)
    for start,end,label,color in [(0,2,'P0','#2c4538'),(2,4,'P1','#304e43'),(4,9,'P2','#2c4538'),(9,24,'P3','#24352d')]:
        b+=rect(px(start),59,(end-start)*23,30,color,color)+text((px(start)+px(end))/2,80,label,18,INK,'middle')
    b+=rect(px(12),95,276,232,'#101a15','#101a15')
    for v in (45,55,65):b+=line(90,py(v),642,py(v),'#486152',1,'4 5')+text(75,py(v)+6,str(v),18,MUTED,'end')
    b+=text(36,125,'VWC',18)+text(36,148,'(%)',18)
    b+='<polyline points="'+' '.join(f'{px(h)},{py(v)}' for h,v in samples)+f'" fill="none" stroke="{GREEN}" stroke-width="3"/>'
    for h,_ in events:b+=line(px(h),103,px(h),120,BLUE,4)
    for h in (0,4,8,12,16,20,24):b+=text(px(h),350,str(h),18,MUTED,'middle')
    b+=text(90,385,'Light',20,AMBER)+text(px(12)+8,385,'Night',20,MUTED)
    b+=text(36,429,'P3 starts after the last irrigation, before lights-off.',21)
    b+=text(36,462,'In this paper, P3 stops at lights-on. Then P0 starts.',21)
    b+=text(36,503,'Blue lines = shots. The values are an example.',20,BLUE)
    f['p0-p1-p2-p3-states']=plate('p0-p1-p2-p3-states','Irrigation phases each day','Example VWC data',b,542,'An example of 24 hours, with a light period of 12 hours, shows the phases. P0 is the time from lights-on to the first irrigation. P1 fills the substrate again, and P2 keeps the VWC stable. P3 is the time from the last shot to the next lights-on. The total dryback between the irrigation windows includes P3 and the P0 after it. The values and the times are only an example.')

    f['crop-stage-arc']=steps('crop-stage-arc','Growth stages of the crop','Signals of the stage',[
        ('Vegetative stage, roots in slab','Roots in the slab. Uptake is stable.'),
        ('Flower set','Monitor the first flower sites and the stretch.'),
        ('Flower bulking','Slower stretch. Monitor flower growth.'),
        ('Examine the maturity','Use signals of the flower for the cultivar, and your records.')],
        'The time of each stage is different for different cultivars and growth conditions. Examine the maturity with signals of the flower and the records of the crop. The irrigation ranges are in the table for the growth stages. <a href="#ref-13">[13]</a> <a href="#ref-16">[16]</a>')

    b=text(36,38,'SIDE VIEW · all runoff from one slab',21,GREEN)+assembly(118)
    # Supply connects to every block; drain follows a different coloured path.
    b+=line(90,51,620,51,BLUE,4)
    for x in (187,367,547):b+=line(x-25,51,x-25,145,BLUE,3)
    b+=text(90,82,'Supply',19,BLUE)
    b+=line(65,285,665,285,AMBER,4)+line(65,255,65,285,AMBER,4)+line(665,255,665,340,AMBER,4)+line(665,340,604,340,AMBER,4)
    for x in (145,360,615):b+=arrow(x,246,x,278,AMBER)
    b+=rect(100,244,30,41,'#65786c',MUTED)+rect(520,244,30,41,'#65786c',MUTED)
    b+=text(80,324,'Slab above the runoff tray',20)
    b+=rect(562,348,82,95,'#203d48',BLUE)+arrow(604,339,604,367,AMBER)
    for j in range(4):b+=line(562,365+j*17,578,365+j*17,MUTED)
    b+=text(36,390,'All slab drainage → tray → outlet → container',21,AMBER)
    b+=text(36,476,'Runoff % = collected drain mL / applied mL × 100',22)
    b+=text(36,513,'Use the same slab and interval for the two values.',20,MUTED)
    f['measurement-runoff-layout']=plate('measurement-runoff-layout','Collect slab runoff','Setup diagram',b,552,'Three blocks are on one slab above a runoff tray. Gold shows how all the drainage flows to a container with volume marks, and blue shows the feed tubing. The positions of the slits are different for different products and drainage procedures. Catch all the drainage, and do not let the slab stay in the runoff in the tray. When you divide the slab totals by three, the result is an average and not a measurement for one plant. <a href="#ref-15">[15]</a>')

    f['ec-correction-finish']=steps('ec-correction-finish','EC measurements and nutrient changes','Sequence of measurements',[
        ('Find the type of EC measurement','Feed, runoff, bulk EC or pore-water EC estimate.'),
        ('Compare the readings','Same method, almost the same VWC, calibration and time.'),
        ('Examine irrigation and drainage','Examine supply, drainage, feed and crop water use.'),
        ('Record the change and the effect','Measure VWC, EC and runoff after the change.'),
        ('Record nutrient changes before harvest','Record products, concentrations and times.')],
        'The unit of EC is mS/cm, and the number is the same as the number in dS/m. The color of the solution is not an EC measurement. The bulk EC of a substrate sensor and an estimate of the pore-water EC are different quantities. The Fade procedure of Athena is only for the nutrient products in the procedure. <a href="#ref-18">[18]</a> <a href="#ref-17">[17]</a>')

    f['climate-demand-response']=steps('climate-demand-response','Water uptake along the table','Positions of measurement',[
        ('Measure at the correct positions','Light in the canopy, air conditions and the plant.'),
        ('Compare the substrate readings','Examine the VWC rate of change, supply and runoff.'),
        ('Compare the positions','Measure at the near, middle and far ends.'),
        ('Correct for the change you see','Stay in the set limits. Measure the result.')],
        'A climate that makes the plant use more water does not always give more uptake in a plant with stress. Use readings that you can compare before you change the irrigation. For air tubes with holes, measure the static pressure and the air movement at positions that you can measure again. In this example, no data show that a second tube is better.')

    f['troubleshooting-ladder']=steps('troubleshooting-ladder','Irrigation fault checks','Sequence for diagnosis',[
        ('Wilt in one plant','Do a catch test of its outlet. Examine block and roots.'),
        ('High runoff, VWC does not increase','Examine flow around block, drainage and probe.'),
        ('EC increases','Compare the same EC method. Examine feed and runoff.'),
        ('Different readings','Examine the position, the calibration and the supply.'),
        ('Correct the fault that you find','Examine the result. Record the correction.')],
        'A symptom can have some causes. Repair an outlet that does not operate, and correct sudden plant stress immediately. After you select a change of steering, monitor the result for one light cycle. Do not wait one day to correct a fault that you know.')

    b=text(36,43,'Electrical input → heat in the room',25,GREEN,weight=700)
    b+=text(36,102,'BTU/h = watts × 3.412',30)+text(36,157,'800 W ≈ 2,730 BTU/h',30,AMBER)
    b+=text(36,215,'Boundary: electrical energy that stays in the room.',20)
    b+=text(36,255,'Circulation moves heat.',22)+text(36,290,'Cooling or exhaust removes heat at that boundary.',21)
    f['room-heat']=plate('room-heat','Electrical input and room heat','Calculated heat equivalent',b,331,'The conversion is correct if all of the electrical input stays in the room as heat. If drivers are not in the room, or if energy leaves the room, calculate these quantities in a different step. The number of fans does not give the change of the leaf temperature.')
    return f


FIGURES = {key: value for key, value in figures().items() if key not in {
    'slab-preparation', 'crop-stage-arc', 'ec-correction-finish',
    'climate-demand-response', 'troubleshooting-ladder', 'room-heat',
}}
