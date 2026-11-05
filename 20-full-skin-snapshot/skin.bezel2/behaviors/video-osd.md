# Video OSD

**Object:** video controls · Kodi: `VideoOSD.xml`, buttons `6501`–`6509`, keymap `<fullscreenvideo>` / `<videoosd>` → `bz_cmd.py vidsel` / `vidback`
**Where:** over fullscreen video
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Select pauses the video and shows a control column: Play / Pause, Rewind, Fast forward, Stop, Subtitles, Audio, Bookmarks, Settings, Info. Up / Down wrap; Left or Back hides the column. Back never stops the film by accident: the first Back hides what's showing, the next one (with nothing showing) stops.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| OSD | Select | Left / Back | column of 9 rows |
| Sub-dialog | Subtitles / Audio / Bookmarks / Settings | Back | that dialog |

### Timeline
OSD 300 fade.

### Interruptions
Opening the OSD hides the pause screen at once.

### Continuity
Closing the OSD while paused shows the pause screen again.

### Layering
Video < pause screen (hidden while OSD) < OSD < sub-dialogs.

### Geometry
Column in the strip position.

### Art
—

### Input
Up / Down move (wrap); Select runs; Left closes; Right nothing; Back stepped.

### Speed targets
—

### Never
No accidental stop on the first Back.

### Acceptance checks
Select → OSD → Down × 4 → Subtitles; Back → OSD; Back → closed; Back → stop.

## Kodi implementation (sandbox)

### How it works (live detail; dated sections are the current state unless a later one supersedes them)
#### Open / close

##### Simple
While a video plays, Select pauses it and shows the control column. Left or Back hides the controls again. The pause screen shows whenever the video is paused and the OSD is closed.

##### How it works
- The BEZEL keymap replaces Select in `fullscreenvideo` with `bz_cmd.py vidsel`. That script runs `PlayerControl(Play)` (pause/resume) and then opens `videoosd`.
- Opening the OSD hides the pause screen (1116 is gated on `!Window.IsActive(videoosd)`).
- The OSD fades in and out over 300 ms. Focus always starts on Play/Pause.

##### Wiring
| Item | Value |
|---|---|
| Window anim | WindowOpen fade 0→100, 300 ms sine out · WindowClose 100→0, 300 ms sine in |
| defaultcontrol | `always` 6501 |
| Keymap `<fullscreenvideo>` | keyboard return/enter, remote select → `RunScript(bz_cmd.py,vidsel)` · backspace / remote back / gamepad b / joystick b → `vidback` |
| Keymap `<videoosd>` | backspace / escape / remote back → `vidback` |
| `vidsel` | `PlayerControl(Play)` + `ActivateWindow(videoosd)` |

---

#### Rows and keys

##### Simple
Nine rows: Play/Pause, Rewind, Fast forward, Stop, Subtitles, Audio, Bookmarks, Settings, Info. Up/Down wraps around, Left closes the OSD and Right does nothing.

##### How it works
- The rows are plain buttons in a fixed vertical chain, wrapping 6509↔6501.
- The sub-pages (subtitles, audio, video settings, bookmarks) are Kodi's own OSD dialogs. While any of those is open, the pause screen stays hidden.

##### Wiring
| ID | Label | onclick |
|---|---|---|
| 6501 | `$VAR[BzOSDPlayLbl]` | `PlayerControl(Play)` |
| 6502 | Rewind | `PlayerControl(Rewind)` |
| 6503 | Fast forward | `PlayerControl(Forward)` |
| 6504 | Stop | `PlayerControl(Stop)` |
| 6505 | Subtitles | `ActivateWindow(osdsubtitlesettings)` |
| 6506 | Audio | `ActivateWindow(osdaudiosettings)` |
| 6507 | Bookmarks | `ActivateWindow(videobookmarks)` |
| 6508 | Settings | `ActivateWindow(osdvideosettings)` |
| 6509 | Info | `Action(Info)` |

- Every row: onleft `Dialog.Close(videoosd)` · onright noop · Up/Down wraps 6509↔6501.

---

#### Stepped Back (`vidback`)

##### Simple
Back never stops the film by accident. The first Back hides whatever controls are showing. Back again, once nothing is on screen, stops playback.

##### How it works
`bz_cmd.py vidback` checks the screen in order and does only the first match:
1. **OSD visible:** stamp `bz_vosdc` = now and close the OSD.
2. **`fullscreeninfo` visible:** close it.
3. **`Player.ShowInfo`:** send `Action(Info)` to hide the info bar.
4. **Seek bar showing** (`Player.DisplayAfterSeek | Player.Seeking`): treat it as a controls step and re-stamp `bz_vosdc`, **unless** the OSD was closed by Back less than 6 s ago. Closing the OSD leaves Kodi's seek bar briefly on screen, and that leftover shouldn't cost an extra press.
5. **Nothing showing:** `PlayerControl(Stop)`.

##### Wiring
- `scripts/bz_cmd.py` `vidback` (~L532).
- Home prop `bz_vosdc` = float time.
- 6 s grace window.

---

#### Touch
None specified.

### Wiring
See the detail above.

### Kodi workarounds (do not port)
Stepped Back implemented by a script reading what is visible.

## Related
[fullscreen-video](fullscreen-video.md) · [pause-overlay](pause-overlay.md) · [keymaps](keymaps.md)
