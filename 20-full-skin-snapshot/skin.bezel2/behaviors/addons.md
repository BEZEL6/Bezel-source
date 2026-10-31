# Add-ons browser

**Object:** `AddonBrowser.xml` · list `60`, side grouplist `9000` (radiobuttons `7`,`8`; buttons `9`,`5`)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Kodi add-on browser opened from MM ADD-ONS (`bz_mm.py GO['addons']` → `ActivateWindow(addonbrowser)`).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | List 60 rows; top/bottom stay (onup/ondown = 60, no wrap out) |
| Right | Side menu 9000 (Kodi toggles 7/8, buttons 9/5) |
| Left | If `$EXP[bz_navok]` → open MM |
| Back at `addons://` root / empty path | Open MM (`bz_nav=true`) |
| Select | Kodi default (open category / add-on) |
| Menu / C / double-tap Select | Section menu 1119 (context-menu.md) |

## Window props
onload `bz_cmd.py backdrop`; onunload saves `bz_backdrop_last`, clears `bz_backdrop`, `bz_minibig`.

## Related
mm-list.md · context-menu.md · keymaps.md
