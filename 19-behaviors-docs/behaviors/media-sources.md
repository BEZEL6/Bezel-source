# Media sources

**Object:** `Custom_1117_MediaSources.xml` window `1117` · grouplist `9000` (125,128, 440 wide) with 11 rows `7101–7121` · grouplist `9001` (584,136) with `9101` / `9102` · bounce `6299`  
**Where:** Main Menu row MEDIA SOURCES  
**Last updated:** 2026-11-01 · 5.33.221
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**How it works.** Picking a row stores which row it was (`bz_msfocus`) and a return flag (`bz_msret=1`), then opens the Kodi window with `return`. That media window's `onback` checks for the flag and a `sources://` path and re-opens 1117. On load, 1117 clears the flag and restores focus on a 1-second AlarmClock, so the focus lands after the rows exist. With no stored row, focus goes to 7101.

**Wiring.**
- MM row → clear `bz_nav` / `bz_navtune` / `bz_navbez` → `ActivateWindow(1117)`.
- `<defaultcontrol always="true">7101</defaultcontrol>`, `menucontrol` 9001, `BezelSecFadeIn` (5.33.177).
- `onload`: `ClearProperty(bz_msret)`. `bz_msfocus` set → `AlarmClock(bzmsf,SetFocus($INFO[bz_msfocus]),00:01,silent)`, else `SetFocus(7101)`.
- `6299` bounce → `bz_msfocus` or 7101.
- Return: Includes_Bezel lines ~1518 and ~2664, media-window `onback` with `bz_msret=1` + `FolderPath` starting `sources://` → `ActivateWindow(1117)`.

## Layout

**Wiring.** `BezelStdFrame`, title "Media sources", label "Settings / Media sources". DETAIL panel visible while `ControlGroup(9000).HasFocus` shows `$VAR[BzMSHead]` / `$VAR[BzMSBody]` for the focused row.

## Keys

**Simple.** Up and Down move through the rows and wrap. Left or Right goes to CANCEL / SETTINGS. Back opens the Main Menu.

**Wiring.**
- 7101: `bz_msret=1`, `bz_msfocus=7101`, `ActivateWindow(Videos,sources://video/,return)`. `onup` 7121 (wrap), `ondown` 7102, left/right 9001. Rows: 7101 VIDEOS SOURCES… · 7102 Update library · 7103 Clean library · 7104 Export library · 7105 Import library (`MediaSettings,library`) · 7111 MUSIC SOURCES… (`Music,sources://music/,return`) · 7112–7115 the same four library rows for music · 7121 PICTURES SOURCES… (`Pictures,sources://pictures/,return`). I did not re-trace the per-row actions of 7102–7104 / 7112–7114 for this doc.
- Every button in 9000: `onback` → `SetProperty(bz_nav,true,home)` (BUG-024).
- 9001: `9101` CANCEL → `Close` · `9102` SETTINGS → `ActivateWindow(MediaSettings)`.

## Related
mm-list.md · filebrowser.md · files-filemanager.md

## 5.33.220 — Warm strip Media Sources (current state)
- Custom_1117 is still a window (6299 bounce, msret/msfocus kept) but now uses the strip chrome: VIDEOS ▾ / MUSIC ▾ / PICTURES ▾ (bz_msx), each with SOURCES » (count), library actions and an UPDATE ON START pill; ADD SOURCE » (sources://video/ with msret); LIBRARY SCAN pill (QUIET/SHOW). Wrap is 7100↔7131 and the default focus is 7100. Menucontrol 9001 has been removed.
- Back → MM unchanged. FileBrowser / add-source dialog are still stock.

## Focus highlight + pills (5.33.221)
- Focused row uses the **same highlight bar as Bezel lists**: full-row image 390×48, `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]` (follows Tuner highlight shape/opacity); focused label colour `$VAR[BzATHiText]`.
- List rows (1131 list 9140, 1130 list 9130/9131, AddonBrowser list 60) put the bar in `focusedlayout` behind `Control.HasFocus(<list>)`.
- Button/radiobutton rows (1117, DialogAddonInfo) use `<texturefocus/>` plus a sibling image `visible Control.HasFocus(<id>)` — a `$VAR` inside button `texturefocus` did not render in these dialogs.
- Value pills (‹ AUTO ›, ‹ OFF ›, radios): Bezel pill `bezel/np_pill32.png` border 12 — 33FFFFFF fill for value / radio off, E6FFFFFF for radio on. Old `mm_pill_ol` outline and `ad_pill_on/off` are no longer used.
- Zip / repository / category follow-ons (AddonBrowser strip) get the same bar. File manager stays stock.
