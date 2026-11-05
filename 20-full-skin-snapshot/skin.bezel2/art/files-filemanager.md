# File manager — files-filemanager

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `files-filemanager` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/files-filemanager.md) · [layout](../layout/files-filemanager.md) · [state](../state/files-filemanager.md) · [motion](../motion/files-filemanager.md) · [art](../art/files-filemanager.md) · [input](../input/files-filemanager.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It opens with a random backdrop. Back at the top of a pane opens the Main Menu.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/logo.png` | 256×256 | xml/DialogNotification.xml, xml/Includes.xml, xml/Includes_Bezel.xml, xml/Includes_DialogSelect.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/files-filemanager.md) line refs. Global inventory: [media-map](media-map.md).
