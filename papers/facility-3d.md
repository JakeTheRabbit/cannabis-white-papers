---
slug: "facility-3d"
title: "A 3D model of a grow facility before construction"
eyebrow: "Facility · Layout"
summary: "With a 3D model on your screen, you can find errors that have a high cost before construction starts. The model shows the rooms, the equipment and the airflow."
track: "Facility and quality"
read_time: "~14 min to read"
diagrams: "11 diagrams"
related: ["airflow-design", "grow-room-systems", "f2-crop-steering"]
url: "https://www.growlabs.nz/wiki/facility-3d.html"
md_url: "https://www.growlabs.nz/wiki/papers/facility-3d.md"
version: "1.2"
updated: "2026-07-18"
license: "CC BY-NC 4.0"
license_url: "https://creativecommons.org/licenses/by-nc/4.0/"
attribution: "The Cannabis White Papers"
refs: [{"id": "threejs-repo", "n": 1, "cite": "mrdoob and contributors. three.js, JavaScript 3D Library [WebGL/WebGPU scene-graph rendering library]. GitHub repository (MIT License). Accessed 2026-06-22.", "url": "https://github.com/mrdoob/three.js/", "peer": false}, {"id": "kitaya-2003-air-current-gas-exchange", "n": 2, "cite": "Kitaya, Y., Tsuruyama, J., Shibuya, T., Endo, M., & Yoshida, M. (2003). Effects of air current speed on gas exchange in plant leaves and plant canopies. Advances in Space Research, 31(1), 177–182. DOI:10.1016/S0273-1177(02)00747-0", "url": "https://doi.org/10.1016/S0273-1177(02)00747-0", "peer": true}, {"id": "kimura-2020-leaf-boundary-layer", "n": 3, "cite": "Kimura, K., Yasutake, D., Yamanami, A., & Kitano, M. (2020). Spatial examination of leaf-boundary-layer conductance using artificial leaves for assessment of light airflow within a plant canopy under different controlled greenhouse conditions. Agricultural and Forest Meteorology, 280, 107773. DOI:10.1016/j.agrformet.2019.107773", "url": "https://doi.org/10.1016/j.agrformet.2019.107773", "peer": true}, {"id": "ibc-2024-1011-5-2-stairs", "n": 4, "cite": "International Code Council (2024). 2024 International Building Code (IBC), Section 1011.5.2, Riser height and tread depth (stair riser 7 in. max / 4 in. min; rectangular tread 11 in. min).", "url": "https://codes.iccsafe.org/s/IBC2024P1/chapter-10-means-of-egress/IBC2024P1-Ch10-Sec1011.5.2", "peer": false}, {"id": "wac-314-55-083-cannabis-security", "n": 5, "cite": "Washington State Liquor and Cannabis Board. WAC 314-55-083, Security and traceability requirements for cannabis licensees (surveillance of all entrances/exits, processing/storage/destruction areas and POS; min. 640x470 resolution; min. 10 fps; recordings retained >=45 days; storage device secured against tampering/theft).", "url": "https://app.leg.wa.gov/wac/default.aspx?cite=314-55-083", "peer": false}]
---

# A 3D model of a grow facility before construction

_Facility · Layout · ~14 min to read_

> With a 3D model on your screen, you can find errors that have a high cost before construction starts. The model shows the rooms, the equipment and the airflow.

## Purpose and scope

> **NOTE: Jurisdiction**
>
> Examples of security and exit in this paper can refer to US regulations (WAC and IBC). These regulations are only examples. The correct building codes and license regulations are those of the jurisdiction that will do the inspection of your facility.

A grow facility is a building with rooms, equipment, airflow and security cameras. The usual document for a facility is the floor plan, a flat drawing from above that an architect makes. Only experts can read a floor plan easily. A **3D model** is the same floor plan on your screen. You can turn it, make it larger or smaller, and select parts of it. Thus investors, electricians, inspectors and personnel can read it immediately.

Write the building as data and do not make a drawing of it. You write a data file with a list of the rooms and their dimensions. The software code makes the building from this data. To change the layout of the facility for the next harvest, you only change some numbers.The example in this paper is a cultivation facility with a license and with two floors. The size is 14.8 by 16.7 m (48.6 by 54.8 ft).

- A 3D model shows the position of the objects in relation to each other. It shows the direction of the airflow, the area that each camera can see, and the density of the benches. It also shows the position of the ducts and the drains.
- The model uses Three.js, a library for the web with no cost. All of the model is one HTML file that you can use in each browser. Other software is not necessary.[^threejs-repo]
- The floor plan is a data file. Thus, to find the effect of a fourth bench, you change a list. You do not make the drawing of the building again.
- The same model does four tasks at the same time. It is a tool for the layout and a document of compliance for the license. It is also an aid for the training of personnel and a dashboard with current data.

> **Diagram.** The same facility, in a drawing and in a model. The 3D model does not replace the drawing of the architect. It makes the information of the drawing easy to read for all other persons.

## Definitions

This section gives the terms of this paper. It is not necessary to know these terms before you read this paper. These terms occur many times in this paper. Read this section one time. Then the remaining part of this paper is easy to read.

**3D model**: A model of the building on a screen. You can turn it, make it larger or smaller, and select parts of it. The model does not stay in one view. You can move in the model.

**Three.js**: A software library with no cost that makes 3D scenes in a web browser. Other software is not necessary.

**Floor plan**: The flat drawing of the walls, doors and rooms that an architect makes. It shows the building from above.

**Render and scene**: To ‘render’ is to show the model on the screen. The ‘scene’ is all of the objects in the model: walls, benches, lights and cameras.

**JSON data file**: A file with a list of data: the names, sizes and positions of the rooms. The software code reads this file to make the model.

**FOV cone**: The ‘field of view’ cone. It is a transparent cone that shows the area that one camera can see. Thus an area of the floor with no color is a blind spot.

**Fit-out**: The equipment that you add to an empty room, for example benches, lights, dehumidifiers and CO₂ cylinders.

**Digital twin**: A 3D model with a connection to sensors. It shows the current temperature and humidity of each room.

## Building model from data

**Do not make the building manually in software code.** This decision is the most important decision of this method. Write the building as data, and let the software code make the geometry from the data. The reference schema, the structure of the data file, has only four types of record. Thus it can show almost all buildings for cultivation.

The data file shows each **room** as a rectangle, `[x, y, width, depth]` in meters. It shows each **wall** as a centerline with openings. The position of an opening is its distance along the wall.One wall thickness of 0.15 m (5.9 in) for all walls prevents many errors when you write the data. All values use one unit: one unit is one meter. Thus you divide the millimeter values on the floor plan of the architect (4800, 9200) by 1000 one time, when you write the data. You do not do this again.

> **KEY: The four types of record**
>
> - **Rooms**: a rectangle for the inner floor area, in meters.
> - **Walls**: a centerline with openings (doors, the roller door of 4.6 m (15.1 ft), and pass-through openings) at a distance along the wall.
> - **Equipment**: benches, dehumidifiers, AC heads and CO₂ tanks.
> - **Devices**: cameras, sirens, safes, and racks for the network and for power.

Doors, the roller door and pass-through openings are all the _same_ type of object, an ‘opening’ in a wall. An opening has a width and a head height (the height of the top). Thus the data file is short. Because the model is data, it stays correct when you change the layout. You change numbers, and you do not change geometry.

> **Diagram.** The four types of record, with the primary fields of each type. Approximately 25 wall rows show the full envelope and the partitions of the reference building.

> **Diagram.** All three read the same numbers. Thus, when you correct a dimension one time, it is correct in all three.

## The shell of the building: floors, walls, openings and stairs

The software code makes the shell of the building from the data: the floors, the walls and the stairs. **Floor slabs** are flat 2D shapes. The code ‘extrudes’ each shape (it gives the shape a thickness), and a shape can have holes. You must make a hole for the void of the stairwell. The openings divide each **wall run** into solid parts. A lintel (a short beam) fills the space above each door.

**Stairs** are a sequence of boxes in the shape of steps. In the reference building, the stairs have a total height of 3.25 m (10.7 ft) and a run of 4.5 m (14.8 ft). They have 16 steps of 203 mm (8 in) each. The model also checks the stairs before construction.If the space is not sufficient for steps with a correct riser height, you see this on the screen and not on the site. The usual building codes give a maximum of approximately 178 mm (7 in) for a riser and a minimum of 279 mm (11 in) for a tread. Thus a riser of 203 mm (8 in) is too high, and it shows that you must make the run longer.[^ibc-2024-1011-5-2-stairs]

- Floor slabs are extruded shapes. They can have holes for stairwells and for service voids.
- A wall is a centerline with openings. The openings divide the wall into parts, with lintels above them. Only boxes are necessary.
- The model has one group of objects for each floor. When you change floors, the model shows one floor and does not show the other floor. The labels of the other floor also do not show.
- Approximately 10 lines of software code make small parts, for example the corrugated texture of the roller door. Image files are not necessary.

> **Diagram.** One wall run, from left to right. The ‘at’ value of an opening is the distance along the wall at which the opening starts.

| Check | Value | Result |
| --- | --- | --- |
| Total height | 3.25 m (10.7 ft) | The two floor heights give this value |
| Horizontal run | 4.5 m (14.8 ft) | the space in the floor plan |
| Risers | 16 × 203 mm (8 in) | Too high. More than the maximum of 178 mm in the building code. |
| Treads | 281 mm (11.1 in) | Good. More than the minimum of 279 mm. |
| Fit | Correct for the run of 4.5 m | Correct. But make the run longer to decrease the riser height. |

*The model does this check of the stairs automatically. The riser of 203 mm is possible, but it is too high compared with the values in the building code[^ibc-2024-1011-5-2-stairs]. This result is a signal to examine the riser at the start.*

## Facility fit-out and airflow

**Fit-out** changes a building into a grow facility. You make each object from easy shapes. Special software is not necessary.The reference flower rooms have three rolling benches in each room. Each bench is 1.2 by 7.6 m (3.9 by 24.9 ft). The canopy area is 27.4 m² (295 ft²) in a room of 44 m² (474 ft²), which is approximately 62% of the floor. The model shows this number immediately.

The plants are the objects with the highest number, 210 in this model. Thus the model uses ‘instancing’: the software renders all the plants in one batch and not one at a time. This method is the most important method to make the model operate quickly. The climate equipment (dehumidifiers, carbon filter and fan units hung at 2.45 m (8.0 ft), mini-split AC heads and CO₂ cylinders) has a small builder for each item. Each builder uses the size from the datasheet.

Each leaf releases water vapor and absorbs CO₂ all the time. In air that does not move, the layer of air at the surface of the leaf quickly has the maximum moisture and less CO₂. This thin film prevents more gas exchange with the air around it, also in a cool room. This film is the leaf boundary layer: a thin layer of air that does not move. The transpiration of the leaf makes this air different.[^kitaya-2003-air-current-gas-exchange]Air that moves removes this film and replaces it with new air from the room. The air movement makes the gradient for gas exchange again.The floor plan has a target of 3500 m³/h of horizontal airflow for each flower room. The model shows this airflow as arrows that you can show or not show, and an HVAC contractor reads them immediately. A small and equal movement of air across the canopy keeps the conductance of the boundary layer high and equal. If the movement is too small, areas where the air does not move occur. If the movement is too large, the stomata can close.[^kimura-2020-leaf-boundary-layer]

> **Diagram.** The model shows the canopy density automatically, and you do not measure it manually. 62% is a good density for a flower room. It lets personnel walk in the room.

> **Diagram.** The figure shows the airflow as a loop, seen from above. When you show the airflow, contractors and inspectors can see the direction of the air, and you can find where the benches stop the flow.[^kitaya-2003-air-current-gas-exchange]

| Item | Made from | Number |
| --- | --- | --- |
| Rolling bench | Box and leg rails, 1.2 × 7.6 m (3.9 × 24.9 ft) | 9 (3 for each flower room) |
| Dehumidifier | Box and grille | 7 |
| Carbon filter and fan | Cylinder and duct, hung at 2.45 m (8.0 ft) | 10 |
| AC head (mini-split) | Flat box above the doors | 8 |
| CO₂ cylinder | Closed cylinder, on the floor | 6 |

*The list of equipment. Each item has a small builder that you can use again. When you put the items in 3D, you find clashes at the start. Examples are a filter above an aisle or an AC head that touches the door when it moves.*

> **TIP: Clashes that you can see only in 3D**
>
> A flat floor plan does not show height. In 3D you see immediately a carbon filter hung at 2.45 m (8.0 ft) above a walkway. You also see an AC head above the area where a door moves, or a dehumidifier in the same position as a bench. Use the [airflow design](airflow-design.html) paper to find the size of the fans before you put them in the model.

## Security and compliance controls that you can see

An auditor examines the **security plan** of a cultivation facility with a license. When you put this layer in the model, a checklist on paper becomes a model that you can show to an inspector. Each camera has a transparent **FOV cone**. The length of the cone is the range of the camera, and the width of the cone is the angle of the lens. An area of the floor with no color is a blind spot.

The security regulations for cannabis are different in each jurisdiction. For example, typical regulations make surveillance necessary for each entrance, exit, and area for processing, storage and destruction. They also give a minimum resolution and frame rate for the cameras. The video records must stay in storage for some weeks.[^wac-314-55-083-cannabis-security]When you show the cameras as cones, you can show visually that the cameras see all necessary areas. A list is not necessary for this.The model of the reference facility has approximately 22 cameras (20 bullet cameras, 1 doorbell camera and 1 PTZ camera), 16 sirens and 2 drug safes attached to the floor. It also has a walk-in vault (this vault is the drying room) and the PoE and UPS racks (three racks of 6U and one rack of 13U). The racks supply power to all of this equipment.

- Camera cones give a visual check for the license. The cones show if the three cameras in a flower room can see all three benches. They also show if there is an area of the lobby that the two cameras in the hallway do not see.
- A blind spot is an area of the floor with no color. You find it much more easily than in a list of the areas that the cameras see.
- The model has the sirens, the safes, the vault and the racks for the network and for power. The cable routing and the position of the UPS are a part of the security plan, and thus the model shows them.
- One checkbox shows or does not show all of the security layer. The checkbox gives audit mode or tour mode.
- The model compares the cone of the PTZ camera on the roof (70°, 12 m (39 ft)) with the office on the top floor, which has no partitions. It shows if the camera can see an intruder.

> **Diagram.** The camera cones, seen from above. An area of the floor that is not in a cone is a blind spot. Here, there is a gap between cameras 2 and 3, and the gap closes when you point the cameras in a new direction.[^wac-314-55-083-cannabis-security]

| Device | Number | Cause of the position |
| --- | --- | --- |
| Cameras | 22 (20 bullet cameras, 1 doorbell camera, 1 PTZ camera) | Each entrance, each exit and each area for cultivation and for processing |
| Sirens | 16 | Personnel can hear a siren in each zone where they are |
| Drug safes | 2 | Attached to the floor, in rooms that have surveillance |
| Walk-in vault | 1 | The drying room is also the storage with security |
| PoE and UPS racks | 3 × 6U and 1 × 13U | Short cable routing. The power continues when the supply stops. |

*The list of devices, with the cause of the position of each device. The model shows the cable routing and the position of the UPS because an auditor examines them.[^wac-314-55-083-cannabis-security]*

## Procedure for the 3D model

This section gives the sequence of the work, with all the steps. The model is one HTML file with a JSON block and approximately 600 lines of generator code. It is small, and thus you can make a copy of it from a reference document and change it for your facility.

1. **Read the dimension chains**: Read the dimension chains on the floor plan of the architect (for example 4800 + 4632.40 + 4800 across the top). Divide each value in millimeters by 1000 to get meters.
2. **Write the data in JSON**: Write the rooms, the walls, the equipment and the devices in the schema of four records. This task is the primary task, and it becomes your one source of correct data.
3. **Make the shell**: Use the shell builders for the floor slabs, the walls with openings and lintels, and then the stairs. The model also checks the stairs.
4. **Add the fit-out**: Use the fit-out builders for the benches, the plants with instancing and the climate equipment. Use the sizes from the datasheets.
5. **Add the security layer**: Put the cameras with their FOV cones, the sirens, the safes, the vault and the racks in the model. Make one checkbox for all of them.
6. **Add the user controls**: Add an orbit camera and a view from above that shows the 2D floor plan with one selection. Add a function that shows the contents of each room and device when you select it.

> **NOTE: Copy and replace to use the model again**
>
> To start a new facility, you make a copy of the page with the importmap and the script block. Then you replace the data tables in the copy with the data of your facility. The generator code does not change. Only the numbers change.

## Troubleshooting

Most errors are of a small number of types, and these types occur many times. The most important error is a building that you make in software code and not in data. When you do this, each change of the layout is not easy, because you do not have one source of correct data. The other errors are small problems when the software renders the model. They are easy to correct when you know them.

| Error | Correction |
| --- | --- |
| You make the building in software code and not in data | Keep the building in the JSON schema, and let the software code only read it. This method is the primary method. |
| One light in the model for each grow fixture | 14 lights with shadows decrease the frame rate by a large quantity. Use one directional light (the ‘sun’) and emissive surfaces (surfaces that give light). |
| Walls in pure white are too bright | With ACES tone mapping, white values cannot be more than the maximum value. Use a warm color that is almost white (0xe8e6e0), with a high roughness. |
| A shadow camera that is too large | A shadow camera that is too large makes shadows with a low resolution. Make the size of the shadow camera correct for the building and not for all of the scene. |
| Picking in all of the scene | Users select walls when they do not want to select them. Use raycasting on a list of the objects that users can select, and not on all of the scene. |
| No one value of wall thickness for all walls | Set the thickness one time to 0.15 m (5.9 in) and use it again. This prevents many errors when you write the data. |

*Six frequent errors and the recommended correction for each. The time to correct the first error is some weeks. The time to correct each other error is some minutes.*

> **WARN: The most important error, again**
>
> Do not put geometry in the software code manually. If you put geometry in the software code manually, you cannot change the layout at a low cost. Then, for each ‘what if’, you change the software code. You do not change a number.

## Expected results and limitations

Know the limits of the model. This type of model is small and it operates quickly. The reference model renders a full facility with two floors at 60 frames each second on integrated graphics. The facility has approximately 450 meshes and the plants with instancing. The model can render full campuses if you use instancing, put the geometry together, and keep the draw calls to less than approximately 300.

Easy shapes are sufficient for almost all tasks. You use a special tool (Blender, with a file in glTF format) only when one asset with photoreal quality is necessary. You can use the model to make the layout, to show compliance and to monitor the facility. It is **not** a structural engineering approval, and it is not an approval of compliance with the building code. A qualified professional must make sure that the airflow and security targets in the model are correct.

> **Diagram.** The stages of the model, in the sequence of work. For most facilities, only the first stage is necessary for the layout.

| Item | Target | Information |
| --- | --- | --- |
| Meshes | approximately 450 | The shell and the fit-out of a full facility with two floors |
| Frame rate | 60 fps | The model operates smoothly on integrated graphics |
| Draw calls | < 300 | Laptops and tablets with a low capacity can use the model |
| Pixel ratio | The maximum is 2 | Prevents too much load on the GPU with 4K screens |
| Shadow lights | 1 | One directional light (the ‘sun’). The other lights are emissive surfaces. |

*The limits for performance. When you keep these values, the model operates correctly on almost all computers. The value of 60 fps is a benchmark. You can do the benchmark again to make sure of the value. The value is not the same on all computers.*

> **KEY: The model: tasks and limits**
>
> A 3D facility model is a tool for the layout, a document of compliance and an aid for training. When you connect it to sensors, it is also a dashboard with current data. It is not an engineering approval. A qualified professional must make sure that each target for airflow, for the structure and for security in the model is correct. Do not think that the model gives approval of the targets.

Start with easy shapes and put your floor plan in data. When the model finds a clash before construction, the cost of the clash is more than the cost of the model. For more information about the equipment in each room, read the [grow-room systems](grow-room-systems.html) paper. For more information about how to connect the model to current irrigation data, read the [irrigation manual](irrigation-manual.html).

## References

[^threejs-repo]: mrdoob and contributors. three.js, JavaScript 3D Library [WebGL/WebGPU scene-graph rendering library]. GitHub repository (MIT License). Accessed 2026-06-22. https://github.com/mrdoob/three.js/ (source from a manufacturer or industry)
[^kitaya-2003-air-current-gas-exchange]: Kitaya, Y., Tsuruyama, J., Shibuya, T., Endo, M., & Yoshida, M. (2003). Effects of air current speed on gas exchange in plant leaves and plant canopies. Advances in Space Research, 31(1), 177–182. DOI:10.1016/S0273-1177(02)00747-0 https://doi.org/10.1016/S0273-1177(02)00747-0 (source with peer review)
[^kimura-2020-leaf-boundary-layer]: Kimura, K., Yasutake, D., Yamanami, A., & Kitano, M. (2020). Spatial examination of leaf-boundary-layer conductance using artificial leaves for assessment of light airflow within a plant canopy under different controlled greenhouse conditions. Agricultural and Forest Meteorology, 280, 107773. DOI:10.1016/j.agrformet.2019.107773 https://doi.org/10.1016/j.agrformet.2019.107773 (source with peer review)
[^ibc-2024-1011-5-2-stairs]: International Code Council (2024). 2024 International Building Code (IBC), Section 1011.5.2, Riser height and tread depth (stair riser 7 in. max / 4 in. min; rectangular tread 11 in. min). https://codes.iccsafe.org/s/IBC2024P1/chapter-10-means-of-egress/IBC2024P1-Ch10-Sec1011.5.2 (source from a manufacturer or industry)
[^wac-314-55-083-cannabis-security]: Washington State Liquor and Cannabis Board. WAC 314-55-083, Security and traceability requirements for cannabis licensees (surveillance of all entrances/exits, processing/storage/destruction areas and POS; min. 640x470 resolution; min. 10 fps; recordings retained >=45 days; storage device secured against tampering/theft). https://app.leg.wa.gov/wac/default.aspx?cite=314-55-083 (source from a manufacturer or industry)
