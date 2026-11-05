# Idle Big Album fold (book-page leaf) — idle-big-album-fold

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `idle-big-album-fold` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/idle-big-album-fold.md) · [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [idle-big-album-fold baselines](../port-refs/idle-big-album-fold/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/bz_frame_half_l/r.png` | missing |  |
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/idle-big-album-fold.md) line refs. Global inventory: [media-map](media-map.md).

## 5.33.414 GLAREONE (2026-11-03, Rob t2929u)
Album glare restored to ONE static 600x600 texture (art_mask.png) over the idle big album — GLARESPLIT 300x600 halves (art_mask_hl/hr) removed from static + leaf groups. Sweep (5 s go) + 8.5 s pulse pair, zoom/fade/sway unchanged. Whole glare hidden during hinge fold (bz_hf_a). Cover single when leaf off.
