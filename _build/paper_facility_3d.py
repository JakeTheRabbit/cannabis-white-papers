# -*- coding: utf-8 -*-
"""Paper: designing a grow facility in 3D before you build it (beginner)."""
from components import (p, lead, h, ul, ol, callout, defterm, table, figure,
                        stagecard, grid, card, chip, kv, steps)
import figs_lib as L

SLUG = "facility-3d"
TITLE = "Designing a grow facility in 3D before you build it"
EYEBROW = "Facility · Design"
SUB = ("Lay out rooms, equipment and airflow in a 3D model on your screen, and catch the "
       "expensive mistakes before anyone pours concrete.")
META = [("building", "Facility"), ("image", "11 diagrams"),
        ("doc", "Operational guide"), ("clock", "~14 min read")]
RELATED = ["airflow-design", "grow-room-systems", "f2-crop-steering"]
REF_IDS = ["threejs-repo", "kitaya-2003-air-current-gas-exchange",
           "kimura-2020-leaf-boundary-layer", "ibc-2024-1011-5-2-stairs",
           "wac-314-55-083-cannabis-security"]

def _c(rid):
    return "<sup class='cite'><a href='#ref-%s'>[%d]</a></sup>" % (rid, REF_IDS.index(rid) + 1)

SECTIONS = []

SECTIONS.append({"id": "intro", "kicker": "Start here",
  "title": "What 3D facility planning is (and why it beats a paper plan)",
  "blocks": [
    lead("A grow facility is a building full of rooms, equipment, airflow paths and security "
         "cameras. The usual way to plan one, a flat top-down architect's drawing, can only "
         "really be read by experts. A <strong>3D model</strong> is the same plan rebuilt on "
         "your screen as a thing you can rotate, zoom into and click on, so investors, "
         "electricians, inspectors and staff all understand it instantly."),
    p("Describe the building as data instead of drawing it. You write a data file, a plain list "
      "of rooms and their dimensions, and let code draw the building from that data. Re-planning "
      "the facility for the next harvest then becomes nothing more than editing some numbers. The "
      "worked example throughout this paper is a real two-storey licensed cultivation facility "
      "measuring 14.8 by 16.7 metres."),
    ul(["A 3D model makes spatial relationships visible: airflow paths, camera sightlines, bench "
        "density, and where the ducts and drains run.",
        "It is built with Three.js, a free web library, so the whole thing is one HTML file that "
        "opens in any browser with nothing to install." + _c("threejs-repo"),
        "Because the floor plan is a data file, asking &lsquo;what if we fit a fourth bench?&rsquo; "
        "means editing a list, not redrawing the building.",
        "The same model serves four jobs at once: a design tool, a compliance exhibit for "
        "licensing, a staff training aid, and a live monitoring dashboard."]),
    figure(grid([
        card("Flat 2D floor plan", "Top-down lines and symbols. Accurate, but only an architect "
             "or builder can fully read it. One audience.", "experts only"),
        card("Same plan in 3D", "A rotatable, labelled building you click to inspect. Anyone can "
             "see what a room holds and where a camera looks.", "everyone"),
        card("From the same numbers", "Both views come from one data file, so they can never "
             "disagree. Edit the data, both update.", "one source"),
      ], cols=3), 1,
      "The same facility, two ways to read it. The 3D view does not replace the architect's "
      "drawing. It makes that drawing legible to everyone else."),
  ]})

SECTIONS.append({"id": "key-terms", "kicker": "Plain-English dictionary",
  "title": "Key terms, defined from zero",
  "blocks": [
    p("Here is the vocabulary. None of these need prior knowledge. They are the words this topic "
      "keeps using. Read this once and the rest of the paper reads easily."),
    defterm("3D model", "A picture of the building you can rotate, zoom and click on a screen. "
            "Not a fixed photo, but a thing you move around."),
    defterm("Three.js", "A free code library that draws 3D scenes inside an ordinary web "
            "browser, with nothing to install."),
    defterm("Floor plan", "The architect's flat, top-down drawing of walls, doors and rooms."),
    defterm("Render / scene", "To &lsquo;render&rsquo; is to draw the picture. The "
            "&lsquo;scene&rsquo; is everything in the model: walls, benches, lights, "
            "cameras."),
    defterm("JSON / data file", "A plain list of facts, room names, sizes and positions, "
            "that the code reads to build the model."),
    defterm("FOV cone", "&lsquo;Field of view&rsquo; cone: a see-through wedge showing exactly "
            "what one camera can see, so blind spots show up as floor with no tint."),
    defterm("Fit-out", "The equipment and furniture added to a bare room: benches, "
            "lights, dehumidifiers, CO&#8322; cylinders."),
    defterm("Digital twin", "A 3D model wired to live sensors, so it shows the real, current "
            "temperature and humidity of each room."),
  ]})

SECTIONS.append({"id": "model-the-data", "kicker": "Core idea 1",
  "title": "Model the building as data, not as a drawing",
  "blocks": [
    p("<strong>Do not draw the building by hand in code.</strong> This is the single most "
      "important decision in the whole approach. Describe it as data, and let the code interpret "
      "that data into geometry. The reference schema, the shape of the data file, needs only four "
      "kinds of record to capture almost any grow building."),
    p("Each <strong>room</strong> is stored as a rectangle, <code>[x, y, width, depth]</code> "
      "in metres. Each <strong>wall</strong> is a centre-line with openings positioned by how far "
      "along the run they sit, and a single global wall thickness (0.15 m) avoids a whole class of "
      "typos. Everything uses one unit equals one metre, so the millimetre numbers on the "
      "architect's plan (4800, 9200) are divided by 1000 once, at data-entry time, and never "
      "thought about again."),
    callout("key", "The four record types",
      ul(["<strong>Rooms</strong>: an interior footprint rectangle in metres.",
          "<strong>Walls</strong>: a centre-line with openings (doors, the 4.6 m roller "
          "door, pass-throughs) placed by distance along the run.",
          "<strong>Equipment</strong>: benches, dehumidifiers, AC heads, CO&#8322; tanks.",
          "<strong>Devices</strong>: cameras, sirens, safes, network and power racks."], "tight")),
    p("Doors, the roller door and pass-throughs are all the <em>same</em> thing: an "
      "&lsquo;opening&rsquo; on a wall, with a width and a head (top) height. That sameness keeps "
      "the data file short. Because the model is data, it survives every re-plan. You edit "
      "numbers, not geometry."),
    figure(grid([
        card("rooms", "rect = [x, y, w, d], the interior footprint in metres.", "[x,y,w,d]"),
        card("walls", "A centre-line; each opening sits &lsquo;at&rsquo; a distance along the run, "
             "with a width and head height.", "at + width"),
        card("equipment", "Type plus position; each item sized from its datasheet.", "type + pos"),
        card("devices", "Position plus an &lsquo;aim&rsquo; bearing for cameras and sirens.", "pos + aim"),
      ], cols=2), 2,
      "The four record types, with the key fields each one carries. Roughly 25 wall rows describe "
      "the entire reference building's envelope and partitions."),
    figure(L.flow("One data file, three outputs",
            [("JSON data", "rooms, walls, equipment, devices"),
             ("2D SVG plan", "the familiar top-down drawing"),
             ("Bench report", "canopy counts and areas"),
             ("3D scene", "the clickable model")],
            note="One source of truth: the plan, the report and the 3D view can never disagree."), 3,
      "Because all three views read the same numbers, fixing a dimension once fixes it everywhere."),
  ]})

SECTIONS.append({"id": "shell-and-storeys", "kicker": "Core idea 2",
  "title": "Building the shell: floors, walls, openings and stairs",
  "blocks": [
    p("Code builds the physical shell from the data: the floors, walls and stairs. "
      "<strong>Floor slabs</strong> are flat 2D shapes &lsquo;extruded&rsquo; (pushed up) into "
      "thickness, and they can include holes. You need a hole for the void where the stairwell "
      "drops through. Each <strong>wall run</strong> is split by its openings into solid segments, "
      "with a lintel (a short beam) filling the gap above each door."),
    p("<strong>Stairs</strong> are a loop of step-shaped boxes. The reference building climbs "
      "3.25 m over a 4.5 m run as 16 steps of 203 mm each. Drawing the stair this way doubles as a "
      "buildability check: if the steps don't fit the space at a sensible riser height, you find out "
      "now, on screen, not on site. Standard building codes cap a stair riser at about 178 mm "
      "(7 inches) with a tread of at least 279 mm (11 inches), so a 203 mm riser flags as steep and "
      "tells you to lengthen the run." + _c("ibc-2024-1011-5-2-stairs")),
    ul(["Floor slabs are extruded shapes that can carry holes for stairwells and service voids.",
        "A wall is a centre-line plus openings; openings split it into segments with lintels above. "
        "No complex geometry needed.",
        "Each storey gets its own group, so switching floors just hides one and shows the other "
        "(its labels hide automatically too).",
        "Details like the corrugated roller-door texture come from about 10 lines of code, with no "
        "image files."]),
    figure(grid([
        card("Segment", "Solid wall from the corner to the first opening.", "solid"),
        card("Opening", "A door, head height 2.05 m, placed &lsquo;at&rsquo; its distance along the run.", "door"),
        card("Lintel", "A short box filling the wall above the opening.", "above"),
        card("Segment", "Solid wall continues to the next corner.", "solid"),
      ], cols=4), 4,
      "One wall run, read left to right. The opening's &lsquo;at&rsquo; value is simply how far "
      "along the wall it starts."),
    table(["Check", "Value", "Verdict"], [
      ["Total rise", "3.25 m", "fixed by the two floor heights"],
      ["Horizontal run", "4.5 m", "the space allotted on the plan"],
      ["Risers", "16 &times; 203 mm", "steep, over the 178 mm code max"],
      ["Treads", "281 mm", "comfortable, above the 279 mm min"],
      ["Fit", "Fits the 4.5 m run", "OK, but lengthen run to ease the riser"],
    ], cls="compact",
      caption="A stair sanity-check the model performs for free. The 203 mm riser is buildable but "
              "steep against code minimums" + _c("ibc-2024-1011-5-2-stairs") + ", a prompt to revisit it early."),
  ]})

SECTIONS.append({"id": "fit-out-airflow", "kicker": "Core idea 3",
  "title": "Fit-out: benches, plants, climate gear and airflow",
  "blocks": [
    p("<strong>Fit-out</strong> turns a generic building into a grow facility, and every "
      "piece is built from simple shapes. No modelling software required. The reference "
      "flower rooms use 1.2 by 7.6 m rolling benches, three per room, giving 27.4 m&#178; of canopy "
      "in a 44 m&#178; room: about 62% of the floor, a number the model shows at a glance."),
    p("Plants are the highest-count object, 210 of them here, so they are "
      "&lsquo;instanced&rsquo;, meaning drawn in one batch rather than one at a time. That single "
      "trick is the biggest performance lever in the whole model. The climate gear (dehumidifiers, "
      "carbon filter/fan units hung at 2.45 m, mini-split AC heads, CO&#8322; cylinders) each get a "
      "tiny builder, sized straight from the datasheet."),
    p("Moving air thins the still &lsquo;boundary layer&rsquo; of humid air "
      "that clings to each leaf, which is what lets the leaf actually exchange water vapour and "
      "CO&#8322; with the room" + _c("kitaya-2003-air-current-gas-exchange") + ". The plan's target of "
      "3500 m&#179;/h of horizontal airflow per flower room is drawn as toggleable arrows that an "
      "HVAC contractor reads instantly. Modest, even air movement across the canopy keeps that "
      "boundary-layer conductance high and uniform. Too little leaves dead spots, too much can "
      "close stomata" + _c("kimura-2020-leaf-boundary-layer") + "."),
    figure(L.bars("Canopy vs floor area, one flower room",
            [("Canopy (3 benches)", 27.4), ("Total floor", 44.0)], unit=" m²",
            note="Three 1.2 × 7.6 m benches give about 62% canopy coverage of the room floor.",
            maxv=52), 5,
      "The model surfaces canopy density automatically. You never measure it by hand. "
      "62% is a healthy, walkable density for a flower room."),
    figure(L.zones("Horizontal airflow loop across one room", 0, 100,
            [(2, 48, L.GL, "outward flow over benches 1–2"),
             (52, 98, L.BLUL, "return flow over bench 3")],
            unit="%",
            note="A racetrack loop: air sweeps out across the canopy and returns, ~3500 m³/h."), 6,
      "Airflow shown as a top-down loop. Drawing it makes the air path visible to contractors and "
      "inspectors, and reveals where benches would stall the flow." + _c("kitaya-2003-air-current-gas-exchange")),
    table(["Item", "Built from", "Count"], [
      ["Rolling bench", "Box + leg rails, 1.2 &times; 7.6 m", "9 (3 per flower room)"],
      ["Dehumidifier", "Box + grille face", "7"],
      ["Carbon filter / fan", "Cylinder + duct, hung at 2.45 m", "10"],
      ["AC head (mini-split)", "Flattened box above doors", "8"],
      ["CO&#8322; cylinder", "Capped cylinder, floor-standing", "6"],
    ], cls="compact",
      caption="The equipment schedule. Each item is a small reusable builder, and placing them in 3D "
              "reveals clashes early: a filter over an aisle, an AC head fouling a door."),
    callout("tip", "Clashes you only see in 3D",
      p("A flat plan hides height. In 3D you immediately catch a carbon filter hung at 2.45 m over a "
        "walkway, an AC head sitting above a door swing, or a dehumidifier that lands on a bench. "
        "Pair this with the <a href='airflow-design.html'>airflow design</a> paper to size the "
        "fans before you place them.")),
  ]})

SECTIONS.append({"id": "security-layer", "kicker": "Core idea 4",
  "title": "The security and compliance layer you can actually see",
  "blocks": [
    p("Licensed cultivation is audited on its <strong>security plan</strong>, and modelling that "
      "layer turns a paper checklist into something you can walk an inspector through. Each camera "
      "gets a translucent <strong>FOV cone</strong>: its length is the usable range, its "
      "width is the lens angle. Blind spots show up as floor with no tint at all."),
    p("Cannabis security rules are jurisdiction-specific, but they are concrete: a typical regime "
      "requires surveillance of every entrance, exit, and processing, storage and destruction area, "
      "at a minimum resolution and frame rate, with recordings retained for weeks" + _c("wac-314-55-083-cannabis-security") +
      ". Modelling the cameras as cones lets you prove that coverage visually instead of arguing it "
      "from a list. The reference facility models roughly 22 cameras (20 bullet, 1 doorbell, 1 PTZ), "
      "16 sirens, 2 floor-bolted drug safes, a walk-in vault (the drying room itself), and the "
      "PoE/UPS racks (three 6U plus one 13U) that keep it all powered."),
    ul(["Camera cones answer licensing questions visually: do three flower-room cameras cover all "
        "three benches? Does the hallway pair leave a lobby gap?",
        "Blind spots appear as un-tinted floor, far easier to spot than reading a coverage "
        "list.",
        "Sirens, safes, the vault and the network/power racks are all modelled, because cable runs "
        "and UPS placement are part of the security story.",
        "One checkbox shows or hides the whole security layer: audit mode versus tour mode.",
        "The roof PTZ camera's 70&deg;, 12 m cone is checked against the upper open-plan office for "
        "intrusion coverage."]),
    figure(L.zones("Camera coverage across one flower room", 0, 100,
            [(4, 40, L.GL, "cam 1 cone"),
             (34, 70, L.GL, "cam 2 cone"),
             (74, 98, L.GL, "cam 3 cone")],
            unit="%",
            note="Cones overlap mid-room; the 40–74 stretch is a candidate blind spot to re-aim."), 7,
      "Top-down camera coverage. Any floor outside every cone is a blind spot. Here, a gap "
      "between cameras 2 and 3 that re-aiming closes." + _c("wac-314-55-083-cannabis-security")),
    table(["Device", "Count", "Placement logic"], [
      ["Cameras", "22 (20 bullet, 1 doorbell, 1 PTZ)", "Every entrance, exit and grow/process area"],
      ["Sirens", "16", "Audible coverage of all occupied zones"],
      ["Drug safes", "2", "Floor-bolted, inside monitored rooms"],
      ["Walk-in vault", "1", "The drying room doubles as secured storage"],
      ["PoE + UPS racks", "3 &times; 6U + 1 &times; 13U", "Short cable runs; power survives an outage"],
    ], cls="compact",
      caption="The device schedule and why each sits where it does. Cable runs and UPS placement "
              "are modelled because they are part of what an auditor checks." + _c("wac-314-55-083-cannabis-security")),
  ]})

SECTIONS.append({"id": "how-to", "kicker": "Do it yourself",
  "title": "A step-by-step path from plan to clickable model",
  "blocks": [
    p("Here is the practical order of work, with nothing skipped. The whole thing is one HTML file, "
      "a JSON block, and roughly 600 lines of generator code, small enough to lift straight "
      "from a reference document and adapt."),
    steps([
      ("Read the dimension chains", "Off the architect's plan, read the chains (e.g. 4800 + 4632.40 + "
       "4800 across the top) and divide every millimetre figure by 1000 to get metres."),
      ("Transcribe to JSON", "Enter rooms, walls, equipment and devices into the four-record schema. "
       "This is the real work, and it becomes your single source of truth."),
      ("Build the shell", "Run the shell builders: floor slabs, walls with openings and lintels, "
       "then the stairs (which also sanity-check themselves)."),
      ("Add the fit-out", "Run the fit-out builders: benches, instanced plants, and climate gear "
       "sized from datasheets."),
      ("Add the security layer", "Place cameras with their FOV cones, sirens, safes, the vault and "
       "the racks; group them under one toggle."),
      ("Add interaction", "An orbit camera plus a one-click top view that reproduces the 2D plan, "
       "and click-to-inspect so each room and device reports its own contents."),
    ]),
    callout("note", "Reuse is copy-and-replace",
      p("To start a new facility, save the page, copy the importmap and script block, and replace "
        "the data tables with your own plan. The generator code does not change. Only the "
        "numbers do.")),
  ]})

SECTIONS.append({"id": "pitfalls", "kicker": "Avoid these",
  "title": "Common pitfalls and how to dodge them",
  "blocks": [
    p("Most mistakes come from a handful of repeatable errors. The biggest by far is modelling in "
      "code instead of in data. Do that and every re-plan becomes painful, because you have "
      "thrown away your single source of truth. The rest are rendering details that are easy to fix "
      "once you know them."),
    table(["Pitfall", "The fix"], [
      ["Modelling in code, not data", "Keep the building in the JSON schema and let code only interpret it. This is the cardinal rule."],
      ["One real light per grow fixture", "14 shadow-casting lights kill the frame rate. Use one directional &lsquo;sun&rsquo; plus emissive (glowing) surfaces."],
      ["Pure-white walls blow out", "Under ACES tone mapping, white clips. Use a warm off-white (0xe8e6e0) at high roughness."],
      ["Shadow camera too big", "An oversized shadow camera makes mushy shadows. Size it to the building, not the world."],
      ["Picking against the whole scene", "Users accidentally select walls. Raycast a curated &lsquo;pickables&rsquo; list instead."],
      ["Forgetting wall thickness as a global", "Set thickness once (0.15 m) and reuse it. This removes a whole class of typos."],
    ], cls="compact",
      caption="Six common pitfalls and the recommended fix for each. The first one is the only one "
              "that costs you weeks. The rest cost minutes."),
    callout("warn", "The cardinal sin, restated",
      p("Remember one thing: the moment you start hand-placing geometry in code, you have "
        "lost the ability to re-plan cheaply. Every &lsquo;what if&rsquo; then means re-coding "
        "instead of re-typing a number.")),
  ]})

SECTIONS.append({"id": "expectations", "kicker": "Reality check",
  "title": "What 3D planning realistically gets you, and what it does not",
  "blocks": [
    p("Set expectations honestly. This kind of model is light and fast: the reference demo draws a "
      "full two-storey facility, about 450 meshes plus instanced plants, at 60 frames "
      "per second on integrated graphics, and scales to whole campuses by instancing and merging "
      "geometry while keeping draw calls under about 300."),
    p("Simple shapes carry you surprisingly far. You only reach for a proper modelling tool "
      "(Blender, exported as glTF) when you need a single photoreal &lsquo;hero&rsquo; asset. The "
      "model is a planning, compliance and monitoring aid. It is <strong>not</strong> a "
      "structural-engineering or code-compliance sign-off. The airflow and security targets it "
      "visualises still need a qualified professional to validate."),
    figure(L.flow("How far to take it",
            [("Primitives", "boxes and cylinders; covers most planning"),
             ("glTF hero", "Blender asset only where photoreal matters"),
             ("Dashboard", "React UI wrapped around the scene"),
             ("Digital twin", "live MQTT / Home Assistant sensors")],
            note="Each rung is more effort; climb only as far as the job actually needs."), 8,
      "A capability ladder. Most facilities never need to climb past the first rung for planning."),
    table(["Budget", "Target", "Why"], [
      ["Meshes", "~450", "A full two-storey facility shell + fit-out"],
      ["Frame rate", "60 fps", "Smooth on integrated graphics"],
      ["Draw calls", "&lt; 300", "Keeps low-end laptops and tablets usable"],
      ["Pixel ratio", "capped at 2", "Stops 4K screens overworking the GPU"],
      ["Shadow lights", "1", "One sun; the rest are emissive surfaces"],
    ], cls="compact",
      caption="The performance budget. Hit these and the model stays smooth almost anywhere. The "
              "60-fps figure is a reproduce-to-verify benchmark, not a guarantee for every machine."),
    callout("key", "What it is, and what it is not",
      p("A 3D facility model is a design tool, a compliance exhibit, a training aid and, "
        "wired to sensors, a live dashboard. It is not an engineering sign-off. Treat every "
        "airflow, structural and security target it shows as something to confirm with a "
        "professional, not as approved.")),
    p("Start with primitives, get your plan into data, and the model pays for itself the first time "
      "it catches a clash before construction. From here, read the "
      "<a href='grow-room-systems.html'>grow-room systems</a> paper to see what fills each room, or "
      "the <a href='irrigation-manual.html'>irrigation manual</a> for wiring the model to live "
      "irrigation data."),
  ]})
