# Music section list — music-list

**Object:** `music-list` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-list.md) · [layout](../layout/music-list.md) · [state](../state/music-list.md) · [motion](../motion/music-list.md) · [art](../art/music-list.md) · [input](../input/music-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [music-list baselines](../port-refs/music-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/logo.png` | 256×256 | xml/DialogNotification.xml, xml/Includes.xml, xml/Includes_Bezel.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/set_chev_dn.png` | 32×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/set_chev_up.png` | 32×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/music-list.md) line refs. Global inventory: [media-map](media-map.md).
