# 21-dustviz

Isolated Bezel viz engine plus the DustViz smear pack. Skin trees and `hair_ember` are not modified.

`visualization.bezel/` is the Kodi addon source (folder name matches the addon id).
`viz.addons/topbar_smear/` is the same pack for `special://skin/viz.addons/`.
The addon also carries it at `visualization.bezel/resources/packs/topbar_smear/`. Default `active_style` is `topbar_smear`. If a saved setting is still `solid_test` and that pack is absent, the engine loads the bundled smear pack instead of the solid placeholder.

Styles (`smear_style`): 0 Original (previous column smear), 1 A Cascade (default), 2 B Side whip, 3 C Neon rain, 4 D Fog bloom, 5 E Mirror, 6 F Stagger.
Placement (`smear_place`): 0 Top (falls), 1 Bottom (rises), 2 Mirror (both edges). Style E also keeps a reflection of the other edge.

In-viz tuner uses the existing keymap bridge (`tuner_cmd.py`, `bezelviz_cmd.txt`). T toggles, arrows select/adjust, OK resets the selected row, Back closes. Hair packs still get the previous tuner.

Windows DX11 was not compiled here. See `WINDOWS-VS2022.md`.

## Smoke on this machine

GL OSMesa headless run of this engine (not Kodi, not Windows). `tools/smear_smoke` passed: bundled pack load, cascade top/bottom/mirror energy, tuner toggle/adjust/reset/close. Frames in `tools/shots/*.png` are that runtime, not the concept mock.

Not runtime-tested: Kodi, Windows DX11, Android GLES, a real TV display. GLES shader files are unchanged from 0.2.0.
