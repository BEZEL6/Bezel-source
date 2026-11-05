# Music Fanart FS (dialog 1121) — music-fanart-fs

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-fanart-fs` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-fanart-fs.md) · [layout](../layout/music-fanart-fs.md) · [state](../state/music-fanart-fs.md) · [motion](../motion/music-fanart-fs.md) · [art](../art/music-fanart-fs.md) · [input](../input/music-fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
In Music, FULLSCREEN goes to a dialog copy of Fanart FS instead of Kodi's visualisation window. The Music window stays underneath, so the fanart stage and the swaying album never restart. Same look, same keys. Every other section still opens real Kodi visualisation.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-fanart-fs.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6399 | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` | `SetFocus(6398)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6410` | `6402` | `` |
| 6403 | `6402` | `6404` | `6401` | `` | `Dialog.Close(1120)` |
| 6403 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6402` | `6404` | `` |
| 6420 | `PlayerControl(Previous)` | `PlayerControl(Next)` | `6401` | `SetProperty(bz_noop,1,home)` | `6422` |
| 6420 | `RunScript(special://skin/scripts/bz_vizset.py,step,0,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,0,1)` | `6429` | `6421` | `ClearProperty(bz_vizset)` |
| 6421 | `SendClick(6421)` | `SendClick(6421)` | `6420` | `ActivateWindow(1115)` | `6422` |
| 6421 | `RunScript(special://skin/scripts/bz_vizset.py,step,1,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,1,1)` | `6420` | `6422` | `ClearProperty(bz_vizset)` |
| 6422 | `RunScript(special://skin/scripts/bz_vizset.py,step,2,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` | `6421` | `6423` | `ClearProperty(bz_vizset)` |
| 6426 | `RunScript(special://skin/scripts/bz_vizset.py,step,6,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,6,1)` | `6425` | `6427` | `ClearProperty(bz_vizset)` |
| 6429 | `ClearProperty(bz_vizset)` | `` | `6420` | `6420` | `ClearProperty(bz_vizset)` |
| 6886 | `60` | `60` | `60` | `60` | `60` |
| 6910 | `noop` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6960 | `6959` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |

**Semantics from behavior (verbatim lines):**
- Object:** `Custom_1121_MusicFanartFS.xml` dialog `1121` · main `6420` · fan art pill copy `6421` · Back router `6422` · touch `6426`–`6430` · big album pill `6401` (shared include)
- Triggers (when `$EXP[bz_m1121ok]`: Music active, audio, no video, not viz, kill switch off): FS pill `6886`, MM FULL `6960`, old menu Full `6910`, Tab / remote Display in Music, Tuner Back with `bz_tunesrc=fsctrl`. Otherwise the same controls run `ActivateWindow(visualisation)`.
- Play Next copied in: double-Select (or double-tap 6429) clears `bz_pnoff` → album viz. Music's stage slides -1100 (same `bz_at_fsslide` rails as 1120), sides + big album pill draw in 1121. 1120 is never opened (`bz_pndlg_ok` false while 1121 visible).
- Back: album viz → fanart; fanart → close, focus Music list `60`.
- | Select (6420) fanart | 1st: `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01)` + `bz_vdtap=1`; 2nd in 1 s: cancel + `ClearProperty(bz_pnoff)` |
- | Select album viz | pause/resume + `bz_pnfoc=6403` ghost |
- | Left / Right | `PlayerControl(Previous/Next)` |
- | Up | fanart → 6421 · album viz → 6401 |
- | Down | noop |
- | Back / Backspace / B | `SetFocus(6422)` (keymap `<window1121>`) |
- No focus moves into Music from the dialog. Leaving album viz (Back → fanart sets `bz_pnoff`) or closing 1121 drops the condition → Kodi reverses the slide back to 1140.
