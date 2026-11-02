# Kodi Settings

## BEZEL Settings 1130 — Back (current, 5.33.240)
- Back on home list 9130: clear `bz_setx` → `SetProperty(bz_setret,1,home)` → `SetProperty(bz_nav,true,home)` → 1 s `AlarmClock(bz_setmm, bz_nav=true)` re-arm → `Dialog.Close(1130)`. MM opens before the dialog closes; re-arm covers a close that lands on the section after the first set.
- `bz_flip.py` counts `Window.IsActive(1130)` in the Settings family (`_sw`), so the next MM open latches `bz_setret` and focuses the SETTINGS row (6996 row 10, `bz_mmpos=10`, strip `settings`) — the opener row.
- Sub-page 9131 Back → `pgback` (back to 9130 on SERVICES), unchanged.

**Object:** `Settings.xml` (Settings home, list `9000`) · `SettingsCategory.xml` sub-pages · Back in sub-lists handled by `scripts/bz_dtap.py` (`bz_setback`)
**Where:** Opened from MM SETTINGS (`bz_mm.py GO['settings']`)
**Last updated:** 2026-11-02 · 5.33.331
**Status:** Live in 5.33.207. Back from Settings home reopens the MM with a 1 s re-arm. Back in a sub-list returns to its category list. Every Settings level fades in 400 ms sine. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Settings home

### Simple
SETTINGS on the main menu opens Kodi's settings home. Up and Down move, and Select opens a category. Back takes you straight back to the main menu.

### How it works
- The list traps focus: Left does nothing, and Right/Up/Down stay on 9000.
- Back runs two steps:
  1. Set `bz_nav=true` straight away, so the MM opens.
  2. A 1 s `AlarmClock` sets `bz_nav=true` again.
- The re-arm covers the race where Kodi's own window change back to the opener (Videos or Music) lands after the first set and closes the MM again. The second set restores it on the opener row.
- On load, BEZEL's backdrop picker runs. On unload, the current backdrop is saved to `bz_backdrop_last` and cleared.

### Wiring
| Item | Value |
|---|---|
| Window anim | `BezelOpenCloseSet` (WindowOpen fade 0→100, 400 ms sine out) |
| onload | `RunScript(bz_cmd.py,backdrop)` |
| onunload | `SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)` · `ClearProperty(bz_backdrop,home)` |
| defaultcontrol | 9000 |
| List 9000 | onleft noop · onright/onup/ondown 9000 · onback `SetProperty(bz_nav,true,home)` then `AlarmClock(bz_setmm,SetProperty(bz_nav,true,home),00:01,silent)` |

---

## Sub-settings Back

### Simple
Inside a settings category, Back from the right-hand list returns you to the category list on the left first, instead of leaving the page.

### How it works
- Kodi ignores `onback` on grouplist children, so the skin can't wire this in XML.
- Instead, `bz_dtap.py` writes `special://profile/keymaps/zz_bezel2_noctx.xml`. In each settings window, that file maps Back/Backspace to `NotifyAll(bz,bz_setback)`.
- The service's monitor receives the notification and checks whether the sub-list (grouplist 5) has focus:
  - If it does, it runs `SetFocus(3)`, the category list.
  - Otherwise it sends a normal `Action(Back)`.
- The file is rewritten only when its content differs, followed by `Action(reloadkeymaps)`.

### Wiring
| Item | Value |
|---|---|
| Keymap | `zz_bezel2_noctx.xml` (written by `noctx()`), windows: systemsettings, servicesettings, pvrsettings, playersettings, mediasettings, interfacesettings, gamesettings |
| Mapping | keyboard `backspace` / remote `back` → `NotifyAll(bz,bz_setback)` |
| Handler | `M.onNotification`: `SetFocus(3)` if `ControlGroup(5).HasFocus()` else `Action(Back)` |

---

## Transitions

### Simple
Every Settings screen, including the deeper pages and settings dialogs, fades in quickly. Nothing zooms or slides, and nothing fades out.

### How it works
- Settings home and SettingsCategory use `BezelOpenCloseSet`, a WindowOpen-only fade, so going from home to a category and back is a clean swap.
- Settings dialogs use `BezelSecFadeInDialog`.
- Profile, SystemInfo and SkinSettings use `BezelSecFadeIn`.

### Wiring
- `BezelOpenCloseSet`: Settings.xml, SettingsCategory.xml.
- `BezelSecFadeInDialog`: DialogSettings, DialogAddonSettings, Custom_1101_SettingsList, and others.
- `BezelSecFadeIn`: SettingsProfile, SettingsSystemInfo, SkinSettings.
- All are fade 0→100, 400 ms sine out (`Includes_Animations.xml`). See section-transitions.md.

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move (stays in 9000) |
| Left | noop |
| Right | stays 9000 |
| Select | Open category |
| Back (home) | `bz_nav=true` now + 1 s re-arm (`bz_setmm`) → MM |
| Back (sub-list) | `bz_setback` → category list 3, else normal Back |

## Touch
None specified.

## Related
mm-list.md · section-transitions.md · keymaps.md · media-sources.md · touch-group.md

## BEZEL Settings dialog 1130 (5.33.215, Rob Nov 1 2026)

### Simple
MM → SETTINGS now opens BEZEL's own Settings, styled as the MM strip, as a dialog **over** the current section. Warm, the poster and the section never unload, so Back drops you straight to the MM with no poster reload. Rows with ▾ expand in place (nested rows are dimmer and smaller), » opens a new menu, and ‹VALUE› pills cycle real Kodi settings with Left/Right/Select.

### How it works
- `bz_mm.py settings` → `ClearProperty(bz_nav,home)` + `ActivateWindow(1130)` (was `ActivateWindow(Settings)`).
- `xml/Custom_1130_BzSettings.xml` (generated by `/workspace/b401/set5215/gen.py`) is a dialog: list 9130 = home, list 9131 = SERVICES sub-page (`bz_setpg=services`).
- `scripts/bz_set.py`: `load` reads values over JSON-RPC into `bz_set_*` props; `x <grp>` toggles `bz_setx`; `pg`/`pgback` switch pages; `cyc <setting> ±1` → `Settings.SetSettingValue`; `go <window>` closes 1130 (Kodi ignores ActivateWindow while a modal dialog is open), opens the stock window, waits until it closes, waits 600 ms for the section's onload, then reopens 1130 (focus is remembered).
- Back on 9130: close 1130 → MM (`bz_nav=true`). Back on 9131: `onback` → hidden button 9139, whose onfocus runs `pgback` (a dialog closes on Back unless onback moves focus to another control; builtin onbacks do not stop that).
- Static list values must be strings (`top`/`sub`) — numeric property values get localized.
- WARM 2.0.1 · TUNER row lives under INTERFACE (opens Tuner with `bz_tunesrc=set`).

### Warm pages and what is still stock (current, 5.33.331)
Every drill-down from 1130 opens as a Warm page in the same dialog (list **9132**, SERVICES on 9131) except the rows below. Each page ends with **MORE (KODI) »** → the stock window for that category.
| Row | Page | Pills |
|---|---|---|
| PLAYER ▾ VIDEOS | `pvideos` | play action, seek delay, stretch 4:3, aspect error, HQ scalers, 3D mode, quit 3D, teletext |
| PLAYER ▾ MUSIC | `pmusic` | auto-play next, queue, crossfade, crossfade albums, ReplayGain, avoid clipping, seek delay |
| PLAYER ▾ DISCS | `discs` | DVD autorun/menu/region, Blu-ray region, disc playback, audio CD, CD lookup, eject after rip |
| PLAYER ▾ LANGUAGE | `plang` | audio / subtitle language, default flag, sub position/size/style/backing, hearing impaired, visual desc. |
| MEDIA ▾ VIDEO FILES / MUSIC FILES / PICTURES | `vfiles` `mfiles` `pics` | file-view and slideshow options |
| MEDIA ▾ SOURCES | — | closes 1130 and opens Media Sources **1117** (Back there → MM, as from MM MEDIA SOURCES) |
| LIBRARY ▾ VIDEO / MUSIC LIBRARY | `vlib` `mlib` | library view options + SCAN NOW / CLEAN NOW (close 1130, run UpdateLibrary/CleanLibrary) |
| INTERFACE ▾ REGIONAL | `regional` | language (info), region, time/date formats, 24h, temperature, speed, charset, time zone (info) |
| SERVICES » SMB / WEATHER / CACHING | `smb` `weather` `caching` | SMB protocol/security/chunk; weather location/provider (info); cache buffer/memory/read factor/chunk |
| EVENT LOG | `events` | event log on/off, notifications, OPEN LOG (KODI) » stock event list |

- Page title: `bz_set.py pg,<page>,<TITLE>` sets `bz_setpg` + `bz_setpgt` (human title shown as "‹ TITLE" and in the sub-header); `pgback` clears both and refocuses 9130 on the opener row (expanded group stays open).
- Pills for these pages are generic: `bz_set.py` reads each setting's own definition (`Settings.GetSettings`, level expert) — options cycle by their Kodi labels, integers by min/max/step, booleans ON/OFF. Ids are listed in `scripts/bz_set_pages.py`.
- Generated by `/workspace/b401/set5215/gen533.py` (owns home row actions, 9132 pages, `bz_set_pages.py`; idempotent, rerun after edits). The old `gen.py` predates 9132 and must not be rerun on the live tree.

Still stock: SERVICES › NAME (needs text entry), ADD-ONS (addonbrowser strip), PROFILES › MANAGE, FILE MANAGER (intentional), EVENT LOG › OPEN LOG list, LibreELEC add-on, and every MORE (KODI) target. The stock windows' Settings-level button (Basic/Standard/Advanced/Expert) only exists on those MORE pages; the Warm pages show settings regardless of level.

## Focus highlight + pills (5.33.221)
- Focused row uses the **same highlight bar as Bezel lists**: full-row image 390×48, `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]` (follows Tuner highlight shape/opacity); focused label colour `$VAR[BzATHiText]`.
- List rows (1131 list 9140, 1130 list 9130/9131, AddonBrowser list 60) put the bar in `focusedlayout` behind `Control.HasFocus(<list>)`.
- Button/radiobutton rows (1117, DialogAddonInfo) use `<texturefocus/>` plus a sibling image `visible Control.HasFocus(<id>)` — a `$VAR` inside button `texturefocus` did not render in these dialogs.
- Value pills (‹ AUTO ›, ‹ OFF ›, radios): Bezel pill `bezel/np_pill32.png` border 12 — 33FFFFFF fill for value / radio off, E6FFFFFF for radio on. Old `mm_pill_ol` outline and `ad_pill_on/off` are no longer used.
- Zip / repository / category follow-ons (AddonBrowser strip) get the same bar. File manager stays stock.

## SYSTEM sub-pages — Warm strip (current, 5.33.241)
- SETTINGS › SYSTEM ▾ → DISPLAY / AUDIO / INPUT / POWER SAVING / LOGGING no longer open stock `systemsettings`. Each runs `bz_set.py pg,<display|audio|input|power|logging>` and opens list **9132** inside dialog 1130 (same MM-strip layout as SERVICES 9131) — section/Warm/MM art stays continuous underneath.
- Pills (JSON-RPC cycle, Left/Right/Select): DISPLAY refresh rate (OFF/START-STOP/ON START), sync to display · AUDIO passthrough, GUI sounds (NEVER/IDLE/ALWAYS), keep audio alive, volume steps (10–100) · INPUT mouse/touch, joystick · POWER screen off (0–120 min, step 5), shutdown timer (0–240, step 15) · LOGGING debug log, event log. Each page ends with `MORE (KODI) »` → stock systemsettings (via `go`, reopens 1130 after).
- Back on 9132 → hidden 9139 → `pgback` → 9130 on the opener SYSTEM sub row. Back from 9130 → MM (5.33.240 fix, unchanged).

## Warm sub-pages (current, 5.33.242)
All Settings sub-pages except File Manager, Event Log, Regional, Player/Media stock rows now open as Warm strip pages in 1130 via `bz_set.py pg,<page>`; list 9132 hosts every page except SERVICES (9131).
| Page (`bz_setpg`) | Opened from 9130 | Rows |
|---|---|---|
| display/audio/input/power/logging | SYSTEM ▾ subs | pills (5.33.241) + MORE (KODI) » |
| profiles | PROFILES | PROFILE / PROFILES (info) · LOG OFF » · MANAGE (KODI) » (stock profiles) |
| sysinfo | SYSTEM INFO | KODI, BUILD DATE, SCREEN, IP, CPU, CPU TEMP, MEMORY, FREE SPACE, UPTIME (info rows, live infolabels) |
| skin | INTERFACE ▾ SKIN | SKIN (info) · SKIN ZOOM ‹-20…20%› · RSS · BEZEL TUNER » · MORE (KODI) » |
| screensaver | INTERFACE ▾ SCREENSAVER | WAIT TIME ‹1–60 MIN› · DIM ON PAUSE · MODE (info) · MORE (KODI) » |
| games | GAMES | GAMES · OSD HELP pills (blank if build has no games) · MORE (KODI) » |
Kind `i` = read-only info row (label2 right, DDFFFFFF). Back on any page → `pgback` → 9130 on the opener row. Still stock: FILE MANAGER (Rob), EVENT LOG, REGIONAL, PLAYER/MEDIA » rows, every MORE (KODI) row.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/settings.md) · [state](../state/settings.md) · [motion](../motion/settings.md) · [art](../art/settings.md) · [input](../input/settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.337 (t2458): deeper generic pages (GENP pills before MORE (KODI))
- display: DITHERING, LIMITED RANGE, BLANK OTHERS, REFRESH DELAY, GPU BUFFERS (8 rows)
- power: SHUTDOWN TYPE, WAIT NETWORK, WAKE ON ACCESS (6)
- logging: COMPONENT LOG (4)
- games: REWIND, REWIND TIME, AUTOSAVE (6)
- audio: OUTPUT CONFIG, CHANNELS, QUALITY, KEEP VOLUME (9)
- input: no further settings available, so it stays at 3 rows.
- 5.33.339: SERVICES › NAME is a Warm pill. Select opens the Bezel strip keyboard (bz_set.py dname), then Settings.SetSettingValue services.devicename, then focus returns to 9131. It no longer goes to stock servicesettings.
- 5.33.340: Text-value pills: an item with property txt=1 (SERVICES › NAME) has no ‹ › arrows and ignores Left/Right. The onleft/onright guards on 9130/9131/9132 and the TXT list in bz_set.py cyc() both enforce this. Edit it with Select, which opens the Bezel keyboard. Save path tested: BezelTest went to the pill and to services.devicename, then restored to Kodi.
