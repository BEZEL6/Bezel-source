# Fanart FS (visualisation) — fanart-fs

**Object:** `fanart-fs` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fanart-fs.md) · [layout](../layout/fanart-fs.md) · [state](../state/fanart-fs.md) · [motion](../motion/fanart-fs.md) · [art](../art/fanart-fs.md) · [input](../input/fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fanart-fs.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6299 | `60` | `60` | `60` | `60` | `` |
| 6391 | `6390` | `6392` | `6390` | `ActivateWindow(1115)` | `ClearProperty(bz_np,home)` |
| 6401 | `Skin.Reset(bz_dfs_mode)` | `Skin.Reset(bz_dfs_mode)` | `$PARAM[main]` | `$PARAM[main]` | `SetProperty(bz_fsret,true,home)` |
| 6401 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6410` | `6402` | `` |
| 6403 | `6402` | `6404` | `6401` | `` | `Dialog.Close(1120)` |
| 6403 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6402` | `6404` | `` |
| 6407 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6406` | `6408` | `` |
| 6408 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6407` | `6409` | `` |
| 6409 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6408` | `6411` | `` |
| 6410 | `Dialog.Close(1115)` | `Dialog.Close(1115,true)` | `6413` | `6401` | `` |
| 6886 | `60` | `60` | `60` | `60` | `60` |
| 6960 | `6959` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |

**Semantics from behavior (verbatim lines):**
- Object:** `MusicVisualisation.xml` (Kodi `visualisation`) · default `6390` (BezelNPInPlace, Includes_Bezel ~2896, 120,120, 840×900) · **fan art pill** `6391` (~2956, fanart only) · **big album pill** `6401` (album viz) · hidden redirects `6297`, `6299`, `6385`, `60` · touch `6407`/`6408`, `6409`/`6410`
- Status:** draft. This doc matches the live tree. 6409 click = pause, double = album viz. Right = next via keymap (5.33.205). Rob has not approved it.
- Simple.** Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.
- How it works.** One Home prop decides the view: `bz_pnoff=1` means plain Fanart FS (sides off). Empty means album viz. `onload` always sets `bz_pnoff=1`, so every visit starts in fanart. Back is routed by the keymap to `6297`. If album viz is showing, 6297 sets `bz_pnoff=1` (drop to fanart, no exit anim). If fanart is already showing, it runs a real `Action(Back)` (5.33.108 t732).
- Wiring.** `6297` `onfocus`: `!bz_pnoff=1` → `SetProperty(bz_pnoff,1,home)`, else `Action(Back)`. Then `SetFocus(6390)`.
- `6299` `onfocus` → `ClearProperty(bz_np,home)` + `Action(Back)`. `6385` → focus 6390 + `bz_cmd.py npctl,toggle`. `60` → focus 6390.
- Simple.** Select pauses (one tap) or opens album viz (two taps). Left = previous song. Right = next song, everywhere. Up = the pill. M/RED = Music controls.
- How it works.** In fanart, the first Select does not pause at once. It arms a 1 s alarm that pauses and sets `bz_vdtap=1`. A second Select inside that second cancels the alarm and clears `bz_pnoff` (album viz). `bz_vdtap` clears after 1 s either way. There is no `NextPreset` on this path. In album viz, Select pauses at once and shows the ghost logo. Right is taken by the keymap before the skin sees it, so the XML `onright` handlers of 6390 and 6391 never fire in viz.
- | Select on 6390, fanart | 1st: `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01,silent)` + `bz_vdtap=1`. 2nd within 1 s: `CancelAlarm(bz_vdtapgo,true)` + `ClearProperty(bz_pnoff)` + `bz_vdtap=2` |
- | Select on 6390, album viz | `!Paused` → `bz_pnfoc=6403`, else clear. Then `PlayerControl(Play)` |
- | Left on 6390 | `PlayerControl(Previous)` |
- | Right (anywhere) | keymap `<visualisation>` → `PlayerControl(Next)` |
