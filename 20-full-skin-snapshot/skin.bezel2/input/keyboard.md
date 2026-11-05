# Keyboard (DialogKeyboard 10103) — keyboard

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `keyboard` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keyboard.md) · [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid). - File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob. - Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKe

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keyboard.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 300 | `8` | `9603` | `9603` | `9603` | `` |
| 312 | `9601` | `9601` | `9601` | `9601` | `` |
| 9601 | `SetProperty(bz_kbcaps,1,home)` | `9602` | `9601` | `9601` | `` |
| 9602 | `9601` | `9603` | `9602` | `9602` | `` |
| 9603 | `9602` | `300` | `9603` | `9603` | `` |

**Semantics from behavior (verbatim lines):**
- File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob.
- Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKeyboard`: vbar keyboard left of the colour strip, focus on A–Z 9601.
- Bars 9601 A–Z / 9602 0–9 / 9603 symbols (wraplists, focus row 5). Select → `bz_kb.py` appends the char via JSON `Input.SendText` (done=false) to the text read from `Control.GetLabel(312).index(1)`. Pills 32 SPACE, 8 DEL, 300 DONE. Caps: Left on the A–Z bar 9601 toggles Home `bz_kbcaps` (letters redraw upper/lower; no caps pill since 5.33.231). Digits use `$NUMBER[n]` labels (a bare number label is read as a localized string id).
