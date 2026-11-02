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

**5.33.277:** Music-section 6886 still on the colour strip (786,136) — move to fanart UL waits on the list-in-strip build (list 60 occupies the fanart block). In 1121 the 6-cycle pill 6421 now sits at fanart UL 140,136 (labels/behaviour unchanged).

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/fullscreen-pill.md) · [state](../state/fullscreen-pill.md) · [motion](../motion/fullscreen-pill.md) · [art](../art/fullscreen-pill.md) · [input](../input/fullscreen-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Current state (5.33.278)
Music artists/albums/songs: list 60 sits in the colour strip (570..960, uniform 86.67% scale, same nav/focus). Meta (small/big/year+genre pills) on the fanart block 150,196–296. FULLSCREEN pill 6886 at fanart UL 140,136 (music, audio playing; same actions).

## 5.33.280 (Nov 1 2026)
- Music L2/L3 half list (bz_mhalf → bz_covercol): small album at top of strip, list under it, no big strip title (BezelArtistMeta3B hidden). Strip slide 450→510.
- Meta = FS fanart format: small artist bz_mm18s, big title bz_mm34 uppercase, outlined pills np_pill32_ol.png (also in Custom_1121 year/genre).
- FULLSCREEN pill 6886: Left from list 60 (music strip, pill visible) → 6886; Left on 6886 → list 60 + open MM; Select unchanged (1121 when bz_m1121ok, else visualisation).
- Open: L2 ALL ALBUMS row 6097/6098 not shown in half-list mode.

## Current state (5.33.297)
- Left from list 60 on the Music strip (artists/albums/songs) with 6886 visible → **always 6886 first**, ahead of the A-Z bar (6100/6500). Before .297 the long-list L1 Artists A-Z bar (6100, >20 items) took Left and skipped the pill.
- While the pill is visible the A-Z bar is not reached by Left from the list (touch still works); with no audio, Left → A-Z bar as before. Left on 6886 → list 60 + open MM (unchanged).

## 5.33.304 — focus order (Rob)
- Order is list → FULLSCREEN pill → A–Z jump bar. Right from the pill goes to the list. Left from the pill goes to the A–Z bar when it is showing, otherwise to the list or main menu as before. It no longer opens the main menu while the A–Z bar is up.
- A hidden pill can't take focus, so Left from the list reaches the A–Z bar with the pill on or off. Right from the A–Z bar goes to the pill when it's showing, otherwise to the list.
