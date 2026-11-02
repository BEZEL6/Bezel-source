# Dust (ambient particle layers) — dust

**Object:** `dust` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dust.md) · [layout](../layout/dust.md) · [state](../state/dust.md) · [motion](../motion/dust.md) · [art](../art/dust.md) · [input](../input/dust.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Slow drifting dust in the black space of the screen. It starts once after the splash and keeps drifting across window changes, so it never restarts or jumps.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/dust.md) line refs. Global inventory: [media-map](media-map.md).
