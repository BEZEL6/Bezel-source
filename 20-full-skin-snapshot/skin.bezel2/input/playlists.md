# Playlists — playlists

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `playlists` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/playlists.md) · [layout](../layout/playlists.md) · [state](../state/playlists.md) · [motion](../motion/playlists.md) · [art](../art/playlists.md) · [input](../input/playlists.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/playlists.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6409 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6408` | `6411` | `` |
| 9000 | `Close` | `Close` | `noop` | `noop` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. The queue opens from Up next (1115 6409) or the side Playlist button 612. MM PLAYLISTS opens the saved music playlists. Draft: not Rob-approved.
- Up next** in the music controls (or the Playlist side button) shows what's queued now.
- Back returns to where you came from.
- | Queue openers | 1115 `6409` (Up next) · side button `612` |
- ## Section menu (1119) and double-tap
- Menu or double-tap on a queued item gives: Play from here, Item info, Move up, Move down, Remove, Shuffle, Repeat, Save, Clear.
- `musicplaylist` and `videoplaylist` are in `bz_dtap.py` SECW, so a double tap or the context keys open 1119.
- | 7911 | Play from here | `Action(Select)` |
- | 7913 | Move up | `Action(MoveItemUp)` |
- | 7914 | Move down | `Action(MoveItemDown)` |
- The music playlist editor has a button column and two lists. Left and Right move between the buttons and the lists.
- The grouplist and the two scrollbars form a ring: 9000 → right 50 / left 100; scrollbar 60 between 50 and 100; scrollbar 61 between 100 and 9000.
