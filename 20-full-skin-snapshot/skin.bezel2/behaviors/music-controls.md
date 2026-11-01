# Music controls (dialog 1115)

**Object:** `Custom_1115_MusicControls.xml` dialog `1115` (zorder 2, `DepthOSD`) · rows `6401–6413` · viz-settings page `6420–6427` + `6429` · `scripts/bz_vizset.py`
**Where:** Over Music / visualisation / Dialogue FS while audio plays. Right-hand panel at x 570
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Transport rows, the Viz settings sub-page, the TUNER hand-off and Right → Dialogue FS all work as described here. Draft: Rob hasn't approved or re-smoked it.
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, including order and races), and **Wiring** (properties, conditions, control IDs, scripts and timings from the live tree).

---

## Open / close

### Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

### How it works
- Kodi's own music OSD windows are thin wrappers. `MusicOSD.xml` and `PlayerControls.xml` open 1115 from their `onload`, so any key that would show the stock OSD lands on the BEZEL panel instead.
- From the Music list, **Right** on list 60 opens 1115 when no vback card is up, no grid (6600) is visible, and the NP button 6160 is visible.
- From the fan art pill (6391) in full-screen viz, **Down** opens 1115 when NP mode is `controls`. Otherwise it focuses 6390.
- `bz_cmd.py npctl` toggles 1115. If full-screen video is active it opens `videoosd` instead, so the same command means "show controls" everywhere.
- The panel fades in for 250 ms and the column slides up from 30 px below. On close it fades out over 420 ms and drifts 20 px. Focus always starts on Play/Pause (`defaultcontrol always`).

### Wiring
| Item | Value |
|---|---|
| Window | `<window type="dialog" id="1115">`, zorder 2, `DepthOSD`, `defaultcontrol always="true"` 6401 |
| Open anim | Fade 0→100, 250 ms sine out (WindowOpen); column group slide 0,30→0, 250 ms cubic |
| Close anim | Fade 100→0, 420 ms sine inout (WindowClose); column slide 0→0,-20 |
| Openers | `MusicOSD.xml` onload (`Player.HasAudio`) · `PlayerControls.xml` onload (`!Window.IsActive(fullscreenvideo) + Player.HasAudio`) · `Includes_Bezel.xml` list 60 onright (`String.IsEmpty(bz_vback) + !Control.IsVisible(6600) + Control.IsVisible(6160)`) · fan art pill ondown (`$EXP[bz_npm_ctl]` = `Skin.String(bz_npmode)=controls`) · `bz_cmd.py npctl` (`videoosd` when `Window.IsActive(fullscreenvideo)`) |
| Backdrop | Full-screen button (click = Close) · 840×900 dim at 120,120 · title "PLAYER CONTROLS" at 570,66 with BzFSSh shadow variants (`!Skin.HasSetting(bz_fssh_off)`) |
| Column | Group 570,120, 390×900 · solid FF0E0F12 backing + `BzMMStrip` colour · section labels PLAYBACK / MODE / MORE · focus pill `bezel/mm_pill.png` |

---

## Rows and keys

### Simple
Thirteen rows in three blocks. Up/Down moves and wraps from Close back to Play. Left closes the panel. Right either jumps to the big Dialogue FS screen (when that makes sense) or just closes.

### How it works
- Every row runs a Kodi `PlayerControl` or window action. Up next and Visualisation close the panel first, so the next window isn't stacked under a dialog.
- Visualisation uses a 1 s `AlarmClock` to open Kodi's viz picker *after* the close animation has started. Opening the picker directly from inside the closing dialog would race it.
- Right checks `$EXP[bz_pndlg_ok]`. When it's true: close 1115 without animation (`Close(1115,true)`), then put focus on the album-rail slot that matches the current slide speed, then open 1120. The focus must land first, because 1120's slide-in starts from the focused rail.

### Wiring
| ID | Label | onclick |
|---|---|---|
| 6401 | Play/Pause | `PlayerControl(Play)` |
| 6402 | Last | `PlayerControl(Previous)` |
| 6403 | Next | `PlayerControl(Next)` |
| 6404 | Rewind | `PlayerControl(Rewind)` |
| 6405 | FF | `PlayerControl(Forward)` |
| 6406 | Stop | `PlayerControl(Stop)` |
| 6407 | Shuffle | `PlayerControl(Random)` |
| 6408 | Repeat | `PlayerControl(Repeat)` |
| 6409 | Up next | Close + `ActivateWindow(musicplaylist)` |
| 6411 | Visualisation | Close + `AlarmClock(bzviz,Addon.Default.Set(xbmc.player.musicviz),00:01,silent)` |
| 6412 | Viz settings | `SetProperty(bz_vizset,1)` · `RunScript(bz_vizset.py,load)` · `SetFocus(6420)` |
| 6413 | TUNER | see below |
| 6410 | Close controls | Close |

- Up/Down chain: 6401↔6402↔…↔6408↔6409↔6411↔6412↔6413↔6410↔6401 (wraps).
- Every row: `onleft` = Close.
- Every row `onright`: when `$EXP[bz_pndlg_ok]`, it runs `Close(1115,true)`, then SetFocus by `Skin.String(bz_at_fsslide)` (1→6369 · 2→6379 · empty/3→6399 · 4→6384), then `ActivateWindow(1120)`. Otherwise it runs Close.
- `bz_pndlg_ok` (Includes_Bezel ~L318) = `!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + !Window.IsActive(1120)`.

---

## TUNER hand-off (6413)

### Simple
TUNER jumps straight into the BEZEL Tuner on the main menu. Back from the Tuner returns you to the visualisation with this panel open again.

### How it works
6413 stamps the source (`bz_tunesrc=fsctrl`) **before** it closes, so the Tuner's Back handler knows where to return. It then opens Home, opens the MM (`bz_nav`) with the Tuner card (`bz_navtune`), and focuses the Tuner list 6970 with a zero-delay alarm. The alarm lets the MM build before focus is requested.

### Wiring
- onclick order: `SetProperty(bz_tunesrc,fsctrl,home)` → Close → `ActivateWindow(home)` → `SetProperty(bz_nav,true,home)` → `SetProperty(bz_navtune,true,home)` → `AlarmClock(bz_tunf,SetFocus(6970),00:00)`.
- Tuner 6970 onback with `bz_tunesrc=fsctrl`: `ClearProperty(bz_nav)` → `ActivateWindow(visualisation)` → `ActivateWindow(1115)` (`Includes_Tuner.xml`).

---

## Viz settings page (6420–6429)

### Simple
"Viz settings" swaps the panel to a page listing the current visualisation's own settings (up to 8). Left and Right change a value, and Back returns to the main rows. If the visualisation has no adjustable settings, it says so.

### How it works
1. 6412 sets `bz_vizset=1`, which shows the page group drawn over the main rows. The main rows have no `bz_vizset` condition of their own; focus moves to 6420.
2. `bz_vizset.py load` asks Kodi (JSON-RPC `Settings.GetSettingValue musicplayer.visualisation`) which viz is active.
3. It reads that add-on's `resources/settings.xml` and keeps only `integer`, `number` and `boolean` settings (up to MAX=8).
   - Options come from `<option>` entries.
   - min/max/step come from the constraints (defaults 0/100/1).
4. It publishes labels and values as window properties on the current dialog, so the XML just shows `bz_vsN_lab` / `bz_vsN_val`.
5. Stepping:
   - Booleans toggle (shown On/Off).
   - Option lists cycle (mod length).
   - Numbers clamp to min/max (cast to int for integer settings).
   - Each step writes immediately with `addon.setSetting` and republishes.
6. If no viz is set, it publishes `bz_vs_n=0` and the name "None", and the page shows "No settings for this visualisation".
7. Down on a row skips to Back (6429) when the next row's label is empty. That way focus never lands on a blank slot.

### Wiring
| Item | Value |
|---|---|
| Page group | visible `Window.Property(bz_vizset)=1` |
| Header | "VIZ SETTINGS · `bz_vs_name`"; empty text when `bz_vs_n=0` |
| Rows 6420–6427 | label `bz_vsN_lab`, value `‹ bz_vsN_val ›` · onclick/onright `bz_vizset.py step,N,1` · onleft `step,N,-1` · onback: clear `bz_vizset` + `SetFocus(6412)` · ondown → 6429 if the next label is empty |
| 6429 ‹ Back | clear `bz_vizset` + `SetFocus(6412)`; onup → last populated row |
| Script | `scripts/bz_vizset.py` (57 lines): `vizid()`, `rows()`, `show()`, step; target window `xbmcgui.getCurrentWindowDialogId()` |
| onunload | `ClearProperty(bz_vizset)`; if `Skin.String(bz_npmode)=controls` → `Skin.SetString(bz_npmode,vis)` |

---

## Touch
None specified beyond normal focus/click. Tapping the dim area (full-screen button) closes the panel.

## Related
fanart-fs.md · dialogue-fs.md · music-viz-settings.md · skin-settings-tuner.md · play-next.md
