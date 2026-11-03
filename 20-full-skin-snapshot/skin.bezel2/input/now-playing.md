# Now playing (dialog 1112) — now-playing

**Object:** `now-playing` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/now-playing.md) · [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [now-playing baselines](../port-refs/now-playing/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/now-playing.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6299 | `60` | `60` | `60` | `60` | `` |
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6396 | `6390` | `SetProperty(bz_noop,1,home)` | `Control.Move(6395,-1)` | `Control.Move(6395,1)` | `6390` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6410` | `6402` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Now Playing is a modal dialog over the music list, so the album sway underneath never resets. Tab/Display toggles it, Back/Left/logo close it, and the main menu can open on top of it. In the Music section, the compact NP rides the album grouplist 6397. Draft: not Rob-approved.
- While music plays in the music list, press Tab (keyboard) or Display (remote) and the Now Playing screen fades in over the list. Press it again, Back, or tap the logo, and it fades away over 1 second, leaving the list exactly where it was. Pressed anywhere else, Tab falls back to Kodi's normal fullscreen.
- Opening without a script.** The keymap opens 1112 directly, with no script start-up delay. The dialog's own onload then checks the gate: is music playing in the music window, list view (not the albums/artists grid), with no visualisation and no MM open?
- Script path.** `bz_cmd.py tab` and `np` (logo menu, 60 s idle) open the same way. First they clear `bz_nav`/`bz_navtune`/`bz_navbez`/`bz_np_was` and put focus back on list 60, so keys move the list after the dialog closes.
- Normal close clears `bz_np` first. The panel's own 1000 ms Visible/Hidden fade runs while the list fades back in (a crossfade). The dialog's WindowClose is a no-op 100→100 hold that just keeps the dialog drawn for that 1 s.
- | Keymap `<music>` | keyboard tab / remote display → `ActivateWindow(1112)` · m / red → `ActivateWindow(1115)` · escape → Back |
- | Keymap `<window1112>` | tab / display → `Dialog.Close(1112)` · m / red → 1115 · escape → Back |
- The big NP block has focus. Left/Right change song, and Select opens the colour-block controls.
- Tapping the top-left logo, or pressing Back, ends Now Playing.
- 6299:** the music window's Back trap. Focusing it closes the dialog.
- 60:** Stands in for the list. When the slide menu's "back to list" target lands here, it clears the MM props and refocuses 6390. That's how the **main menu opens on top of Now Playing**: `BezelNavMenu` is drawn last inside this dialog, so the dialog stays open underneath.
- 2. **Album tap (6381).** An 800×800 hit area. It's visible only when the audio latch is set and there's no back/flip animation. It opens the existing album flip with the dialog still up. The track list is the shared `BezelFlipText` include, and Back returns to proxy 60, which goes to Now Playing.
