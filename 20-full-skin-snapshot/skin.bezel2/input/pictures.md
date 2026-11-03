# Pictures — pictures

**Object:** `pictures` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/pictures.md) · [layout](../layout/pictures.md) · [state](../state/pictures.md) · [motion](../motion/pictures.md) · [art](../art/pictures.md) · [input](../input/pictures.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/pictures.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 621 | `` | `` | `` | `` | `SetProperty(bz_nav,true,home)` |
| 624 | `` | `` | `` | `` | `SetProperty(bz_nav,true,home)` |
| 9000 | `Close` | `Close` | `noop` | `noop` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Kodi Pictures in BEZEL chrome. Back at the sources root, or Left when navok, opens the MM. Menu or double-tap opens the section menu. Draft: not Rob-approved.
- ## Getting back to the MM
- At the top of Pictures, Back opens the main menu.
- Left opens it at any depth, as long as the menu isn't locked.
- Inside a folder, Back goes up a level as usual.
- List 63 and **every** side-menu button carry the same conditional onback, so Back from the side menu at root also opens the MM.
- In a subfolder the condition is false, so Kodi's own Back (parent folder) runs.
- Left uses `$EXP[bz_navok]`: no `bz_navlock`, no `bz_navgrace`, and the MM isn't already open.
- BEZEL adds the Back handling and two visibility gates: plugin settings only inside a plugin, and Get more only on add-on listings.
- ## Section menu (1119) and double-tap
- Press Menu, or double-tap, for a short list: View, Open folder, Picture info, Slideshow, Recursive slideshow, Sort by, Order, Favourite.
- `pictures` is in `bz_dtap.py` SECW. A single tap is Select after the tap window. A double tap (or c/menu/title via the noctx keymap) opens 1119 instead of Kodi's context menu.
