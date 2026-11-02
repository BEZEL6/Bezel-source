# Keymaps (BEZEL profile keymaps) — keymaps

**Object:** `keymaps` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keymaps.md) · [layout](../layout/keymaps.md) · [state](../state/keymaps.md) · [motion](../motion/keymaps.md) · [art](../art/keymaps.md) · [input](../input/keymaps.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A skin cannot ship keymaps, so BEZEL writes its own into the Kodi profile while BEZEL is the skin. It removes them again as soon as you switch skins, so other skins behave normally.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keymaps.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6422 | `RunScript(special://skin/scripts/bz_vizset.py,step,2,-1)` | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` | `6421` | `6423` | `ClearProperty(bz_vizset)` |

**Semantics from behavior (verbatim lines):**
- `bz_km.py`: `FILES` = the three `zz_bezel2_*` files. `SKIN='skin.bezel2'`. `on_bezel()` falls back to True on exception, so a glitch never deletes the maps. `leave()` deletes the files, clears `bz_km_loaded`, runs `reloadkeymaps` if anything was removed, and logs.
- ## Double-tap Select (dtap)
- Simple.** One Select acts after a short pause. Two quick Selects open the Options/Info menu. Rob sets the pause length in the Tuner.
- How it works.** The keymap turns Select into a notify. A single tap is held for the tap window and then replayed as `Action(Select)`. Before replaying, the script checks that focus has not moved (a fingerprint of window|dialog|control), that it is not more than 0.6 s late, and that `bz_navlock` is not set. So a delayed Select can never land on a new screen. With `bz_dtap_off`, Select passes straight through with no delay.
- `zz_bezel2_dtap.xml`: Select / return / enter (and longpress) → `NotifyAll(bz,bz_sel)` in home, music, videos, filebrowser, filemanager + SECW.
- Second tap → `info()` + `bz_dtapinfo` for 0.8 s. `info()`: filebrowser/filemanager → `Action(ContextMenu)`. SECW not on 1119 → `ActivateWindow(1119)`. Else `Action(Info)`.
- Wiring.** `zz_bezel2_noctx.xml`: in home/music/videos+SECW, c/menu/title/contextmenu/rightclick/longclick → `NotifyAll(bz,bz_ctx)`. The handler closes Kodi's contextmenu (up to 40 × 25 ms) and then runs `info()`. Back in 7 settings windows → `bz_setback`. See context-menu.md.
- | music | m/red → 1115 · tab → 1112 · escape → Back |
- | videos | escape → Back |
- | home/music/videos/programs/pictures/addonbrowser/playlists | longpress select, gamepad a, joystick holdtime 500, menu/title/contentsmenu/etc. → `bz_ctx` |
- | fullscreenvideo | select → `bz_cmd vidsel` · back → `vidback` (fullscreen-video.md) |
- | FullscreenVideo (second block) | back/backspace/escape/browser_back, joystick b/back → `Action(FullScreen)` |
