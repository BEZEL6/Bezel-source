# Fullscreen video

**Object:** `VideoFullScreen.xml` (80 lines: group `0` with labels `10`–`12`, cache group `1`) · keymap `fullscreenvideo` / `videoosd` sections · `bz_cmd.py vidsel` / `vidback`  
**Where:** Kodi `fullscreenvideo`  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it does

**Simple.** Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.

**How it works.** Kodi opens the window by itself when video starts (4.0.1 O28 restored this; the 4.0.0 bounce-back was removed). The window has no focusable controls (`defaultcontrol` empty), so keys go through the BEZEL keymap to `bz_cmd.py`.

**Wiring.** Labels 10/11/12 at 45, top 15/45/75 (Kodi info lines). Group 1 `DepthOSD+` visible `Player.Caching + Integer.IsGreater(Player.CacheLevel,0)`, fade in 200 ms after 300, fade out 150 ms after 200.

## Select

**Simple.** Pause or resume, and show the OSD.

**Wiring.** keymap `fullscreenvideo` select → `bz_cmd.py vidsel` = `PlayerControl(Play)` + `ActivateWindow(videoosd)` (BETA 2.6).

## Back

**Simple.** The first Back hides the controls. The next Back stops.

**How it works.** `vidback` checks the layers top-down and removes only the first one it finds. A seek bar that Kodi leaves after the OSD closes does not count as another layer for 6 s. Without that rule you would need an extra Back.

**Wiring.** `bz_cmd.py vidback` (keymap back in `fullscreenvideo` and `videoosd`):
1. `videoosd` visible → set `bz_vosdc=now`, `Dialog.Close(videoosd)`.
2. `fullscreeninfo` visible → close it.
3. `Player.ShowInfo` → `Action(Info)` (toggle off).
4. `Player.DisplayAfterSeek | Player.Seeking`, and the OSD did not close within the last 6 s → stamp `bz_vosdc` and stop there.
5. Else `PlayerControl(Stop)`.

**Unverified:** the np_tab keymap also has a second `FullscreenVideo` block that maps Back → `Action(FullScreen)` (minimise). Which of the two Back maps Kodi applies has not been tested on device.

## Interactions
- Pause screen 1116 shows when paused (pause-overlay.md).
- The global logo-back button and FS pill are hidden here. Dust is off (dust.md).
- The dtap keymap does not list `fullscreenvideo`, so Select is not double-tap-delayed here.

## Related
video-osd.md · pause-overlay.md · keymaps.md
