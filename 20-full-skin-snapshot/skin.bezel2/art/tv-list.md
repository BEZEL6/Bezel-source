# TV Shows list — tv-list

**Object:** `tv-list` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/tv-list.md) · [layout](../layout/tv-list.md) · [state](../state/tv-list.md) · [motion](../motion/tv-list.md) · [art](../art/tv-list.md) · [input](../input/tv-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [tv-list baselines](../port-refs/tv-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/tv-list.md) line refs. Global inventory: [media-map](media-map.md).
