# Search (dialog 1107) — search

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `search` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/search.md) · [layout](../layout/search.md) · [state](../state/search.md) · [motion](../motion/search.md) · [art](../art/search.md) · [input](../input/search.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/search.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/search.md).

## Control 9000 · `list` · `xml/Custom_1107_SearchDialog.xml` L23
| field | value |
|---|---|
| left | `40` |
| top | `80` |
| width | `370` |
| height | `740` |
| scrolltime | `200` |
| onleft | `9000` |
| onright | `9000` |
| onup | `9000` |
| ondown | `9000` |
| onback | `SetProperty(bz_nav,true,home)` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

## Control 9000 · `grouplist` · `xml/Includes_MediaMenu.xml` L49
| field | value |
|---|---|
| left | `0` |
| top | `50` |
| width | `470` |
| height | `100%` |
| onleft | `9000` |
| onright | `50` |
| onup | `9000` |
| ondown | `14100` |
| onback | `50` |

