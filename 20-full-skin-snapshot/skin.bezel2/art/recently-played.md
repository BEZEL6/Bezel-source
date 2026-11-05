# Recently played — recently-played

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `recently-played` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/recently-played.md) · [layout](../layout/recently-played.md) · [state](../state/recently-played.md) · [motion](../motion/recently-played.md) · [art](../art/recently-played.md) · [input](../input/recently-played.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| — | — | No skin-owned media; uses list art (ListItem.Art) / Kodi textures |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/recently-played.md) line refs. Global inventory: [media-map](media-map.md).
