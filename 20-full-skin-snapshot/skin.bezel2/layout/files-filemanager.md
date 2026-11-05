# File manager — files-filemanager

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `files-filemanager` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/files-filemanager.md) · [layout](../layout/files-filemanager.md) · [state](../state/files-filemanager.md) · [motion](../motion/files-filemanager.md) · [art](../art/files-filemanager.md) · [input](../input/files-filemanager.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It opens with a random backdrop. Back at the top of a pane opens the Main Menu.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/files-filemanager.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/files-filemanager.md).

No numbered controls referenced by this object resolve in live XML (object is a Kodi-native window / script-driven). Port as: full-screen view owned by the window listed in the behavior file.
