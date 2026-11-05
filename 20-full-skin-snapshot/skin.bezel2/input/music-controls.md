# Music controls (dialog 1115) — music-controls

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-controls` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-controls.md) · [layout](../layout/music-controls.md) · [state](../state/music-controls.md) · [motion](../motion/music-controls.md) · [art](../art/music-controls.md) · [input](../input/music-controls.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-controls.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6160 | `60` | `60` | `60` | `60` | `` |
| 6369 | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` |
| 6379 | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` |
| 6384 | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` |
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6399 | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6410` | `6402` | `` |
| 6402 | `6404` | `6403` | `6401` | `` | `Dialog.Close(1120)` |
| 6402 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6401` | `6403` | `` |
| 6403 | `6402` | `6404` | `6401` | `` | `Dialog.Close(1120)` |
| 6403 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6402` | `6404` | `` |
| 6404 | `6403` | `6402` | `6401` | `` | `Dialog.Close(1120)` |
| 6404 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6403` | `6405` | `` |
| 6405 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6404` | `6406` | `` |
| 6406 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6405` | `6407` | `` |
| 6407 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6406` | `6408` | `` |
| 6408 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6407` | `6409` | `` |
| 6409 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6408` | `6411` | `` |
| 6410 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6413` | `6401` | `` |
| 6411 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6409` | `6412` | `` |
| 6412 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6411` | `6413` | `` |
| 6413 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6412` | `6410` | `` |
| 6420 | `RunScript(special://skin/scripts/bz_vizset.py,step,0,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,0,1)` | `6429` | `6421` | `ClearProperty(bz_vizset)` |
| 6427 | `RunScript(special://skin/scripts/bz_vizset.py,step,7,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,7,1)` | `6426` | `6429` | `ClearProperty(bz_vizset)` |
| 6429 | `ClearProperty(bz_vizset)` | `` | `6420` | `6420` | `ClearProperty(bz_vizset)` |
| 6600 | `60` | `` | `` | `` | `60` |
| 6600 | `SetProperty(bz_nav,true,home)` | `` | `` | `` | `60` |
| 6970 | `SetProperty(bz_tune_dirty,1,home)` | `SetProperty(bz_tune_dirty,1,home)` | `noop` | `noop` | `ClearProperty(bz_navtune,home)` |

**Semantics from behavior (verbatim lines):**
- Where:** Over Music / visualisation / Dialogue FS while audio plays. Right-hand panel at x 570
- Status:** Live in 5.33.207. Transport rows, the Viz settings sub-page, the TUNER hand-off and Right → Dialogue FS all work as described here. Draft: Rob hasn't approved or re-smoked it.
- The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.
- From the Music list, **Right** on list 60 opens 1115 when no vback card is up, no grid (6600) is visible, and the NP button 6160 is visible.
- From the fan art pill (6391) in full-screen viz, **Down** opens 1115 when NP mode is `controls`. Otherwise it focuses 6390.
- The panel fades in for 250 ms and the column slides up from 30 px below. On close it fades out over 420 ms and drifts 20 px. Focus always starts on Play/Pause (`defaultcontrol always`).
- Thirteen rows in three blocks. Up/Down moves and wraps from Close back to Play. Left closes the panel. Right either jumps to the big Dialogue FS screen (when that makes sense) or just closes.
- Every row runs a Kodi `PlayerControl` or window action. Up next and Visualisation close the panel first, so the next window isn't stacked under a dialog.
- Right checks `$EXP[bz_pndlg_ok]`. When it's true: close 1115 without animation (`Close(1115,true)`), then put focus on the album-rail slot that matches the current slide speed, then open 1120. The focus must land first, because 1120's slide-in starts from the focused rail.
- | 6409 | Up next | Close + `ActivateWindow(musicplaylist)` |
- Up/Down chain: 6401↔6402↔…↔6408↔6409↔6411↔6412↔6413↔6410↔6401 (wraps).
- TUNER jumps straight into the BEZEL Tuner on the main menu. Back from the Tuner returns you to the visualisation with this panel open again.
