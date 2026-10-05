# -*- coding: utf-8 -*-
"""Paper: designing a grow facility in 3D before you build it (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "facility-3d"
TITLE = "A 3D model of a grow facility before construction"
EYEBROW = "Facility · Layout"
SUB = ("With a 3D model on your screen, you can find errors that have a high cost before "
       "construction starts. The model shows the rooms, the equipment and the airflow.")
META = [("building", "Facility"), ("image", "11 diagrams"),
        ("doc", "Manual for operation"), ("clock", "~14 min to read")]
RELATED = ["airflow-design", "grow-room-systems", "f2-crop-steering"]
REF_IDS = ["threejs-repo", "kitaya-2003-air-current-gas-exchange",
           "kimura-2020-leaf-boundary-layer", "ibc-2024-1011-5-2-stairs",
           "wac-314-55-083-cannabis-security"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

# Fact-check jurisdiction banner
JURISDICTION_NOTE = "Examples of security and exit in this paper can refer to US regulations (WAC and IBC). These regulations are only examples. The correct building codes and license regulations are those of the jurisdiction that will do the inspection of your facility."


SECTIONS.append({"id": "intro", "kicker": "Start here",
  "title": "Purpose and scope",
  "blocks": [
    callout("NOTE", "Jurisdiction", JURISDICTION_NOTE),

    lead("A grow facility is a building with rooms, equipment, airflow and security cameras. The "
         "usual document for a facility is the floor plan, a flat drawing from above that an "
         "architect makes. Only experts can read a floor plan easily. A <strong>3D model</strong> "
         "is the same floor plan on your screen. You can turn it, make it larger or smaller, and "
         "select parts of it. Thus investors, electricians, inspectors and personnel can read it "
         "immediately."),
    p("Write the building as data and do not make a drawing of it. You write a data file with a "
      "list of the rooms and their dimensions. The software code makes the building from this data. "
      "To change the layout of the facility for the next harvest, you only change some "
      "numbers.</p><p>The example in this paper is a cultivation facility with a license and with "
      "two floors. The size is 14.8 by 16.7 m (48.6 by 54.8 ft)."),
    ul(["A 3D model shows the position of the objects in relation to each other. It shows the "
        "direction of the airflow, the area that each camera can see, and the density of the "
        "benches. It also shows the position of the ducts and the drains.",
        "The model uses Three.js, a library for the web with no cost. All of the model is one HTML "
        "file that you can use in each browser. Other software is not necessary." + _c("threejs-repo"),
        "The floor plan is a data file. Thus, to find the effect of a fourth bench, you change a "
        "list. You do not make the drawing of the building again.",
        "The same model does four tasks at the same time. It is a tool for the layout and a "
        "document of compliance for the license. It is also an aid for the training of personnel "
        "and a dashboard with current data."]),
    figure(grid([
        card("Flat 2D floor plan", "Lines and symbols, seen from above. It is accurate, but only an "
             "architect or a contractor can read all of it. It is for one group of persons.", "only experts"),
        card("Same floor plan in 3D", "A building on the screen, with labels. You can turn it and select "
             "a part to examine it. Each person can see the contents of a room and the area that a "
             "camera sees.", "all persons"),
        card("From the same numbers", "The drawing and the model use one data file. Thus they are "
             "always the same. When you change the data, the drawing and the model change.", "one source"),
      ], cols=3), 1,
      "The same facility, in a drawing and in a model. The 3D model does not replace the drawing of "
      "the architect. It makes the information of the drawing easy to read for all other persons."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Terms",
  "title": "Definitions",
  "blocks": [
    p("This section gives the terms of this paper. It is not necessary to know these terms before "
      "you read this paper. These terms occur many times in this paper. Read this section one time. "
      "Then the remaining part of this paper is easy to read."),
    defterm("3D model", "A model of the building on a screen. You can turn it, make it larger or "
            "smaller, and select parts of it. The model does not stay in one view. You can move in "
            "the model."),
    defterm("Three.js", "A software library with no cost that makes 3D scenes in a web browser. "
            "Other software is not necessary."),
    defterm("Floor plan", "The flat drawing of the walls, doors and rooms that an architect makes. It shows the building from above."),
    defterm("Render and scene", "To &lsquo;render&rsquo; is to show the model on the screen. The "
            "&lsquo;scene&rsquo; is all of the objects in the model: walls, benches, lights and "
            "cameras."),
    defterm("JSON data file", "A file with a list of data: the names, sizes and positions of the "
            "rooms. The software code reads this file to make the model."),
    defterm("FOV cone", "The &lsquo;field of view&rsquo; cone. It is a transparent cone that shows "
            "the area that one camera can see. Thus an area of the floor with no color is a blind "
            "spot."),
    defterm("Fit-out", "The equipment that you add to an empty room, for example benches, lights, "
            "dehumidifiers and CO&#8322; cylinders."),
    defterm("Digital twin", "A 3D model with a connection to sensors. It shows the current "
            "temperature and humidity of each room."),
  ]})

SECTIONS.append({"id": "model-the-data", "kicker": "Part 1",
  "title": "Building model from data",
  "blocks": [
    p("<strong>Do not make the building manually in software code.</strong> This decision is the "
      "most important decision of this method. Write the building as data, and let the software "
      "code make the geometry from the data. The reference schema, the structure of the data file, "
      "has only four types of record. Thus it can show almost all buildings for cultivation."),
    p("The data file shows each <strong>room</strong> as a rectangle, <code>[x, y, width, "
      "depth]</code> in meters. It shows each <strong>wall</strong> as a centerline with openings. "
      "The position of an opening is its distance along the wall.</p><p>One wall thickness of 0.15 "
      "m (5.9 in) for all walls prevents many errors when you write the data. All values use one "
      "unit: one unit is one meter. Thus you divide the millimeter values on the floor plan of the "
      "architect (4800, 9200) by 1000 one time, when you write the data. You do not do this again."),
    callout("key", "The four types of record",
      ul(["<strong>Rooms</strong>: a rectangle for the inner floor area, in meters.",
          "<strong>Walls</strong>: a centerline with openings (doors, the roller door of 4.6 m "
          "(15.1 ft), and pass-through openings) at a distance along the wall.",
          "<strong>Equipment</strong>: benches, dehumidifiers, AC heads and CO&#8322; tanks.",
          "<strong>Devices</strong>: cameras, sirens, safes, and racks for the network and for power."], "tight")),
    p("Doors, the roller door and pass-through openings are all the <em>same</em> type of object, "
      "an &lsquo;opening&rsquo; in a wall. An opening has a width and a head height (the height of "
      "the top). Thus the data file is short. Because the model is data, it stays correct when you "
      "change the layout. You change numbers, and you do not change geometry."),
    figure(grid([
        card("rooms", "rectangle = [x, y, w, d], the inner floor area in meters.", "[x,y,w,d]"),
        card("walls", "A centerline. Each opening has an &lsquo;at&rsquo; value (the distance along "
             "the wall), a width and a head height.", "at + width"),
        card("equipment", "Type and position. The size of each item is the size in its datasheet.", "type + position"),
        card("devices", "Position and an &lsquo;aim&rsquo; direction for cameras and sirens.", "position + direction"),
      ], cols=2), 2,
      "The four types of record, with the primary fields of each type. Approximately 25 wall rows "
      "show the full envelope and the partitions of the reference building."),
    figure(L.flow("One data file, three results",
            [("JSON data", "rooms, walls, equipment, devices"),
             ("2D SVG drawing", "the flat drawing from above"),
             ("Bench list", "canopy numbers and areas"),
             ("3D scene", "the model you can select")],
            note="One source of correct data: the drawing, the list and the 3D model are always the same."), 3,
      "All three read the same numbers. Thus, when you correct a dimension one time, it is correct in all three."),
  ]})

SECTIONS.append({"id": "shell-and-storeys", "kicker": "Part 2",
  "title": "The shell of the building: floors, walls, openings and stairs",
  "blocks": [
    p("The software code makes the shell of the building from the data: the floors, the walls and "
      "the stairs. <strong>Floor slabs</strong> are flat 2D shapes. The code &lsquo;extrudes&rsquo; "
      "each shape (it gives the shape a thickness), and a shape can have holes. You must make a "
      "hole for the void of the stairwell. The openings divide each <strong>wall run</strong> into "
      "solid parts. A lintel (a short beam) fills the space above each door."),
    p("<strong>Stairs</strong> are a sequence of boxes in the shape of steps. In the reference "
      "building, the stairs have a total height of 3.25 m (10.7 ft) and a run of 4.5 m (14.8 ft). "
      "They have 16 steps of 203 mm (8 in) each. The model also checks the stairs before "
      "construction.</p><p>If the space is not sufficient for steps with a correct riser height, "
      "you see this on the screen and not on the site. The usual building codes give a maximum of "
      "approximately 178 mm (7 in) for a riser and a minimum of 279 mm (11 in) for a tread. Thus a "
      "riser of 203 mm (8 in) is too high, and it shows that you must make the run longer." +
      _c("ibc-2024-1011-5-2-stairs")),
    ul(["Floor slabs are extruded shapes. They can have holes for stairwells and for service voids.",
        "A wall is a centerline with openings. The openings divide the wall into parts, with "
        "lintels above them. Only boxes are necessary.",
        "The model has one group of objects for each floor. When you change floors, the model shows "
        "one floor and does not show the other floor. The labels of the other floor also do not "
        "show.",
        "Approximately 10 lines of software code make small parts, for example the corrugated "
        "texture of the roller door. Image files are not necessary."]),
    figure(grid([
        card("Wall part", "Solid wall from the corner to the first opening.", "solid"),
        card("Opening", "A door with a head height of 2.05 m (6.7 ft). The &lsquo;at&rsquo; value is its distance along the wall.", "door"),
        card("Lintel", "A short box that fills the wall above the opening.", "above"),
        card("Wall part", "Solid wall continues to the next corner.", "solid"),
      ], cols=4), 4,
      "One wall run, from left to right. The &lsquo;at&rsquo; value of an opening is the distance "
      "along the wall at which the opening starts."),
    table(["Check", "Value", "Result"], [
      ["Total height", "3.25 m (10.7 ft)", "The two floor heights give this value"],
      ["Horizontal run", "4.5 m (14.8 ft)", "the space in the floor plan"],
      ["Risers", "16 &times; 203 mm (8 in)", "Too high. More than the maximum of 178 mm in the building code."],
      ["Treads", "281 mm (11.1 in)", "Good. More than the minimum of 279 mm."],
      ["Fit", "Correct for the run of 4.5 m", "Correct. But make the run longer to decrease the riser height."],
    ], cls="compact",
      caption="The model does this check of the stairs automatically. The riser of 203 mm is "
              "possible, but it is too high compared with the values in the building code" +
              _c("ibc-2024-1011-5-2-stairs") + ". This result is a signal to examine the riser at "
              "the start."),
  ]})

SECTIONS.append({"id": "fit-out-airflow", "kicker": "Part 3",
  "title": "Facility fit-out and airflow",
  "blocks": [
    p("<strong>Fit-out</strong> changes a building into a grow facility. You make each object from "
      "easy shapes. Special software is not necessary.</p><p>The reference flower rooms have three "
      "rolling benches in each room. Each bench is 1.2 by 7.6 m (3.9 by 24.9 ft). The canopy area "
      "is 27.4 m&#178; (295 ft&#178;) in a room of 44 m&#178; (474 ft&#178;), which is "
      "approximately 62% of the floor. The model shows this number immediately."),
    p("The plants are the objects with the highest number, 210 in this model. Thus the model uses "
      "&lsquo;instancing&rsquo;: the software renders all the plants in one batch and not one at a "
      "time. This method is the most important method to make the model operate quickly. The "
      "climate equipment (dehumidifiers, carbon filter and fan units hung at 2.45 m (8.0 ft), "
      "mini-split AC heads and CO&#8322; cylinders) has a small builder for each item. Each builder "
      "uses the size from the datasheet."),
    p("Each leaf releases water vapor and absorbs CO&#8322; all the time. In air that does not "
      "move, the layer of air at the surface of the leaf quickly has the maximum moisture and less "
      "CO&#8322;. This thin film prevents more gas exchange with the air around it, also in a cool "
      "room. This film is the leaf boundary layer: a thin layer of air that does not move. The "
      "transpiration of the leaf makes this air different." + _c("kitaya-2003-air-current-gas-exchange") +
      "</p><p>Air that moves removes this film and replaces it with new air from the room. The air "
      "movement makes the gradient for gas exchange again.</p><p>The floor plan has a target of "
      "3500 m&#179;/h of horizontal airflow for each flower room. The model shows this airflow as "
      "arrows that you can show or not show, and an HVAC contractor reads them immediately. A small "
      "and equal movement of air across the canopy keeps the conductance of the boundary layer high "
      "and equal. If the movement is too small, areas where the air does not move occur. If the "
      "movement is too large, the stomata can close." + _c("kimura-2020-leaf-boundary-layer")),
    figure(L.bars("Canopy and floor area in one flower room",
            [("Canopy (3 benches)", 27.4), ("Total floor", 44.0)], unit=" m²",
            note="Three benches of 1.2 × 7.6 m give a canopy area of approximately 62% of the floor.",
            maxv=52), 5,
      "The model shows the canopy density automatically, and you do not measure it manually. 62% is "
      "a good density for a flower room. It lets personnel walk in the room."),
    figure(L.zones("Loop of horizontal airflow across one room", 0, 100,
            [(2, 48, L.GL, "flow out above benches 1 and 2"),
             (52, 98, L.BLUL, "flow back above bench 3")],
            unit="%",
            note="The air flows out across the canopy and then back in a loop, approximately 3500 m³/h."), 6,
      "The figure shows the airflow as a loop, seen from above. When you show the airflow, "
      "contractors and inspectors can see the direction of the air, and you can find where the "
      "benches stop the flow." + _c("kitaya-2003-air-current-gas-exchange")),
    table(["Item", "Made from", "Number"], [
      ["Rolling bench", "Box and leg rails, 1.2 &times; 7.6 m (3.9 &times; 24.9 ft)", "9 (3 for each flower room)"],
      ["Dehumidifier", "Box and grille", "7"],
      ["Carbon filter and fan", "Cylinder and duct, hung at 2.45 m (8.0 ft)", "10"],
      ["AC head (mini-split)", "Flat box above the doors", "8"],
      ["CO&#8322; cylinder", "Closed cylinder, on the floor", "6"],
    ], cls="compact",
      caption="The list of equipment. Each item has a small builder that you can use again. When "
              "you put the items in 3D, you find clashes at the start. Examples are a filter above "
              "an aisle or an AC head that touches the door when it moves."),
    callout("tip", "Clashes that you can see only in 3D",
      p("A flat floor plan does not show height. In 3D you see immediately a carbon filter hung at "
        "2.45 m (8.0 ft) above a walkway. You also see an AC head above the area where a door "
        "moves, or a dehumidifier in the same position as a bench. Use the <a "
        "href='airflow-design.html'>airflow design</a> paper to find the size of the fans before "
        "you put them in the model.")),
  ]})

SECTIONS.append({"id": "security-layer", "kicker": "Part 4",
  "title": "Security and compliance controls that you can see",
  "blocks": [
    p("An auditor examines the <strong>security plan</strong> of a cultivation facility with a "
      "license. When you put this layer in the model, a checklist on paper becomes a model that you "
      "can show to an inspector. Each camera has a transparent <strong>FOV cone</strong>. The "
      "length of the cone is the range of the camera, and the width of the cone is the angle of the "
      "lens. An area of the floor with no color is a blind spot."),
    p("The security regulations for cannabis are different in each jurisdiction. For example, "
      "typical regulations make surveillance necessary for each entrance, exit, and area for "
      "processing, storage and destruction. They also give a minimum resolution and frame rate for "
      "the cameras. The video records must stay in storage for some weeks." +
      _c("wac-314-55-083-cannabis-security") + "</p><p>When you show the cameras as cones, you can "
      "show visually that the cameras see all necessary areas. A list is not necessary for "
      "this.</p><p>The model of the reference facility has approximately 22 cameras (20 bullet "
      "cameras, 1 doorbell camera and 1 PTZ camera), 16 sirens and 2 drug safes attached to the "
      "floor. It also has a walk-in vault (this vault is the drying room) and the PoE and UPS racks "
      "(three racks of 6U and one rack of 13U). The racks supply power to all of this equipment."),
    ul(["Camera cones give a visual check for the license. The cones show if the three cameras in a "
        "flower room can see all three benches. They also show if there is an area of the lobby "
        "that the two cameras in the hallway do not see.",
        "A blind spot is an area of the floor with no color. You find it much more easily than in a "
        "list of the areas that the cameras see.",
        "The model has the sirens, the safes, the vault and the racks for the network and for "
        "power. The cable routing and the position of the UPS are a part of the security plan, and "
        "thus the model shows them.",
        "One checkbox shows or does not show all of the security layer. The checkbox gives audit mode or tour mode.",
        "The model compares the cone of the PTZ camera on the roof (70&deg;, 12 m (39 ft)) with the "
        "office on the top floor, which has no partitions. It shows if the camera can see an "
        "intruder."]),
    figure(L.zones("Camera cones in one flower room", 0, 100,
            [(4, 40, L.GL, "camera 1 cone"),
             (34, 70, L.GL, "camera 2 cone"),
             (74, 98, L.GL, "camera 3 cone")],
            unit="%",
            note="The cones have an overlap. The area 40 to 74 can be a blind spot. Point the cameras again."), 7,
      "The camera cones, seen from above. An area of the floor that is not in a cone is a blind "
      "spot. Here, there is a gap between cameras 2 and 3, and the gap closes when you point the "
      "cameras in a new direction." + _c("wac-314-55-083-cannabis-security")),
    table(["Device", "Number", "Cause of the position"], [
      ["Cameras", "22 (20 bullet cameras, 1 doorbell camera, 1 PTZ camera)", "Each entrance, each exit and each area for cultivation and for processing"],
      ["Sirens", "16", "Personnel can hear a siren in each zone where they are"],
      ["Drug safes", "2", "Attached to the floor, in rooms that have surveillance"],
      ["Walk-in vault", "1", "The drying room is also the storage with security"],
      ["PoE and UPS racks", "3 &times; 6U and 1 &times; 13U", "Short cable routing. The power continues when the supply stops."],
    ], cls="compact",
      caption="The list of devices, with the cause of the position of each device. The model shows "
              "the cable routing and the position of the UPS because an auditor examines them." +
              _c("wac-314-55-083-cannabis-security")),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "Method",
  "title": "Procedure for the 3D model",
  "blocks": [
    p("This section gives the sequence of the work, with all the steps. The model is one HTML file "
      "with a JSON block and approximately 600 lines of generator code. It is small, and thus you "
      "can make a copy of it from a reference document and change it for your facility."),
    steps([
      ("Read the dimension chains", "Read the dimension chains on the floor plan of the architect "
       "(for example 4800 + 4632.40 + 4800 across the top). Divide each value in millimeters by "
       "1000 to get meters."),
      ("Write the data in JSON", "Write the rooms, the walls, the equipment and the devices in the "
       "schema of four records. This task is the primary task, and it becomes your one source of "
       "correct data."),
      ("Make the shell", "Use the shell builders for the floor slabs, the walls with openings and "
       "lintels, and then the stairs. The model also checks the stairs."),
      ("Add the fit-out", "Use the fit-out builders for the benches, the plants with instancing and "
       "the climate equipment. Use the sizes from the datasheets."),
      ("Add the security layer", "Put the cameras with their FOV cones, the sirens, the safes, the "
       "vault and the racks in the model. Make one checkbox for all of them."),
      ("Add the user controls", "Add an orbit camera and a view from above that shows the 2D floor plan "
       "with one selection. Add a function that shows the contents of each room and device when you "
       "select it."),
    ]),
    callout("note", "Copy and replace to use the model again",
      p("To start a new facility, you make a copy of the page with the importmap and the script "
        "block. Then you replace the data tables in the copy with the data of your facility. The "
        "generator code does not change. Only the numbers change.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Prevent these errors",
  "title": "Troubleshooting",
  "blocks": [
    p("Most errors are of a small number of types, and these types occur many times. The most "
      "important error is a building that you make in software code and not in data. When you do "
      "this, each change of the layout is not easy, because you do not have one source of correct "
      "data. The other errors are small problems when the software renders the model. They are easy "
      "to correct when you know them."),
    table(["Error", "Correction"], [
      ["You make the building in software code and not in data", "Keep the building in the JSON schema, and let the software code only read it. This method is the primary method."],
      ["One light in the model for each grow fixture", "14 lights with shadows decrease the frame rate by a large quantity. Use one directional light (the &lsquo;sun&rsquo;) and emissive surfaces (surfaces that give light)."],
      ["Walls in pure white are too bright", "With ACES tone mapping, white values cannot be more than the maximum value. Use a warm color that is almost white (0xe8e6e0), with a high roughness."],
      ["A shadow camera that is too large", "A shadow camera that is too large makes shadows with a low resolution. Make the size of the shadow camera correct for the building and not for all of the scene."],
      ["Picking in all of the scene", "Users select walls when they do not want to select them. Use raycasting on a list of the objects that users can select, and not on all of the scene."],
      ["No one value of wall thickness for all walls", "Set the thickness one time to 0.15 m (5.9 in) and use it again. This prevents many errors when you write the data."],
    ], cls="compact",
      caption="Six frequent errors and the recommended correction for each. The time to correct the "
              "first error is some weeks. The time to correct each other error is some minutes."),
    callout("warn", "The most important error, again",
      p("Do not put geometry in the software code manually. If you put geometry in the software "
        "code manually, you cannot change the layout at a low cost. Then, for each &lsquo;what "
        "if&rsquo;, you change the software code. You do not change a number.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Limits",
  "title": "Expected results and limitations",
  "blocks": [
    p("Know the limits of the model. This type of model is small and it operates quickly. The "
      "reference model renders a full facility with two floors at 60 frames each second on "
      "integrated graphics. The facility has approximately 450 meshes and the plants with "
      "instancing. The model can render full campuses if you use instancing, put the geometry "
      "together, and keep the draw calls to less than approximately 300."),
    p("Easy shapes are sufficient for almost all tasks. You use a special tool (Blender, with a "
      "file in glTF format) only when one asset with photoreal quality is necessary. You can use "
      "the model to make the layout, to show compliance and to monitor the facility. It is "
      "<strong>not</strong> a structural engineering approval, and it is not an approval of "
      "compliance with the building code. A qualified professional must make sure that the airflow "
      "and security targets in the model are correct."),
    figure(L.flow("Stages of the model",
            [("Easy shapes", "boxes and cylinders for most layout tasks"),
             ("glTF asset", "Blender asset, only for photoreal quality"),
             ("Dashboard", "React UI around the scene"),
             ("Digital twin", "sensors through MQTT or Home Assistant")],
            note="Each stage is more work. Use only the stages that are necessary for the task."), 8,
      "The stages of the model, in the sequence of work. For most facilities, only the first stage is necessary for the layout."),
    table(["Item", "Target", "Information"], [
      ["Meshes", "approximately 450", "The shell and the fit-out of a full facility with two floors"],
      ["Frame rate", "60 fps", "The model operates smoothly on integrated graphics"],
      ["Draw calls", "&lt; 300", "Laptops and tablets with a low capacity can use the model"],
      ["Pixel ratio", "The maximum is 2", "Prevents too much load on the GPU with 4K screens"],
      ["Shadow lights", "1", "One directional light (the &lsquo;sun&rsquo;). The other lights are emissive surfaces."],
    ], cls="compact",
      caption="The limits for performance. When you keep these values, the model operates correctly "
              "on almost all computers. The value of 60 fps is a benchmark. You can do the "
              "benchmark again to make sure of the value. The value is not the same on all "
              "computers."),
    callout("key", "The model: tasks and limits",
      p("A 3D facility model is a tool for the layout, a document of compliance and an aid for "
        "training. When you connect it to sensors, it is also a dashboard with current data. It is "
        "not an engineering approval. A qualified professional must make sure that each target for "
        "airflow, for the structure and for security in the model is correct. Do not think that the "
        "model gives approval of the targets.")),
    p("Start with easy shapes and put your floor plan in data. When the model finds a clash before "
      "construction, the cost of the clash is more than the cost of the model. For more information "
      "about the equipment in each room, read the <a href='grow-room-systems.html'>grow-room "
      "systems</a> paper. For more information about how to connect the model to current irrigation "
      "data, read the <a href='irrigation-manual.html'>irrigation manual</a>."),
  ]})
