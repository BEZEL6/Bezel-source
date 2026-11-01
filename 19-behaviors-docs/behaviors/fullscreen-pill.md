# Fullscreen pill (Music list)

**Object:** button `6886` inside `BezelFSLeftStage` (Includes_Bezel), in a horizontal grouplist at 786,136 (158×32, aligned right)  
**Where:** Music section list, over the left fanart stage, while audio plays  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live tree. Rob has not approved it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it does

**Simple.** A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).

**How it works.** The pill is inside the fanart left stage, so it rides the stage slide in and out and never pops on its own. Its group hides in every case where it would be wrong or on top of something: in viz, fullscreen video, Dialogue FS, 1112, while the Play Next return latch runs, with the MM open, or outside artists/albums/songs. It was hard-hidden in 5.33.154/.155 and restored under BUG-018 (.169/.173).

**Wiring.**
- Group visible: `Player.HasAudio + Window.IsActive(music)` + not visualisation active/visible + not fullscreenvideo active/visible + not 1120 active/visible + `!Window.IsVisible(1112)` + `bz_pnoff≠1` + `bz_fsret≠true` + `!$EXP[bz_navmenu]` + `Container.Content(artists|albums|songs)`.
- Button: width auto, height 32, label FULLSCREEN, font `bz_b15`, text `BzFSCTint`, `bezel/np_pill32.png` with `BzFSCTint50` / `BzFSCTint80` (5.33.126 t909).

## Keys

**Simple.** Select opens full screen. Any direction or Back returns to the list.

**Wiring.** `onclick` (`Player.HasAudio`) → `ActivateWindow(visualisation)`. `onleft` / `onright` / `onup` / `ondown` / `onback` → `60`.

## Related
fanart-fs.md · dialogue-fs.md · music-list.md

**5.33.210:** `onclick` → `ActivateWindow(1121)` when `$EXP[bz_m1121ok]` (Music Fanart FS dialog), else `ActivateWindow(visualisation)`. Pill hides while 1121 is visible.
