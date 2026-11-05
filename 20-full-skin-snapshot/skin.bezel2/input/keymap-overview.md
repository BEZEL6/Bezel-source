# Keymap & action vocabulary

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state · [PORT_INDEX](../PORT_INDEX.md) · behavior: [keymaps](../behaviors/keymaps.md)

## Simple
Bezel uses standard remote keys (Up/Down/Left/Right/Select/Back) plus a few specials: **Tab/Display** = Now Playing / Fanart FS, **M / Red** = Music Controls, **hold Select** (or double-tap) = Options+Info, **Esc** = Back. A port should implement the *actions* below, then map each platform's remote/touch to them.

## Deep (rebuild detail)
### Files (profile-global; Kodi has no skin-scoped keymaps)
| file | written by | lifetime |
|---|---|---|
| `zz_bezel2_np_tab.xml` | `bz_cmd.py keymap` copies `resources/keymaps/bezel2_np_tab.xml` | while on Bezel; deleted by `bz_km.leave()` |
| `zz_bezel2_dtap.xml` | `bz_dtap.py` (Select → `NotifyAll(bz,bz_sel)`) | unless `bz_dtap_off`; dtap-off removes only this |
| `zz_bezel2_noctx.xml` | `bz_dtap.py` (C/menu/title/contextmenu → `NotifyAll(bz,bz_ctx)`) | while on Bezel |
Leave: `bz_km.py leave()` deletes all three, clears `bz_km_loaded`, `Action(reloadkeymaps)`; manual `RunScript(special://skin/scripts/bz_cmd.py,keymap_leave)`.

### Key → action (from bezel2_np_tab.xml + dtap)
| context | key | Kodi builtin | port action |
|---|---|---|---|
| music | Tab / remote Display | `ActivateWindow(1121)` | `openMusicFanartFS` |
| music / 1112 / 1121 | M, Red | `ActivateWindow(1115)` | `openMusicControls` |
| 1115 | M, Red | `Dialog.Close(1115)` | `closeMusicControls` |
| 1112 | Tab / Display | `Dialog.Close(1112)` | `closeNowPlaying` |
| 1121 | Tab / Display | `Dialog.Close(1121)` | `closeFanartFS` |
| 1121 | Backspace / browser_back / remote back / pad B | `SetFocus(6422)` | `fanartFSBack` (focus pill) |
| 1121 | long Return/Enter | `PlayPause` | `playPause` |
| music, videos, 1112, 1121 | Esc | `Back` | `back` (opens MM at top level) |
| busy dialog | Tab / Display | `SetProperty(bz_tabq,true,home)` | `queueNowPlaying` (opened when busy ends) |
| home (+ library windows) | long Select / Return | `NotifyAll(bz,bz_ctx)` | `openOptionsInfo` |
| home/music/videos | Select (dtap on) | `NotifyAll(bz,bz_sel)` → 1 tap Select, 2 taps within `bz_at_dtapwin` (200–500, def 300 ms) Info | `select` / `openOptionsInfo` |
| library windows | C / Menu / Title / ContextMenu | `NotifyAll(bz,bz_ctx)` | `openOptionsInfo` |

### Core navigation actions every screen must implement
`up` `down` `left` `right` `select` `back` `openMenu` (Back/Left at list edge → MM 6996, sets `bz_nav`) `playPause` `openNowPlaying` `openOptionsInfo`. Per-object edges: `input/<id>.md`. Touch: [touch-group](../behaviors/touch-group.md), logo = Back ([bezel-logo-back](../behaviors/bezel-logo-back.md)).
