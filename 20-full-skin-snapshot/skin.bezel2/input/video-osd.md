# Video OSD — video-osd

**Object:** `video-osd` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/video-osd.md) · [layout](../layout/video-osd.md) · [state](../state/video-osd.md) · [motion](../motion/video-osd.md) · [art](../art/video-osd.md) · [input](../input/video-osd.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/video-osd.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6501 | `Dialog.Close(videoosd)` | `noop` | `6509` | `6502` | `` |
| 6502 | `Dialog.Close(videoosd)` | `noop` | `6501` | `6503` | `` |
| 6503 | `Dialog.Close(videoosd)` | `noop` | `6502` | `6504` | `` |
| 6504 | `Dialog.Close(videoosd)` | `noop` | `6503` | `6505` | `` |
| 6505 | `Dialog.Close(videoosd)` | `noop` | `6504` | `6506` | `` |
| 6506 | `Dialog.Close(videoosd)` | `noop` | `6505` | `6507` | `` |
| 6507 | `Dialog.Close(videoosd)` | `noop` | `6506` | `6508` | `` |
| 6508 | `Dialog.Close(videoosd)` | `noop` | `6507` | `6509` | `` |
| 6509 | `Dialog.Close(videoosd)` | `noop` | `6508` | `6501` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Select in video = pause + OSD. Back is stepped: it hides controls first and only stops on a later press. Draft: not Rob-approved.
- While a video plays, Select pauses it and shows the control column. Left or Back hides the controls again. The pause screen shows whenever the video is paused and the OSD is closed.
- The BEZEL keymap replaces Select in `fullscreenvideo` with `bz_cmd.py vidsel`. That script runs `PlayerControl(Play)` (pause/resume) and then opens `videoosd`.
- | Keymap `<fullscreenvideo>` | keyboard return/enter, remote select → `RunScript(bz_cmd.py,vidsel)` · backspace / remote back / gamepad b / joystick b → `vidback` |
- | Keymap `<videoosd>` | backspace / escape / remote back → `vidback` |
- Nine rows: Play/Pause, Rewind, Fast forward, Stop, Subtitles, Audio, Bookmarks, Settings, Info. Up/Down wraps around, Left closes the OSD and Right does nothing.
- Every row: onleft `Dialog.Close(videoosd)` · onright noop · Up/Down wraps 6509↔6501.
- ## Stepped Back (`vidback`)
- Back never stops the film by accident. The first Back hides whatever controls are showing. Back again, once nothing is on screen, stops playback.
- 4. **Seek bar showing** (`Player.DisplayAfterSeek | Player.Seeking`): treat it as a controls step and re-stamp `bz_vosdc`, **unless** the OSD was closed by Back less than 6 s ago. Closing the OSD leaves Kodi's seek bar briefly on screen, and that leftover shouldn't cost an extra press.
- ## Touch
