# Add-ons browser — addons

**Object:** `addons` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/addons.md) · [layout](../layout/addons.md) · [state](../state/addons.md) · [motion](../motion/addons.md) · [art](../art/addons.md) · [input](../input/addons.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Pick ADD-ONS in the Main Menu and Kodi's add-on browser opens in BEZEL chrome with a random backdrop. Press Back at the top level and the Main Menu opens again.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/addons.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |
| 9000 | `Close` | `Close` | `noop` | `noop` | `` |
| 9000 | `Close` | `Close` | `noop` | `noop` | `Close` |
| 9130 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9130` | `9130` | `ClearProperty(bz_setx,home)` |
| 9140 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9140` | `9140` | `Dialog.Close(1131)` |

**Semantics from behavior (verbatim lines):**
- Simple.** Pick ADD-ONS in the Main Menu and Kodi's add-on browser opens in BEZEL chrome with a random backdrop. Press Back at the top level and the Main Menu opens again.
- How it works.** The `addons` GO entry in `bz_mm.py` closes the MM first, then opens the window. It never runs the MM warm underlay path, because that is for library sections only. `onload` picks a backdrop. `onunload` saves the backdrop it showed, so the next window does not repeat it, and clears the mini-player big flag. Back inside a sub-folder is Kodi's normal parent-folder step. The list's `onback` only opens the MM at the root, where `FolderPath` is `addons://` or empty.
- Open: `bz_mm.py` `MMLOCK_S=0.30` drops a repeat Select within 300 ms. `store()` writes `Skin.String(bz_lastart_<sec>)`, then `bz_mmpick=true`, then closes 1112 if open. GO `addons` = `ClearProperty(bz_nav)` + `ActivateWindow(addonbrowser)`.
- Simple.** Up and Down move through the list. Left opens the Main Menu. Right goes to the side menu. Back goes up a folder, or opens the MM at the top.
- How it works.** Left uses `$EXP[bz_navok]`, so it cannot open the MM while a nav lock or grace window is running or when the MM is already open. Up and Down stay on 60, so there is no escape off the list ends. The MM focus bounces stop a stray focus landing on 60 while the strip is open.
- | Left | `$EXP[bz_navok]` → `SetProperty(bz_nav,true,home)` |
- | Right | `9000` |
- | Up / Down | `60` |
- | Back | root → `bz_nav=true`; else Kodi parent folder |
- | Select | Kodi open/install. The dtap keymap covers `addonbrowser` (SECW), so a double-tap opens 1119 (context-menu.md) |
- » rows: bz_set `ago,<path>` closes 1131, opens AddonBrowser (path,return); when it closes, `_reopen` brings 1131 back unless MM navigation (bz_nav), a modal, fullscreen or a plugin path is active.
- AddonBrowser.xml restyled as a Warm strip (title $VAR[BzAdTitle], "ADD-ONS · N ITEMS", 48px rows with »). Back at the root returns to 1131 → Back again → MM.
