# MM warm (WARM 2.0.1) — LOCKED — mm-warm

**Object:** `mm-warm` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-warm.md) · [layout](../layout/mm-warm.md) · [state](../state/mm-warm.md) · [motion](../motion/mm-warm.md) · [art](../art/mm-warm.md) · [input](../input/mm-warm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
These are the fixed numbers and switches for the whole warm system.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [mm-warm baselines](../port-refs/mm-warm/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/logo.png` | 256×256 | xml/DialogNotification.xml, xml/Includes.xml, xml/Includes_Bezel.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/us_flag.png` | 30×18 | xml/Custom_1118_PowerMenu.xml, xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/mm-warm.md) line refs. Global inventory: [media-map](media-map.md).
