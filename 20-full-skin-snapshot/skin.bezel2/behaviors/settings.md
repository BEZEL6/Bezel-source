# Kodi Settings

**Object:** `Settings.xml` (Settings home, list `9000`) · `SettingsCategory.xml` sub-pages · Back in sub-lists handled by `scripts/bz_dtap.py` (`bz_setback`)
**Where:** Opened from MM SETTINGS (`bz_mm.py GO['settings']`)
**Last updated:** 2026-10-31
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
