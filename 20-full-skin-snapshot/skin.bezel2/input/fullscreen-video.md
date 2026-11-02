# Fullscreen video — fullscreen-video

**Object:** `fullscreen-video` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-video.md) · [layout](../layout/fullscreen-video.md) · [state](../state/fullscreen-video.md) · [motion](../motion/fullscreen-video.md) · [art](../art/fullscreen-video.md) · [input](../input/fullscreen-video.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fullscreen-video.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|

**Semantics from behavior (verbatim lines):**
- Simple.** Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.
- How it works.** Kodi opens the window by itself when video starts (4.0.1 O28 restored this; the 4.0.0 bounce-back was removed). The window has no focusable controls (`defaultcontrol` empty), so keys go through the BEZEL keymap to `bz_cmd.py`.
- ## Select
- Wiring.** keymap `fullscreenvideo` select → `bz_cmd.py vidsel` = `PlayerControl(Play)` + `ActivateWindow(videoosd)` (BETA 2.6).
- ## Back
- Simple.** The first Back hides the controls. The next Back stops.
- How it works.** `vidback` checks the layers top-down and removes only the first one it finds. A seek bar that Kodi leaves after the OSD closes does not count as another layer for 6 s. Without that rule you would need an extra Back.
- Wiring.** `bz_cmd.py vidback` (keymap back in `fullscreenvideo` and `videoosd`):
- Unverified:** the np_tab keymap also has a second `FullscreenVideo` block that maps Back → `Action(FullScreen)` (minimise). Which of the two Back maps Kodi applies has not been tested on device.
- The global logo-back button and FS pill are hidden here. Dust is off (dust.md).
- The dtap keymap does not list `fullscreenvideo`, so Select is not double-tap-delayed here.
