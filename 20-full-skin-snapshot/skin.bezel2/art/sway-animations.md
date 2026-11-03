# Sway animations — shared clock, album, poster, stub cast — sway-animations

**Object:** `sway-animations` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/sway-animations.md) · [layout](../layout/sway-animations.md) · [state](../state/sway-animations.md) · [motion](../motion/sway-animations.md) · [art](../art/sway-animations.md) · [input](../input/sway-animations.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- The big album (Music) and the poster (Movies/TV) slowly rock left and right, like a picture tilting on a wall.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/pn_cast.png` | 160×600 | xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/sway-animations.md) line refs. Global inventory: [media-map](media-map.md).

## 5.33.414 GLAREONE (2026-11-03, Rob t2929u)
Album glare restored to ONE static 600x600 texture (art_mask.png) over the idle big album — GLARESPLIT 300x600 halves (art_mask_hl/hr) removed from static + leaf groups. Sweep (5 s go) + 8.5 s pulse pair, zoom/fade/sway unchanged. Whole glare hidden during hinge fold (bz_hf_a). Cover single when leaf off.
