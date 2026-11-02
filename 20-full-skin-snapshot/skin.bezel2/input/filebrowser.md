# File browser — filebrowser

**Object:** `filebrowser` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/filebrowser.md) · [layout](../layout/filebrowser.md) · [state](../state/filebrowser.md) · [motion](../motion/filebrowser.md) · [art](../art/filebrowser.md) · [input](../input/filebrowser.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/filebrowser.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 450 | `9100` | `9100` | `450` | `9100` | `` |
| 451 | `9100` | `9100` | `451` | `9100` | `` |
| 9100 | `9100` | `9100` | `450` | `450` | `` |

**Semantics from behavior (verbatim lines):**
- Warm strip like 1130/1131/1117: group at 570,120, full-screen 8C dim, `BezelMMStripChrome box=true`. 411 title, 412 path crumb. Panels 450/451: width 390, rows 48, `$VAR[BzATHiTex]`/`BzATHiCol`/`BzATHiText` highlight; folders show », files show size + ✓. Grouplist 9100 is now a horizontal row of np_pill32 pills (413 OK, 414 Cancel, 415/416 when enabled) at y 808. 60 hidden. Nav: 450 Left/Right/Down → 9100; 9100 Up/Down → 450. Footer hint + FileBrowserSelectLabel.
- Simple.** Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.
- Simple.** Up and Down move through the list. Left goes to the buttons. Right goes to the scrollbar. Select opens the folder or picks the item. A double-tap gives Kodi's own context menu.
- How it works.** The dtap keymap includes `filebrowser`. A single Select goes through `bz_dtap` (it fires after the tap window). A second tap inside the window runs `info()`, which for filebrowser is `Action(ContextMenu)` (5.33.99).
- | Control | Left | Right | Up / Down |
