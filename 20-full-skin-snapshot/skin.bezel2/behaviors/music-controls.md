# Music controls

**Object:** the music "remote control" panel · Kodi: dialog `1115` (`Custom_1115_MusicControls.xml`, zorder 2, `DepthOSD`) · rows `6401`–`6413` · viz settings page `6420`–`6427` + Back `6429` · `scripts/bz_vizset.py`
**Where:** over Music, fullscreen music and Dialogue FS while audio plays; column at x 570
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
A column of 13 rows over a dimmed screen: Play / Pause, Last, Next, Rewind, Fast forward, Stop, Shuffle, Repeat, Up next, Visualisation, Viz settings, TUNER, Close. It opens when Kodi would show its music OSD, with Menu / Red in fullscreen, from the cycle pill's Controls mode, and with Right from the Music list. Up / Down move (wrapping). Left closes. Right closes, or in Music slides the big album into Dialogue FS. Viz settings swaps the column for the current visualisation's own settings. TUNER jumps into the BEZEL Tuner, and Back from there returns here.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Rows | open | Left / Back / Close row / tap outside | dim backdrop, title PLAYER CONTROLS, column of rows, focus on Play / Pause |
| Viz settings | Viz settings row | Back / ‹ Back row | header VIZ SETTINGS · name, up to 8 rows `label ‹ value ›` |
| No viz settings | Viz settings with none | Back | "No settings for this visualisation" |
| Handed to Tuner | TUNER row | Tuner Back | Tuner over the MM |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| open | panel fades in; column rises 30 px into place | 250 | sine out (fade), cubic (rise) |
| close | panel fades out; column drifts 20 px up | 420 | sine in-out |
| Visualisation row | panel closes, then Kodi's visualisation picker opens 1 s later | — | — |

### Interruptions
- Right to Dialogue FS: the panel closes instantly (no fade) so the album slide starts at once.
- Rows that open another screen (Up next, Visualisation) close the panel first: nothing stacks under it.

### Continuity
- Every open starts on Play / Pause and on the main rows (never on the viz page).
- Closing while the cycle pill was on Controls returns the pill to Visualizer.

### Layering
Screen below < full-screen dim (840 × 900 at 120,120 + tap-to-close area) < column < system dialogs.

### Geometry
| Piece | Value |
|---|---|
| Column | 570, 120, 390 × 900 (the strip position) |
| Title | 570, 66 |
| Dim block | 120, 120, 840 × 900 |

### Art
Column: solid near-black (#0E0F12) backing + the strip colour; section labels PLAYBACK / MODE / MORE; focus pill. Title with a soft shadow (Tuner can switch shadows off).

### Input
| Action | Result |
|---|---|
| Up / Down | move, wraps Close ↔ Play / Pause |
| Select | run the row |
| Left | close |
| Right | Music + playing + allowed: Dialogue FS; else close |
| Viz page Left / Right | step the value |
| Viz page Back | main rows, focus Viz settings |
| Tap outside | close |

### Speed targets
Panel visible within 250 ms; row actions immediate.

### Never
- No stuck viz settings page on reopen: every open starts on the main rows (463 VIZSETRESET).
- Tuner re-entry must work after a Tuner Back (469 TUNERREOPEN).

### Acceptance checks
1. Fullscreen → Menu → panel; Down × 3 wraps correctly; Left closes.
2. Viz settings → close → reopen → main rows.
3. TUNER → Tuner → Back → back here; TUNER again → Tuner opens.
4. Music list → Right → panel → Right → Dialogue FS.

## Kodi implementation (sandbox)

### How it works
- **Openers.** `MusicOSD.xml` onload (`Player.HasAudio`), `PlayerControls.xml` onload (`!fullscreenvideo + Player.HasAudio`), list 60 onright in Music (`bz_vback` empty, NP button 6160 visible), cycle pill Down in Controls mode (6391 / 6421), keymap m / red in 1121 and viz, `bz_cmd.py npctl` (toggle; fullscreen video → `videoosd`).
- **Right → Dialogue FS.** Every row's `onright` with `$EXP[bz_pndlg_ok]`: `Close(1115,true)` → `bz_rail=centre` → `ActivateWindow(1120)`; else close.
- **Visualisation row.** `Dialog.Close(1115)` → `AlarmClock(bzviz,Addon.Default.Set(xbmc.player.musicviz),00:01)` (picker after the close starts).
- **Viz settings.** 6412: `SetProperty(bz_vizset,1,1115)` → `bz_vizset.py load` → focus 6420. The script reads the active viz (JSON-RPC `musicplayer.visualisation`), its `resources/settings.xml` (integer / number / boolean, max 8, options from `<option>`, min / max / step defaults 0 / 100 / 1) and publishes `bz_vsN_lab` / `bz_vsN_val` on the dialog. Steps write at once with `addon.setSetting`. Down skips empty rows to 6429.
- **Page reset.** `bz_vizset` is always addressed to window 1115 and cleared on load and unload (463).
- **TUNER row.** `bz_tunesrc=fsctrl` → close → `ActivateWindow(home)` → `bz_nav` + `bz_navtune` → `AlarmClock(bz_tunf,SetFocus(6970))`. Tuner rail Back with `fsctrl`: clear `bz_nav` / `bz_navtune` / `bz_tunesrc` first, then 1121 (or viz) + 1115 (469).
- **onunload:** clear `bz_vizset`; `bz_npmode=controls` → `vis`.

### Wiring
| Id | Row | onclick |
|---|---|---|
| 6401 | Play / Pause | `PlayerControl(Play)` |
| 6402 / 6403 | Last / Next | `PlayerControl(Previous / Next)` |
| 6404 / 6405 | Rewind / Fast forward | `PlayerControl(Rewind / Forward)` |
| 6406 | Stop | `PlayerControl(Stop)` |
| 6407 / 6408 | Shuffle / Repeat | `PlayerControl(Random / Repeat)` |
| 6409 | Up next | close + `ActivateWindow(musicplaylist)` |
| 6411 | Visualisation | close + 1 s picker alarm |
| 6412 | Viz settings | page (above) |
| 6413 | TUNER | hand-off (above) |
| 6410 | Close controls | `Dialog.Close(1115)` |
| Chain | 6401 ↔ … ↔ 6408 ↔ 6409 ↔ 6411 ↔ 6412 ↔ 6413 ↔ 6410 ↔ 6401 (wraps); every row onleft = close |
| Anim | WindowOpen fade 250 sine out; column slide 0,30 → 0 250 cubic; WindowClose fade 420 sine in-out, slide 0 → 0,−20 |
| defaultcontrol | `always` 6401 |

### Kodi workarounds (do not port)
- Hijacking `MusicOSD` / `PlayerControls` onload: the only way to replace Kodi's OSD.
- The 1 s alarm before the viz picker: avoids a race with the closing dialog.
- Window-scoped `bz_vizset`: Kodi's unscoped SetProperty targets the focused window.
- `Close(1115,true)` before 1120: modal ordering.

## Related
[music-viz-settings](music-viz-settings.md) · [dialogue-fs](dialogue-fs.md) · [music-fanart-fs](music-fanart-fs.md) · [skin-settings-tuner](skin-settings-tuner.md)
