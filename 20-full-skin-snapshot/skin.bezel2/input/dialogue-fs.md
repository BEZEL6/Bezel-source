# Dialogue FS — dialogue-fs

**Object:** `dialogue-fs` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialogue-fs.md) · [layout](../layout/dialogue-fs.md) · [state](../state/dialogue-fs.md) · [motion](../motion/dialogue-fs.md) · [art](../art/dialogue-fs.md) · [input](../input/dialogue-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Tap the big album in Music, or press Right from Music controls, and the album slides out to a full-screen album view. Back slides it home again.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/dialogue-fs.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6369 | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` | `SetFocus(6368)` |
| 6379 | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` | `SetFocus(6378)` |
| 6384 | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` | `SetFocus(6383)` |
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6399 | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` |
| 6400 | `PlayerControl(Previous)` | `PlayerControl(Next)` | `6401` | `SetProperty(bz_noop,1,home)` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6403 | `6402` | `6404` | `6401` | `` | `Dialog.Close(1120)` |

**Semantics from behavior (verbatim lines):**
- Object:** `Custom_1120_PlayNext.xml` dialog `1120` · main `6400` (660,220, 600×600) · **big album pill** `6401` (shared `BezelBigAlbumPill`) · touch sides `6405`/`6406` · side albums `BezelFSPlayNext` · album grouplist `6397`
- Where:** Music section, over the left fanart stage
- Simple.** Tap the big album in Music, or press Right from Music controls, and the album slides out to a full-screen album view. Back slides it home again.
- How it works.** From the Music section, Right or Select on the NP control `6390` (when `$EXP[bz_pndlg_ok]`) first focuses the album rail button for the current slide speed (6369/6379/6399/6384), then `ActivateWindow(1120)`. The left stage then slides -1100 px at the Tuner slide speed. On Back, 6400 sets the `bz_fsret` latch, which holds the LeftStage off-frame for about 1 s, and then closes 1120. That lets the side fade (600 ms) finish before the reverse slide starts, so no half-faded album slides back. On unload, focus goes back to the rail button that matches the slide speed, so the strip lands on the same row it left from.
- Simple.** Select pauses or resumes and shows a ghost logo. Left and Right change song. Up goes to the big album pill. Down does nothing.
- How it works.** Select checks whether the player is paused before toggling. Going into pause sets `bz_pnfoc=6403`, which shows the pause logo. Resuming clears it. The CEC-repeat guard of 5.33.115 was replaced by this single action (5.33.116 t807).
- | Select | `!Player.Paused` → `SetProperty(bz_pnfoc,6403,home)`; paused → `ClearProperty(bz_pnfoc,home)`; then `PlayerControl(Play)` |
- | Left / Right | `PlayerControl(Previous)` / `PlayerControl(Next)` |
- | Up | `6401` |
- | Down | `SetProperty(bz_noop,1,home)` (noop) |
- | Back | fsret latch + close (above) |
- Simple.** Upper right: ALBUM ↔ PREV/NEXT. Select, Left or Right flips it. Up or Down returns to 6400. Back closes 1120 with the same latch. Full spec: big-album-pill.md. It is not the fan art pill `6391`.
