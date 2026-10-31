# Music controls

**Object:** `Custom_1115_MusicControls.xml` dialog `1115` (zorder 2) · buttons `6401–6413`, viz-settings rows `6420–6429`; `scripts/bz_vizset.py`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Transport and options dialog for music. Opened from the fan art pill 6391 (Controls mode Select, or Down in viz / controls mode) or from Dialogue FS.

## Rows (Up/Down wraps 6410 ↔ 6401)
Play/Pause 6401 · Last 6402 · Next 6403 · Rewind 6404 · FF 6405 · Stop 6406 · Shuffle 6407 (Random) · Repeat 6408 · Up next 6409 (→ musicplaylist) · Visualisation 6411 (choose viz) · Viz settings 6412 · TUNER 6413 · Close controls 6410.

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move (wraps) |
| Left | Close 1115 |
| Right | If `$EXP[bz_pndlg_ok]`: close 1115, focus the album rail for `bz_at_fsslide` (1→6369, 2→6379, 3/empty→6399, 4→6384) and open 1120 (Dialogue FS). Otherwise close |
| Select on 6412 | `bz_vizset=1`, `bz_vizset.py load`, focus 6420 |
| Left / Right on 6420–6429 | `bz_vizset.py step,n,∓1` (change viz setting n) |
| Back in viz settings | Clear `bz_vizset`, focus 6412 |
| Select TUNER 6413 | `bz_tunesrc=fsctrl`, close, Home + MM Tuner (`bz_navtune`) |

onunload: clears `bz_vizset`; if `bz_npmode=controls` it resets to `vis`.

## Related
fanart-fs.md · dialogue-fs.md · music-viz-settings.md · skin-settings-tuner.md
