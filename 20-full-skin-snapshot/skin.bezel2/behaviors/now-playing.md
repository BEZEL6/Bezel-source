# Now playing (dialog 1112)

**Object:** `Custom_1112_NowPlaying.xml` dialog `1112` (zorder 1) · keymap `bezel2_np_tab.xml` (`<music>`, `<window1112>`) · `bz_cmd.py tab` / `np` / `npctl`
**Where:** Over the Music window list view while music plays
**Last updated:** 2026-11-02 · 5.33.309
**Status:** Live in 5.33.207. Now Playing is a modal dialog over the music list, so the album sway underneath never resets. Tab/Display toggles it, Back/Left/logo close it, and the main menu can open on top of it. In the Music section, the compact NP rides the album grouplist 6397. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
While music plays in the music list, press Tab (keyboard) or Display (remote) and the Now Playing screen fades in over the list. Press it again, Back, or tap the logo, and it fades away over 1 second, leaving the list exactly where it was. Pressed anywhere else, Tab falls back to Kodi's normal fullscreen.

### How it works
- **Opening without a script.** The keymap opens 1112 directly, with no script start-up delay. The dialog's own onload then checks the gate: is music playing in the music window, list view (not the albums/artists grid), with no visualisation and no MM open?
  - **Gate fails** (and `bz_np` isn't already true): the dialog closes itself instantly and opens Kodi's `visualisation`, the old fullscreen path.
  - **Gate passes:** it sets `bz_npdlg` and `bz_np`.
- **Gate input.** The gate uses `Player.HasAudio` directly, not the debounced `bz_audio_latch`. On the first Tab after Kodi starts, the latch may not be set yet.
- **Script path.** `bz_cmd.py tab` and `np` (logo menu, 60 s idle) open the same way. First they clear `bz_nav`/`bz_navtune`/`bz_navbez`/`bz_np_was` and put focus back on list 60, so keys move the list after the dialog closes.
- **Closing, two fades:**
  - Normal close clears `bz_np` first. The panel's own 1000 ms Visible/Hidden fade runs while the list fades back in (a crossfade). The dialog's WindowClose is a no-op 100→100 hold that just keeps the dialog drawn for that 1 s.
  - If Tab/Display closes it directly with `bz_np` still true, the whole dialog fades 100→0 over 1000 ms (sine in-out).
- **Unload.** `bz_np` is cleared unless the next window is visualisation, and `bz_npdlg` is always cleared.

### Wiring
| Item | Value |
|---|---|
| Keymap `<music>` | keyboard tab / remote display → `ActivateWindow(1112)` · m / red → `ActivateWindow(1115)` · escape → Back |
| Keymap `<window1112>` | tab / display → `Dialog.Close(1112)` · m / red → 1115 · escape → Back |
| onload (gate false and `bz_np`≠true) | `Dialog.Close(1112,true)` · `ActivateWindow(visualisation)` |
| onload (gate true) | `SetProperty(bz_npdlg,true,home)` · `SetProperty(bz_np,true,home)` |
| onunload | `!visualisation` → `ClearProperty(bz_np)` · `ClearProperty(bz_npdlg)` |
| defaultcontrol | `always` 6390 (NP block, Includes_Bezel ~L2896) |
| WindowClose | `bz_np`≠true: fade 100→100, 1000 ms (hold) · `bz_np`=true: 100→0, 1000 ms sine inout |
| `bz_cmd.py tab` | 1112 open → clear `bz_np`, close · gate ok (+`bz_audio_latch`, `!System.HasModalDialog`) → open as above · else `Action(FullScreen)` |

---

## Controls inside the dialog

### Simple
- The big NP block has focus. Left/Right change song, and Select opens the colour-block controls.
- Tapping the album does nothing in Now Playing (the track-list flip is deleted, 5.33.309).
- Tapping the top-left logo, or pressing Back, ends Now Playing.

### How it works
1. **Hidden proxies.** Several invisible buttons sit off-screen at x −400. They catch the IDs the shared panel include names when it moves focus:
   - **6299:** the music window's Back trap. Focusing it closes the dialog.
   - **6385:** NP toggle. It refocuses 6390 and runs `npctl`.
   - **60:** Stands in for the list. When the slide menu's "back to list" target lands here, it clears the MM props and refocuses 6390. That's how the **main menu opens on top of Now Playing**: `BezelNavMenu` is drawn last inside this dialog, so the dialog stays open underneath.
2. **Album tap (6381):** deleted in 5.33.309 with the track-list flip.
3. **6390 block:**
   - Back clears `bz_np` and goes to 6299, which closes the dialog.
   - Left → Previous.
   - Up → 6401 (or the mode pill 6391 when `bz_pnoff=1`).
   - Down → Up Next proxy 6396 in that mode, otherwise noop.
4. **`npctl`.** Despite the `toggle` argument, it opens 1115 (the music controls), or closes 1115 if it's already open. In fullscreen video it opens `videoosd` instead.

### Wiring
| ID | Role |
|---|---|
| 6381 | album tap; visible `bz_audio_latch` + empty `bz_back`/`bz_flipping`/`bz_backanim` |
| 6387 | logo hit 120×116 at 0,0 → `ClearProperty(bz_np)` + `Dialog.Close(1112)` |
| 6299 | onfocus → clear `bz_np` + close |
| 6385 | onfocus → `SetFocus(6390)` + `bz_cmd.py npctl,toggle` |
| 60 | onfocus → clear `bz_nav`/`bz_navtune`/`bz_navbez` + `SetFocus(6390)` |
| Includes | `BezelSecDim` (parent group), `BezelNPControls` (vis `$EXP[bz_np] + bz_npctl`), `BezelFlipText`, `BezelNavMenu` (drawn last) |
| Slide | inner group slides −1100 px when 1120 / `bz_fsret` by `bz_at_fsslide` (480/380/… ms sine) |

---

## Music section compact NP

### Simple
In the Music section itself (no dialog), the compact now-playing view travels with the big album as one piece.

### How it works
- The compact NP rides album grouplist `6397` with the big album. It slides at the album rail's `bz_at_fsslide` speed, with no separate −1100 px slide and no 1120 fade.
- In the music window, `bz_np_focus=true` on load focuses 6390. See np-bar.md, music-list.md and dialogue-fs.md.

### Wiring
- Album rails: grouplists 6367 / 6377 / 6397 / 6382 (scrolltime 480 / 380 / 280 / 180 for fsslide 1 / 2 / empty-or-3 / 4).
- `$EXP[bz_np]` = `bz_np`=true + [music window | `bz_fsnp`] + `bz_audio_latch` + `!Player.HasVideo`.

---

## Keys
| Key | Behavior |
|---|---|
| Tab / Display | Toggle 1112 (gate) |
| M / Red | Music controls 1115 |
| Left / Right | Previous / Next (6390) |
| Up | 6401 (or pill 6391) |
| Back | Clear `bz_np` → 6299 → close |
| Esc | Back (so the slide menu closes first) |

## Touch
Album tap 6381 = flip. Logo tap 6387 = close.

## Related
np-bar.md · music-controls.md · music-list.md · dialogue-fs.md · keymaps.md

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [screens](../port-refs/now-playing/) · [PORT_INDEX](../PORT_INDEX.md)


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## Over Music Level 2 / 3 (5.33.324)
Opening Now Playing over the L2 album list or L3 song list fades the shared strip small album out with the list rows and meta (bz_np Conditional fade, 1000 ms sine). See music-list.md.
