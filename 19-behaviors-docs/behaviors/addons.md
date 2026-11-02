# Add-ons browser

**Object:** `AddonBrowser.xml` (Kodi `addonbrowser`), list `60`, grouplist `9000`  
**Where:** Opened from the Main Menu row ADD-ONS (`bz_mm.py addons`)  
**Last updated:** 2026-11-01 · 5.33.221
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** Pick ADD-ONS in the Main Menu and Kodi's add-on browser opens in BEZEL chrome with a random backdrop. Press Back at the top level and the Main Menu opens again.

**How it works.** The `addons` GO entry in `bz_mm.py` closes the MM first, then opens the window. It never runs the MM warm underlay path, because that is for library sections only. `onload` picks a backdrop. `onunload` saves the backdrop it showed, so the next window does not repeat it, and clears the mini-player big flag. Back inside a sub-folder is Kodi's normal parent-folder step. The list's `onback` only opens the MM at the root, where `FolderPath` is `addons://` or empty.

**Wiring.**
- Open: `bz_mm.py` `MMLOCK_S=0.30` drops a repeat Select within 300 ms. `store()` writes `Skin.String(bz_lastart_<sec>)`, then `bz_mmpick=true`, then closes 1112 if open. GO `addons` = `ClearProperty(bz_nav)` + `ActivateWindow(addonbrowser)`.
- `<defaultcontrol always="true">60</defaultcontrol>`.
- `onload`: `RunScript(special://skin/scripts/bz_cmd.py,backdrop)`.
- `onunload`: save `bz_backdrop_last`, then clear `bz_backdrop` and `bz_minibig`.
- List 60 `onback` with `[String.IsEqual(Container.FolderPath,addons://) | String.IsEmpty(Container.FolderPath)] + !$EXP[bz_navmenu]` → `SetProperty(bz_nav,true,home)` (5.33.179 BUG-024).

## Backdrop

**Simple.** Every visit shows a random image from the skin's backdrop folder. It never shows the same one twice in a row. Rob can pin one image instead.

**How it works.** `bz_cmd.py backdrop` lists `special://skin/extras/backdrop/` (png/jpg/jpeg/webp/gif). It drops the current image and `bz_backdrop_last` from the pool and picks at random. When the Skin.String `bz_bdimg` is set, that fixed image wins.

**Wiring.** Home prop `bz_backdrop` is read by the backdrop image. `bz_backdrop_last` is written on unload. Shared with Favourites (favourites.md) and File manager (files-filemanager.md).

## Keys

**Simple.** Up and Down move through the list. Left opens the Main Menu. Right goes to the side menu. Back goes up a folder, or opens the MM at the top.

**How it works.** Left uses `$EXP[bz_navok]`, so it cannot open the MM while a nav lock or grace window is running or when the MM is already open. Up and Down stay on 60, so there is no escape off the list ends. The MM focus bounces stop a stray focus landing on 60 while the strip is open.

**Wiring.**
| Key | Control 60 |
|---|---|
| Left | `$EXP[bz_navok]` → `SetProperty(bz_nav,true,home)` |
| Right | `9000` |
| Up / Down | `60` |
| Back | root → `bz_nav=true`; else Kodi parent folder |
| Select | Kodi open/install. The dtap keymap covers `addonbrowser` (SECW), so a double-tap opens 1119 (context-menu.md) |

List 60 includes `BezelMMFocusBounce` and `BezelMMFocusBounceList`. When `bz_navmenu` is open and `bz_mmpick` is not true, `onfocus` runs `SetFocus(6996)`. The List variant also checks `bz_mmwarm`.

## Related
mm-list.md · context-menu.md · keymaps.md · favourites.md

## 5.33.220 — Warm strip Add-ons (current state)
- MM → ADD-ONS opens **Custom_1131_BzAddons.xml** (dialog 1131, list 9140), styled like Settings 1130: title + breadcrumb, ▾ expand, » new menu, ‹PILL›.
- Rows: MY ADD-ONS ▾ (Video/Music/Program/Services/Skins/All » with counts from bz_set adload), FROM REPOSITORY », FROM ZIP FILE (bz_set azip → InstallFromZip), SEARCH », pills UPDATES (AUTO/NOTIFY/NEVER) / NOTIFY / UNKNOWN SRC, AVAILABLE UPDATES », RUNNING », RECENTLY UPDATED », DEPENDENCIES ▾ (ALL / ORPHANED).
- » rows: bz_set `ago,<path>` closes 1131, opens AddonBrowser (path,return); when it closes, `_reopen` brings 1131 back unless MM navigation (bz_nav), a modal, fullscreen or a plugin path is active.
- AddonBrowser.xml restyled as a Warm strip (title $VAR[BzAdTitle], "ADD-ONS · N ITEMS", 48px rows with »). Back at the root returns to 1131 → Back again → MM.
- DialogAddonInfo.xml restyled as a strip: OPEN » / ENABLED pill / AUTO-UPDATE pill / CONFIGURE / UPDATE / VERSIONS / DEPENDENCIES / INSTALL-UNINSTALL.
- Still stock: DialogAddonSettings, DialogSelect (version pick), FileBrowser (zip picker).

## Focus highlight + pills (5.33.221)
- Focused row uses the **same highlight bar as Bezel lists**: full-row image 390×48, `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]` (follows Tuner highlight shape/opacity); focused label colour `$VAR[BzATHiText]`.
- List rows (1131 list 9140, 1130 list 9130/9131, AddonBrowser list 60) put the bar in `focusedlayout` behind `Control.HasFocus(<list>)`.
- Button/radiobutton rows (1117, DialogAddonInfo) use `<texturefocus/>` plus a sibling image `visible Control.HasFocus(<id>)` — a `$VAR` inside button `texturefocus` did not render in these dialogs.
- Value pills (‹ AUTO ›, ‹ OFF ›, radios): Bezel pill `bezel/np_pill32.png` border 12 — 33FFFFFF fill for value / radio off, E6FFFFFF for radio on. Old `mm_pill_ol` outline and `ad_pill_on/off` are no longer used.
- Zip / repository / category follow-ons (AddonBrowser strip) get the same bar. File manager stays stock.


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/AddonBrowser.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 60 | list | 0,112 | 390×720 | `SetProperty(bz_nav,true,home)/9000/60/60` | `—` |
| 9000 | grouplist | —,50 | —×— | `—/—/—/—` | `—` |
| 201 | label | —,— | —×— | `—/—/—/—` | `—` |
| 7 | radiobutton | —,— | —×— | `—/—/—/—` | `Control.IsEnabled(7)` |
| 8 | radiobutton | —,— | —×— | `—/—/—/—` | `Control.IsEnabled(8)` |
| 9 | button | —,— | —×— | `—/—/—/—` | `—` |
| 5 | button | —,— | —×— | `—/—/—/—` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `RunScript(special://skin/scripts/bz_cmd.py,backdrop)`
- `SetProperty(bz_nav,true,home)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/addons.md) · [state](../state/addons.md) · [motion](../motion/addons.md) · [art](../art/addons.md) · [input](../input/addons.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.335 — no section list bleed under the Add-ons strip (t2451)
- The section list 60 under 1131 showed through the translucent Warm strip. List 60 (both Includes_Bezel copies) now fades out (150 ms) while 1131, 1130, 1117 or 1132 is visible; the double-tap/controls hint (BezelDtapHint) hides under those dialogs too. Left meta panel and poster (Warm art) stay. Smoke: `audit_settings_levels/335_addons_pre.png` (bleed) → `335_addons_post.png` (clean), `335_addons_closed.png` (back to MM).
