# File manager — files-filemanager

**Object:** `files-filemanager` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/files-filemanager.md) · [layout](../layout/files-filemanager.md) · [state](../state/files-filemanager.md) · [motion](../motion/files-filemanager.md) · [art](../art/files-filemanager.md) · [input](../input/files-filemanager.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It opens with a random backdrop. Back at the top of a pane opens the Main Menu.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/files-filemanager.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|

**Semantics from behavior (verbatim lines):**
- Simple.** It opens with a random backdrop. Back at the top of a pane opens the Main Menu.
- How it works.** It has no `always` default, so Kodi gives focus back to the pane you last used (5.33.145 BUG-002). The pane `onback` only opens the MM when that pane has no folder (the source list). Inside a folder, Back is Kodi's parent step.
- Simple.** It has two lists in the same spot. The one you are not using slides left and dims, so the active pane is always in front.
- Wiring.** Lists 20 and 21: left 570, top 120, 390×900. Unfocused animation: slide to -450,0 and fade to 45 over 200 ms (sine). `pagecontrol` 60/61, `scrolltime` 200. Scrollbars 60/61 at left -400 (offscreen).
- Simple.** Left and Right swap panes. Up and Down move within a pane. Select opens. A double-tap gives Kodi's context menu (copy/move/delete).
- | Left / Right | 21 | 20 |
- | Up / Down | 20 | 21 |
- | Double-tap | `bz_dtap.info()` → `Action(ContextMenu)` | same |
