# Fullscreen video — fullscreen-video

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `fullscreen-video` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-video.md) · [layout](../layout/fullscreen-video.md) · [state](../state/fullscreen-video.md) · [motion](../motion/fullscreen-video.md) · [art](../art/fullscreen-video.md) · [input](../input/fullscreen-video.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fullscreen-video.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/fullscreen-video.md).

No numbered controls referenced by this object resolve in live XML (object is a Kodi-native window / script-driven). Port as: full-screen view owned by the window listed in the behavior file.
