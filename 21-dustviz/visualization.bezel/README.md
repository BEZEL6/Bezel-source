# visualization.bezel — Bezel viz ENGINE (scaffold v0.1)
Engine-only Kodi `xbmc.player.musicviz` addon. Gets frequency bins from Kodi core, renders soft textured quads into the
visualisation control rect. Style looks (dust, hair, …) are **data packs in the Bezel skin** at `skin.bezel2/viz.addons/<id>/`.
No C++ in the skin; never rebuilds Kodi UI; no direct touch input (skin → Window(Home) properties only).

## Build (Spectrum-style, needs Kodi addon SDK)
```
git clone https://github.com/xbmc/xbmc kodi
cd kodi && make -C tools/depends/target/binary-addons PREFIX=<kodi>/addons ADDONS="visualization.bezel" ADDON_SRC_PREFIX=/workspace
# or: cmake -DADDONS_TO_BUILD=visualization.bezel -DADDON_SRC_PREFIX=/workspace -DCMAKE_BUILD_TYPE=Release \
#     -DAPP_RENDER_SYSTEM=gles -DCMAKE_INSTALL_PREFIX=<out> <kodi>/cmake/addons
```
Shield/Android: build through Kodi's Android depends toolchain with `APP_RENDER_SYSTEM=gles`.
**Not built on the scaffold box** — no Kodi headers, cmake or C++ compiler present. API details (Start/GetInfo signatures,
window-property reads from a viz) must be checked against the target Kodi version headers on first build.

## Pack path contract
1. setting `pack_root` (absolute, optional) → 2. `special://skin/viz.addons/` → builtin default pack.
Dev tree on box: `/workspace/skin.bezel2.vizsandbox/viz.addons/` (sandbox; set pack_root to it, active_style=hair_ember or solid_test).

## v1 budget (engine-owned caps, `src/Types.h`; not Kodi limits)
- Draw layers: 3–6 (default stack light_behind → haze → dust → strobe/fx → debug), `kMaxLayers = 6`
- Textures: one atlas per pack, ~4–16 soft textures, `kMaxPackTextures = 16`
- Particles are the real throttle: default 400, hard cap 2000 — raise after Shield profiling.

## Stub vs implemented
Implemented (minimal): addon entry, low/mid/high envelopes, particle pool+cap, swirl/push-back/drift, quad batcher
(pass-through shader only, generated glow-disc fallback texture), layer stack, idle modes, settings tuner, path discovery.
Stub: PNG decode (uses generated disc), manifest arrays (layers/textures use defaults; scalar defaults parsed),
real atlas packing, sprite-sheet frames, beat-detected strobes, skin property reads, debug text/fps (log only), warps.

## License
GPL-2.0-or-later (build files/structure derived from visualization.spectrum; see LICENSE.md). New engine code same license.

## Windows / DirectX 11
`APP_RENDER_SYSTEM=dx11` (automatic on WIN32) builds `src/SpritesDX11.cpp` with HLSL in `resources/shaders/DX11/`.
See deliverables/DESKTOP-WINDOWS/WINDOWS-STATUS.md. GL/GLES builds are unchanged.
