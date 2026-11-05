# Big album pill — big-album-pill

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `big-album-pill` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/big-album-pill.md) · [layout](../layout/big-album-pill.md) · [state](../state/big-album-pill.md) · [motion](../motion/big-album-pill.md) · [art](../art/big-album-pill.md) · [input](../input/big-album-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The **big album pill** is the ALBUM ↔ PREV/NEXT mode control. It looks the same, sits in the same place and works the same on Dialogue FS and on full screen album viz. It is **not** the fan art pill (`6391`, fanart-fs.md).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/big-album-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6400 | `PlayerControl(Previous)` | `PlayerControl(Next)` | `6401` | `SetProperty(bz_noop,1,home)` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |

**Semantics from behavior (verbatim lines):**
- Where:** Upper right, grouplist at 1360,60, 500×32, aligned right
- Simple.** Select, Left or Right flips the mode. Up or Down goes back to the album. Back closes Dialogue FS, or goes back to the album in viz.
- How it works.** All three toggle keys use the same two guarded actions. If the mode is `album` they reset it, otherwise they set `album`. `back_close=1` (1120 only) runs the Dialogue FS close latch: `bz_fsret=true` for 1 s, then `Dialog.Close(1120)`. The latch holds the left stage off-frame until the side fade finishes. With `back_close` empty (viz), Back just focuses `main`.
- Wiring.** `vis=[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + Player.HasAudio`, `main=6390`. 6390 `onup` → 6401 when `bz_pnoff≠1`, else 6391. The touch side hits `6407`/`6408` (`Playlist.PlayOffset(music,∓1)`) need PREV/NEXT mode and an existing neighbour track.
