# Now playing (dialog 1112) — now-playing

**Object:** `now-playing` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/now-playing.md) · [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [now-playing baselines](../port-refs/now-playing/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/np_prev.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/now-playing.md) line refs. Global inventory: [media-map](media-map.md).
