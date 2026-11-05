# Keyboard (DialogKeyboard 10103) — keyboard

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `keyboard` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keyboard.md) · [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid). - File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob. - Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKe

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/keyboard.md) line refs. Global inventory: [media-map](media-map.md).
