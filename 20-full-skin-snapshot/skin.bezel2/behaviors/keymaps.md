# Keymaps (BEZEL profile keymaps)

**Object:** `scripts/bz_km.py` (leave/cleanup) · `bz_cmd.py keymap` / `keymap_leave` (np_tab) · `scripts/bz_dtap.py` (dtap + noctx) · `bz_flip.py km_leave_watch` (line 457) · source `resources/keymaps/bezel2_np_tab.xml`  
**Where:** Installed into the profile keymaps folder as `zz_bezel2_np_tab.xml`, `zz_bezel2_dtap.xml`, `zz_bezel2_noctx.xml`  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Why profile keymaps

**Simple.** A skin cannot ship keymaps, so BEZEL writes its own into the Kodi profile while BEZEL is the skin. It removes them again as soon as you switch skins, so other skins behave normally.

**How it works.** Kodi loads keymaps alphabetically and later files win, so every file gets a `zz_` name and loads last. Installing a file is followed by `reloadkeymaps`. When the skin changes, two watchers notice (`bz_dtap` every ~1 s and `bz_flip km_leave_watch` every 1 s) and call `bz_km.leave()`.

**Wiring.**
- `bz_km.py`: `FILES` = the three `zz_bezel2_*` files. `SKIN='skin.bezel2'`. `on_bezel()` falls back to True on exception, so a glitch never deletes the maps. `leave()` deletes the files, clears `bz_km_loaded`, runs `reloadkeymaps` if anything was removed, and logs.
- `bz_cmd.py keymap` (line 41): copy `bezel2_np_tab.xml` → `zz_bezel2_np_tab.xml`, delete the legacy `bezel2_np_tab.xml`, log other Tab/Display maps, then reload. `keymap_leave` (line 38).
- `bz_flip.py` line 457 `km_leave_watch`: 1 s poll → `leave()` + clear `bz_flip_running`.

## Double-tap Select (dtap)

**Simple.** One Select acts after a short pause. Two quick Selects open the Options/Info menu. Rob sets the pause length in the Tuner.

**How it works.** The keymap turns Select into a notify. A single tap is held for the tap window and then replayed as `Action(Select)`. Before replaying, the script checks that focus has not moved (a fingerprint of window|dialog|control), that it is not more than 0.6 s late, and that `bz_navlock` is not set. So a delayed Select can never land on a new screen. With `bz_dtap_off`, Select passes straight through with no delay.

**Wiring.**
- `zz_bezel2_dtap.xml`: Select / return / enter (and longpress) → `NotifyAll(bz,bz_sel)` in home, music, videos, filebrowser, filemanager + SECW.
- SECW = pictures, programs, games, addonbrowser, music/video playlist, PVR windows.
- Window = `STEPS[bz_at_dtapwin-1]`, default 0.3 s. STEPS = 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600 ms.
- Second tap → `info()` + `bz_dtapinfo` for 0.8 s. `info()`: filebrowser/filemanager → `Action(ContextMenu)`. SECW not on 1119 → `ActivateWindow(1119)`. Else `Action(Info)`.

## No Kodi context menu (noctx)

**Wiring.** `zz_bezel2_noctx.xml`: in home/music/videos+SECW, c/menu/title/contextmenu/rightclick/longclick → `NotifyAll(bz,bz_ctx)`. The handler closes Kodi's contextmenu (up to 40 × 25 ms) and then runs `info()`. Back in 7 settings windows → `bz_setback`. See context-menu.md.

## bz_dtap loop

**Wiring.** Guard `bz_dtap_running`. Loop every 20 ms. `install()` every 25 ticks (rewrites only once when fresh). `on_bezel` check every 50 ticks (~1 s) → `leave()` and break. Side jobs: close a stray Kodi contextmenu, mirror 9880 into `bz_secfan` / `bz_secfanlbl`, clear `bz_navtune`, apply `bz_tune_dirty` after 1.2 s. `finally`: not on BEZEL → `leave()`, else if not aborting → `install(False)`. Exit signal `bz_quit_dtap` (bz_cmd quit).

## np_tab sections

**Wiring.**
| Window | Keys → action |
|---|---|
| music | m/red → 1115 · tab → 1112 · escape → Back |
| videos | escape → Back |
| busydialog / busydialognocancel | tab/display → `bz_tabq=true` |
| window1112 | m → 1115 · tab/display → `Dialog.Close(1112)` |
| window1115 | m/red → close |
| home/music/videos/programs/pictures/addonbrowser/playlists | longpress select, gamepad a, joystick holdtime 500, menu/title/contentsmenu/etc. → `bz_ctx` |
| fullscreenvideo | select → `bz_cmd vidsel` · back → `vidback` (fullscreen-video.md) |
| FullscreenVideo (second block) | back/backspace/escape/browser_back, joystick b/back → `Action(FullScreen)` |
| videoosd | back → `vidback` |
| visualisation | Right → `PlayerControl(Next)` (5.33.205) · back → `SetFocus(6297)` · M/RED → 1115 · select → Select · longpress return → PlayPause · gamepad/joystick mapped to match |

**Unverified:** both a `fullscreenvideo` and a `FullscreenVideo` block map Back. Which one wins on device has not been tested.

## Related
context-menu.md · fanart-fs.md · fullscreen-video.md · skin-settings-tuner.md
