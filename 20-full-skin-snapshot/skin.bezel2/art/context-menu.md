# Section menu (context) — context-menu

**Object:** `context-menu` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/context-menu.md) · [layout](../layout/context-menu.md) · [state](../state/context-menu.md) · [motion](../motion/context-menu.md) · [art](../art/context-menu.md) · [input](../input/context-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/set_chev_dn.png` | 32×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/set_chev_up.png` | 32×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/context-menu.md) line refs. Global inventory: [media-map](media-map.md).
