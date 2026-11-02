# Recently played — recently-played

**Object:** `recently-played` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/recently-played.md) · [layout](../layout/recently-played.md) · [state](../state/recently-played.md) · [motion](../motion/recently-played.md) · [art](../art/recently-played.md) · [input](../input/recently-played.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/recently-played.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/recently-played.md).

## Control 6097 · `button` · `xml/Includes_Bezel.xml` L2196
| field | value |
|---|---|
| visible | `!$EXP[bz_covercol] ¦ $EXP[bz_allpick]` |

## Control 6100 · `grouplist` · `xml/Includes_Bezel.xml` L2222
| field | value |
|---|---|
| left | `78` |
| top | `151` |
| width | `36` |
| height | `837` |
| orientation | `vertical` |
| itemgap | `0` |
| onleft | `60` |
| onright | `60` |
| visible | `!$EXP[bz_navmenu]` |

## Control 6500 · `grouplist` · `xml/Includes_Bezel.xml` L2748
| field | value |
|---|---|
| left | `78` |
| top | `151` |
| width | `36` |
| height | `837` |
| orientation | `vertical` |
| itemgap | `0` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onright | `60` |
| visible | `!$EXP[bz_navmenu]` |

