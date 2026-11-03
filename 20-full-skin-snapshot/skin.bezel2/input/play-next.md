# Play Next (1120 non-album mode) — play-next

**Object:** `play-next` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/play-next.md) · [layout](../layout/play-next.md) · [state](../state/play-next.md) · [motion](../motion/play-next.md) · [art](../art/play-next.md) · [input](../input/play-next.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/play-next.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6400 | `PlayerControl(Previous)` | `PlayerControl(Next)` | `6401` | `SetProperty(bz_noop,1,home)` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6403 | `6402` | `6404` | `6401` | `` | `Dialog.Close(1120)` |
| 6420 | `PlayerControl(Previous)` | `PlayerControl(Next)` | `6401` | `SetProperty(bz_noop,1,home)` | `6422` |

**Semantics from behavior (verbatim lines):**
- A small pill at the top right switches between **ALBUM** (just the big album) and **PREV/NEXT**, where the previous and next songs' albums show at the sides. The choice is remembered and shared between Dialogue FS and the full-screen album viz.
- Select, Left and Right on the pill all toggle the mode: Reset ↔ SetString album.
- Up and Down return to the window's main control: 6400 on 1120, 6390 on viz.
- On 1120 the pill's Back closes the dialog (`back_close=1`). On viz, Back returns to the main control.
- Select pauses or resumes, and a ghost logo shows while paused.
- Left and Right change song, Up goes to the pill, and Back closes the view.
- When Select pauses, it first sets `bz_pnfoc=6403`, which drives the pause ghost logo. Resuming clears it.
- Down is a deliberate noop.
- Back sets `bz_fsret` for 1 s so the music window knows it's returning from FS, then closes 1120.
- In PREV/NEXT mode, tapping the left or right album plays the previous or next song. A tile only appears when there's a song to go to.
- 6405 and 6406 are touch targets. They're visible only outside album mode and when `MusicPlayer.offset(∓1).Title` exists.
- If a remote lands focus on a tile, it bounces straight back to 6400.
