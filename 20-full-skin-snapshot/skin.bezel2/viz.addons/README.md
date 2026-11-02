# viz.addons — Bezel viz style packs
Data-only packs (textures + manifest.json) loaded by the `visualization.bezel` engine addon. No C++ here, no skin XML.
Engine looks in: addon setting `pack_root` → `special://skin/viz.addons/<id>/`.

Per pack v1 budget (engine caps): 3–6 layers (light_behind → haze → dust → strobe_fx → debug),
ONE atlas, ~4–16 soft textures (`textures/<name>.png`, premultiplied-ish white RGBA glows/sheets/warps).
Particle count is the real throttle (`defaults.particle_cap`, engine hard cap 2000).
Layer kinds: light_behind, haze, dust, strobe_fx, debug. See /workspace/dust-viz-skills/dustviz-engine-scaffold.md.
