---
slug: "facility-3d"
title: "Designing a grow facility in 3D before you build it"
eyebrow: "Facility · Design"
summary: "Lay out rooms, equipment and airflow in a 3D model on your screen, and catch the expensive mistakes before anyone pours concrete."
track: "Facility & quality"
read_time: "~14 min read"
diagrams: "11 diagrams"
related: ["airflow-design", "grow-room-systems", "f2-crop-steering"]
url: "https://jaketherabbit.github.io/cannabis-white-papers/facility-3d.html"
md_url: "https://jaketherabbit.github.io/cannabis-white-papers/papers/facility-3d.md"
version: "1.0"
updated: "2026-06-24"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "threejs-repo", "n": 1, "cite": "mrdoob and contributors. three.js, JavaScript 3D Library [WebGL/WebGPU scene-graph rendering library]. GitHub repository (MIT License). Accessed 2026-06-22.", "url": "https://github.com/mrdoob/three.js/", "peer": false}, {"id": "kitaya-2003-air-current-gas-exchange", "n": 2, "cite": "Kitaya, Y., Tsuruyama, J., Shibuya, T., Endo, M., & Yoshida, M. (2003). Effects of air current speed on gas exchange in plant leaves and plant canopies. Advances in Space Research, 31(1), 177–182. DOI:10.1016/S0273-1177(02)00747-0", "url": "https://doi.org/10.1016/S0273-1177(02)00747-0", "peer": true}, {"id": "kimura-2020-leaf-boundary-layer", "n": 3, "cite": "Kimura, K., Yasutake, D., Yamanami, A., & Kitano, M. (2020). Spatial examination of leaf-boundary-layer conductance using artificial leaves for assessment of light airflow within a plant canopy under different controlled greenhouse conditions. Agricultural and Forest Meteorology, 280, 107773. DOI:10.1016/j.agrformet.2019.107773", "url": "https://doi.org/10.1016/j.agrformet.2019.107773", "peer": true}, {"id": "ibc-2024-1011-5-2-stairs", "n": 4, "cite": "International Code Council (2024). 2024 International Building Code (IBC), Section 1011.5.2, Riser height and tread depth (stair riser 7 in. max / 4 in. min; rectangular tread 11 in. min).", "url": "https://codes.iccsafe.org/s/IBC2024P1/chapter-10-means-of-egress/IBC2024P1-Ch10-Sec1011.5.2", "peer": false}, {"id": "wac-314-55-083-cannabis-security", "n": 5, "cite": "Washington State Liquor and Cannabis Board. WAC 314-55-083, Security and traceability requirements for cannabis licensees (surveillance of all entrances/exits, processing/storage/destruction areas and POS; min. 640x470 resolution; min. 10 fps; recordings retained >=45 days; storage device secured against tampering/theft).", "url": "https://app.leg.wa.gov/wac/default.aspx?cite=314-55-083", "peer": false}]
---

# Designing a grow facility in 3D before you build it

_Facility · Design · ~14 min read_

> Lay out rooms, equipment and airflow in a 3D model on your screen, and catch the expensive mistakes before anyone pours concrete.

## What 3D facility planning is (and why it beats a paper plan)

A grow facility is a building full of rooms, equipment, airflow paths and security cameras. The usual way to plan one, a flat top-down architect's drawing, can only really be read by experts. A **3D model** is the same plan rebuilt on your screen as a thing you can rotate, zoom into and click on, so investors, electricians, inspectors and staff all understand it instantly.

Describe the building as data instead of drawing it. You write a data file, a plain list of rooms and their dimensions, and let code draw the building from that data. Re-planning the facility for the next harvest then becomes nothing more than editing some numbers. The worked example throughout this paper is a real two-storey licensed cultivation facility measuring 14.8 by 16.7 metres.

- A 3D model makes spatial relationships visible: airflow paths, camera sightlines, bench density, and where the ducts and drains run.
- It is built with Three.js, a free web library, so the whole thing is one HTML file that opens in any browser with nothing to install.[^threejs-repo]
- Because the floor plan is a data file, asking ‘what if we fit a fourth bench?’ means editing a list, not redrawing the building.
- The same model serves four jobs at once: a design tool, a compliance exhibit for licensing, a staff training aid, and a live monitoring dashboard.

> **Diagram.** The same facility, two ways to read it. The 3D view does not replace the architect's drawing. It makes that drawing legible to everyone else.

## Key terms, defined from zero

Here is the vocabulary. None of these need prior knowledge. They are the words this topic keeps using. Read this once and the rest of the paper reads easily.

**3D model** — A picture of the building you can rotate, zoom and click on a screen. Not a fixed photo, but a thing you move around.

**Three.js** — A free code library that draws 3D scenes inside an ordinary web browser, with nothing to install.

**Floor plan** — The architect's flat, top-down drawing of walls, doors and rooms.

**Render / scene** — To ‘render’ is to draw the picture. The ‘scene’ is everything in the model: walls, benches, lights, cameras.

**JSON / data file** — A plain list of facts, room names, sizes and positions, that the code reads to build the model.

**FOV cone** — ‘Field of view’ cone: a see-through wedge showing exactly what one camera can see, so blind spots show up as floor with no tint.

**Fit-out** — The equipment and furniture added to a bare room: benches, lights, dehumidifiers, CO₂ cylinders.

**Digital twin** — A 3D model wired to live sensors, so it shows the real, current temperature and humidity of each room.

## Model the building as data, not as a drawing

**Do not draw the building by hand in code.** This is the single most important decision in the whole approach. Describe it as data, and let the code interpret that data into geometry. The reference schema, the shape of the data file, needs only four kinds of record to capture almost any grow building.

Each **room** is stored as a rectangle, `[x, y, width, depth]` in metres. Each **wall** is a centre-line with openings positioned by how far along the run they sit, and a single global wall thickness (0.15 m) avoids a whole class of typos. Everything uses one unit equals one metre, so the millimetre numbers on the architect's plan (4800, 9200) are divided by 1000 once, at data-entry time, and never thought about again.

> **KEY — The four record types**
> 
> - **Rooms**: an interior footprint rectangle in metres.
> - **Walls**: a centre-line with openings (doors, the 4.6 m roller door, pass-throughs) placed by distance along the run.
> - **Equipment**: benches, dehumidifiers, AC heads, CO₂ tanks.
> - **Devices**: cameras, sirens, safes, network and power racks.

Doors, the roller door and pass-throughs are all the _same_ thing: an ‘opening’ on a wall, with a width and a head (top) height. That sameness keeps the data file short. Because the model is data, it survives every re-plan. You edit numbers, not geometry.

> **Diagram.** The four record types, with the key fields each one carries. Roughly 25 wall rows describe the entire reference building's envelope and partitions.

> **Diagram.** Because all three views read the same numbers, fixing a dimension once fixes it everywhere.

## Building the shell: floors, walls, openings and stairs

Code builds the physical shell from the data: the floors, walls and stairs. **Floor slabs** are flat 2D shapes ‘extruded’ (pushed up) into thickness, and they can include holes. You need a hole for the void where the stairwell drops through. Each **wall run** is split by its openings into solid segments, with a lintel (a short beam) filling the gap above each door.

**Stairs** are a loop of step-shaped boxes. The reference building climbs 3.25 m over a 4.5 m run as 16 steps of 203 mm each. Drawing the stair this way doubles as a buildability check: if the steps don't fit the space at a sensible riser height, you find out now, on screen, not on site. Standard building codes cap a stair riser at about 178 mm (7 inches) with a tread of at least 279 mm (11 inches), so a 203 mm riser flags as steep and tells you to lengthen the run.[^ibc-2024-1011-5-2-stairs]

- Floor slabs are extruded shapes that can carry holes for stairwells and service voids.
- A wall is a centre-line plus openings; openings split it into segments with lintels above. No complex geometry needed.
- Each storey gets its own group, so switching floors just hides one and shows the other (its labels hide automatically too).
- Details like the corrugated roller-door texture come from about 10 lines of code, with no image files.

> **Diagram.** One wall run, read left to right. The opening's ‘at’ value is simply how far along the wall it starts.

| Check | Value | Verdict |
| --- | --- | --- |
| Total rise | 3.25 m | fixed by the two floor heights |
| Horizontal run | 4.5 m | the space allotted on the plan |
| Risers | 16 × 203 mm | steep, over the 178 mm code max |
| Treads | 281 mm | comfortable, above the 279 mm min |
| Fit | Fits the 4.5 m run | OK, but lengthen run to ease the riser |

*A stair sanity-check the model performs for free. The 203 mm riser is buildable but steep against code minimums[^ibc-2024-1011-5-2-stairs], a prompt to revisit it early.*

## Fit-out: benches, plants, climate gear and airflow

**Fit-out** turns a generic building into a grow facility, and every piece is built from simple shapes. No modelling software required. The reference flower rooms use 1.2 by 7.6 m rolling benches, three per room, giving 27.4 m² of canopy in a 44 m² room: about 62% of the floor, a number the model shows at a glance.

Plants are the highest-count object, 210 of them here, so they are ‘instanced’, meaning drawn in one batch rather than one at a time. That single trick is the biggest performance lever in the whole model. The climate gear (dehumidifiers, carbon filter/fan units hung at 2.45 m, mini-split AC heads, CO₂ cylinders) each get a tiny builder, sized straight from the datasheet.

Moving air thins the still ‘boundary layer’ of humid air that clings to each leaf, which is what lets the leaf actually exchange water vapour and CO₂ with the room[^kitaya-2003-air-current-gas-exchange]. The plan's target of 3500 m³/h of horizontal airflow per flower room is drawn as toggleable arrows that an HVAC contractor reads instantly. Modest, even air movement across the canopy keeps that boundary-layer conductance high and uniform. Too little leaves dead spots, too much can close stomata[^kimura-2020-leaf-boundary-layer].

> **Diagram.** The model surfaces canopy density automatically. You never measure it by hand. 62% is a healthy, walkable density for a flower room.

> **Diagram.** Airflow shown as a top-down loop. Drawing it makes the air path visible to contractors and inspectors, and reveals where benches would stall the flow.[^kitaya-2003-air-current-gas-exchange]

| Item | Built from | Count |
| --- | --- | --- |
| Rolling bench | Box + leg rails, 1.2 × 7.6 m | 9 (3 per flower room) |
| Dehumidifier | Box + grille face | 7 |
| Carbon filter / fan | Cylinder + duct, hung at 2.45 m | 10 |
| AC head (mini-split) | Flattened box above doors | 8 |
| CO₂ cylinder | Capped cylinder, floor-standing | 6 |

*The equipment schedule. Each item is a small reusable builder, and placing them in 3D reveals clashes early: a filter over an aisle, an AC head fouling a door.*

> **TIP — Clashes you only see in 3D**
> 
> A flat plan hides height. In 3D you immediately catch a carbon filter hung at 2.45 m over a walkway, an AC head sitting above a door swing, or a dehumidifier that lands on a bench. Pair this with the [airflow design](airflow-design.html) paper to size the fans before you place them.

## The security and compliance layer you can actually see

Licensed cultivation is audited on its **security plan**, and modelling that layer turns a paper checklist into something you can walk an inspector through. Each camera gets a translucent **FOV cone**: its length is the usable range, its width is the lens angle. Blind spots show up as floor with no tint at all.

Cannabis security rules are jurisdiction-specific, but they are concrete: a typical regime requires surveillance of every entrance, exit, and processing, storage and destruction area, at a minimum resolution and frame rate, with recordings retained for weeks[^wac-314-55-083-cannabis-security]. Modelling the cameras as cones lets you prove that coverage visually instead of arguing it from a list. The reference facility models roughly 22 cameras (20 bullet, 1 doorbell, 1 PTZ), 16 sirens, 2 floor-bolted drug safes, a walk-in vault (the drying room itself), and the PoE/UPS racks (three 6U plus one 13U) that keep it all powered.

- Camera cones answer licensing questions visually: do three flower-room cameras cover all three benches? Does the hallway pair leave a lobby gap?
- Blind spots appear as un-tinted floor, far easier to spot than reading a coverage list.
- Sirens, safes, the vault and the network/power racks are all modelled, because cable runs and UPS placement are part of the security story.
- One checkbox shows or hides the whole security layer: audit mode versus tour mode.
- The roof PTZ camera's 70°, 12 m cone is checked against the upper open-plan office for intrusion coverage.

> **Diagram.** Top-down camera coverage. Any floor outside every cone is a blind spot. Here, a gap between cameras 2 and 3 that re-aiming closes.[^wac-314-55-083-cannabis-security]

| Device | Count | Placement logic |
| --- | --- | --- |
| Cameras | 22 (20 bullet, 1 doorbell, 1 PTZ) | Every entrance, exit and grow/process area |
| Sirens | 16 | Audible coverage of all occupied zones |
| Drug safes | 2 | Floor-bolted, inside monitored rooms |
| Walk-in vault | 1 | The drying room doubles as secured storage |
| PoE + UPS racks | 3 × 6U + 1 × 13U | Short cable runs; power survives an outage |

*The device schedule and why each sits where it does. Cable runs and UPS placement are modelled because they are part of what an auditor checks.[^wac-314-55-083-cannabis-security]*

## A step-by-step path from plan to clickable model

Here is the practical order of work, with nothing skipped. The whole thing is one HTML file, a JSON block, and roughly 600 lines of generator code, small enough to lift straight from a reference document and adapt.

1. **Read the dimension chains** — Off the architect's plan, read the chains (e.g. 4800 + 4632.40 + 4800 across the top) and divide every millimetre figure by 1000 to get metres.
2. **Transcribe to JSON** — Enter rooms, walls, equipment and devices into the four-record schema. This is the real work, and it becomes your single source of truth.
3. **Build the shell** — Run the shell builders: floor slabs, walls with openings and lintels, then the stairs (which also sanity-check themselves).
4. **Add the fit-out** — Run the fit-out builders: benches, instanced plants, and climate gear sized from datasheets.
5. **Add the security layer** — Place cameras with their FOV cones, sirens, safes, the vault and the racks; group them under one toggle.
6. **Add interaction** — An orbit camera plus a one-click top view that reproduces the 2D plan, and click-to-inspect so each room and device reports its own contents.

> **NOTE — Reuse is copy-and-replace**
> 
> To start a new facility, save the page, copy the importmap and script block, and replace the data tables with your own plan. The generator code does not change. Only the numbers do.

## Common pitfalls and how to dodge them

Most mistakes come from a handful of repeatable errors. The biggest by far is modelling in code instead of in data. Do that and every re-plan becomes painful, because you have thrown away your single source of truth. The rest are rendering details that are easy to fix once you know them.

| Pitfall | The fix |
| --- | --- |
| Modelling in code, not data | Keep the building in the JSON schema and let code only interpret it. This is the cardinal rule. |
| One real light per grow fixture | 14 shadow-casting lights kill the frame rate. Use one directional ‘sun’ plus emissive (glowing) surfaces. |
| Pure-white walls blow out | Under ACES tone mapping, white clips. Use a warm off-white (0xe8e6e0) at high roughness. |
| Shadow camera too big | An oversized shadow camera makes mushy shadows. Size it to the building, not the world. |
| Picking against the whole scene | Users accidentally select walls. Raycast a curated ‘pickables’ list instead. |
| Forgetting wall thickness as a global | Set thickness once (0.15 m) and reuse it. This removes a whole class of typos. |

*Six common pitfalls and the recommended fix for each. The first one is the only one that costs you weeks. The rest cost minutes.*

> **WARN — The cardinal sin, restated**
> 
> Remember one thing: the moment you start hand-placing geometry in code, you have lost the ability to re-plan cheaply. Every ‘what if’ then means re-coding instead of re-typing a number.

## What 3D planning realistically gets you, and what it does not

Set expectations honestly. This kind of model is light and fast: the reference demo draws a full two-storey facility, about 450 meshes plus instanced plants, at 60 frames per second on integrated graphics, and scales to whole campuses by instancing and merging geometry while keeping draw calls under about 300.

Simple shapes carry you surprisingly far. You only reach for a proper modelling tool (Blender, exported as glTF) when you need a single photoreal ‘hero’ asset. The model is a planning, compliance and monitoring aid. It is **not** a structural-engineering or code-compliance sign-off. The airflow and security targets it visualises still need a qualified professional to validate.

> **Diagram.** A capability ladder. Most facilities never need to climb past the first rung for planning.

| Budget | Target | Why |
| --- | --- | --- |
| Meshes | ~450 | A full two-storey facility shell + fit-out |
| Frame rate | 60 fps | Smooth on integrated graphics |
| Draw calls | < 300 | Keeps low-end laptops and tablets usable |
| Pixel ratio | capped at 2 | Stops 4K screens overworking the GPU |
| Shadow lights | 1 | One sun; the rest are emissive surfaces |

*The performance budget. Hit these and the model stays smooth almost anywhere. The 60-fps figure is a reproduce-to-verify benchmark, not a guarantee for every machine.*

> **KEY — What it is, and what it is not**
> 
> A 3D facility model is a design tool, a compliance exhibit, a training aid and, wired to sensors, a live dashboard. It is not an engineering sign-off. Treat every airflow, structural and security target it shows as something to confirm with a professional, not as approved.

Start with primitives, get your plan into data, and the model pays for itself the first time it catches a clash before construction. From here, read the [grow-room systems](grow-room-systems.html) paper to see what fills each room, or the [irrigation manual](irrigation-manual.html) for wiring the model to live irrigation data.

## References

[^threejs-repo]: mrdoob and contributors. three.js, JavaScript 3D Library [WebGL/WebGPU scene-graph rendering library]. GitHub repository (MIT License). Accessed 2026-06-22. https://github.com/mrdoob/three.js/ (industry/manufacturer source)
[^kitaya-2003-air-current-gas-exchange]: Kitaya, Y., Tsuruyama, J., Shibuya, T., Endo, M., & Yoshida, M. (2003). Effects of air current speed on gas exchange in plant leaves and plant canopies. Advances in Space Research, 31(1), 177–182. DOI:10.1016/S0273-1177(02)00747-0 https://doi.org/10.1016/S0273-1177(02)00747-0 (peer-reviewed)
[^kimura-2020-leaf-boundary-layer]: Kimura, K., Yasutake, D., Yamanami, A., & Kitano, M. (2020). Spatial examination of leaf-boundary-layer conductance using artificial leaves for assessment of light airflow within a plant canopy under different controlled greenhouse conditions. Agricultural and Forest Meteorology, 280, 107773. DOI:10.1016/j.agrformet.2019.107773 https://doi.org/10.1016/j.agrformet.2019.107773 (peer-reviewed)
[^ibc-2024-1011-5-2-stairs]: International Code Council (2024). 2024 International Building Code (IBC), Section 1011.5.2, Riser height and tread depth (stair riser 7 in. max / 4 in. min; rectangular tread 11 in. min). https://codes.iccsafe.org/s/IBC2024P1/chapter-10-means-of-egress/IBC2024P1-Ch10-Sec1011.5.2 (industry/manufacturer source)
[^wac-314-55-083-cannabis-security]: Washington State Liquor and Cannabis Board. WAC 314-55-083, Security and traceability requirements for cannabis licensees (surveillance of all entrances/exits, processing/storage/destruction areas and POS; min. 640x470 resolution; min. 10 fps; recordings retained >=45 days; storage device secured against tampering/theft). https://app.leg.wa.gov/wac/default.aspx?cite=314-55-083 (industry/manufacturer source)
