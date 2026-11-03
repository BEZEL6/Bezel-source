# File browser — filebrowser

**Object:** `filebrowser` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/filebrowser.md) · [layout](../layout/filebrowser.md) · [state](../state/filebrowser.md) · [motion](../motion/filebrowser.md) · [art](../art/filebrowser.md) · [input](../input/filebrowser.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/set_chev_dn.png` | 32×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/filebrowser.md) line refs. Global inventory: [media-map](media-map.md).
