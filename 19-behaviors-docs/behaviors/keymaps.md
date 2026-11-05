# Keymaps

**Object:** Bezel's key mapping · Kodi: profile keymaps `zz_bezel2_np_tab.xml` (source `resources/keymaps/bezel2_np_tab.xml`), `zz_bezel2_dtap.xml`, `zz_bezel2_noctx.xml` · `scripts/bz_km.py`, `bz_cmd.py keymap` / `keymap_leave`, `scripts/bz_dtap.py`, `bz_flip.py km_leave_watch`
**Where:** every screen while Bezel is the skin
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Bezel adds its own key behaviours on top of the remote: Tab / Display opens fullscreen music from the main screens; M / Red opens music controls; one Select acts after a short pause, two quick Selects open Options / Info; the Menu / long-press keys open Bezel's own section menu instead of Kodi's; Back on Home does nothing. All of it disappears when you switch to another skin.

## Feel contract (any framework)
These are the global input rules a port must reproduce (generic actions).

### States
| State | On screen |
|---|---|
| Bezel active | Bezel actions below |
| Other skin / app | none of them |

### Timeline
| What | Value |
|---|---|
| Single Select | acts after the tap window (Tuner, default 300 ms; 150–600) |
| Double Select | second press inside the window → Options / Info (shown 0.8 s flag) |
| Late Select | dropped if > 0.6 s late or focus moved |

### Interruptions
A delayed single Select is dropped if focus changed or navigation is locked meanwhile.

### Continuity
Rules apply the same in every section.

### Layering
—

### Geometry
—

### Art
—

### Input
| Generic action | Where | Result |
|---|---|---|
| Fullscreen music (Tab / Display) | Music, Home, Movies / TV, Pictures, Programs, Add-ons | open Bezel fullscreen music; inside it: close |
| Music controls (M / Red) | Music, fullscreen music | open / close music controls |
| Select ×2 | lists and section screens | Options / Info (or the section menu) |
| Context (Menu, long Select, title, right-click, long-click) | Home, Music, Videos, Pictures, Programs, Games, Add-ons, playlists, PVR | Bezel section menu (never Kodi's) |
| Back | Home | nothing |
| Back | fullscreen music | album view → fanart → close |
| Right | Kodi FS | next song |
| Back | fullscreen video / video OSD | Bezel video Back rules ([fullscreen-video](fullscreen-video.md)) |
| Tab while busy | busy dialog | queued, opens fullscreen after |
| Long Select | fullscreen music | play / pause |

### Speed targets
Select feels immediate at 300 ms; Tuner can shorten it.

### Never
- Never Kodi's own context menu (noctx).
- No power menu from repeated Back on Home (321).

### Acceptance checks
1. Movies list: Tab with music playing → fullscreen music.
2. Double-Select on a movie → info; single → plays after a short pause.
3. Switch to another skin: Tab / double-Select behave as in that skin.

## Kodi implementation (sandbox)

### How it works
- A skin can't ship keymaps, so Bezel writes `zz_*` files into the profile keymaps folder (loaded last, so they win) and runs `reloadkeymaps`. Watchers (`bz_dtap` ~1 s, `bz_flip km_leave_watch` 1 s) call `bz_km.leave()` when the skin changes: delete the three files, clear `bz_km_loaded`, reload. `on_bezel()` returns True on error so a glitch never deletes them.
- `bz_cmd.py keymap` (1121 / Kodi FS / Music onload): copy `bezel2_np_tab.xml` → `zz_bezel2_np_tab.xml`, delete the legacy name, log other Tab / Display maps, reload.
- **dtap** (`zz_bezel2_dtap.xml`): Select / return / enter (+ long) → `NotifyAll(bz,bz_sel)` in home, music, videos, filebrowser, filemanager + SECW (pictures, programs, games, addonbrowser, playlists, PVR). `bz_dtap.py` holds the tap for `STEPS[bz_at_dtapwin-1]` (150, 175 … 600 ms; default 300) and replays `Action(Select)` if the window|dialog|control fingerprint is unchanged, ≤ 0.6 s late and no `bz_navlock`. Second tap → `info()` + `bz_dtapinfo` 0.8 s (filebrowser / filemanager → `Action(ContextMenu)`; SECW → `ActivateWindow(1119)`; else `Action(Info)`).
- **noctx** (`zz_bezel2_noctx.xml`): c / menu / title / contextmenu / rightclick / longclick → `NotifyAll(bz,bz_ctx)`; handler closes Kodi's context menu (≤ 40 × 25 ms) then `info()`. Back in 7 settings windows → `bz_setback`.
- **bz_dtap loop** (20 ms): `install()` every 25 ticks, `on_bezel` every 50; side jobs: close stray contextmenu, mirror 9880 → `bz_secfan` / `bz_secfanlbl`, clear `bz_navtune`, apply `bz_tune_dirty` after 1.2 s.

### Wiring (np_tab sections)
| Window | Keys → action |
|---|---|
| music | m / red → 1115 · tab / display → `ActivateWindow(1121)` · escape → Back |
| home, videos, pictures, programs, addonbrowser | tab / display → `ActivateWindow(1121)` (472); home: Back (all devices) → noop |
| window1121 | m / red → 1115 · tab / display → `Dialog.Close(1121)` · escape → Back · back / backspace / browser_back / b → `SetFocus(6422)` · long return / enter → PlayPause |
| visualisation | Right → `PlayerControl(Next)` · back → `SetFocus(6297)` · m / red → 1115 · select → Select · long return → PlayPause · gamepad / joystick to match |
| window1115 | m / red → close |
| busydialog / busydialognocancel | tab / display → `bz_tabq=true` |
| home / music / videos / programs / pictures / addonbrowser / playlists | long select, gamepad a, joystick hold 500, menu / title / contentsmenu … → `bz_ctx` |
| fullscreenvideo | select → `bz_cmd vidsel` · back → `vidback`; second `FullscreenVideo` block: back keys → `Action(FullScreen)` (which wins is untested) |
| videoosd | back → `vidback` |
| Removed | `window1112` (465) |
| Note | duplicate window sections in the file are merged by Kodi |

### Kodi workarounds (do not port)
Everything about install / leave, `NotifyAll` hand-offs and the replayed Select: Kodi has no per-skin input layer and no double-press event.

## Related
[music-fanart-fs](music-fanart-fs.md) · [context-menu](context-menu.md) · [fullscreen-video](fullscreen-video.md) · [touch-group](touch-group.md) · [skin-settings-tuner](skin-settings-tuner.md)
