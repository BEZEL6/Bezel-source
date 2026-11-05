# Busy dialog — dialog-busy

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `dialog-busy` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialog-busy.md) · [layout](../layout/dialog-busy.md) · [state](../state/dialog-busy.md) · [motion](../motion/dialog-busy.md) · [art](../art/dialog-busy.md) · [input](../input/dialog-busy.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It is Kodi's "working…" indicator, restyled. It waits a moment before showing, so quick loads never flash it. It stays out of the way during music, video, caching and flips.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/dialog-busy.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/dialog-busy.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 150 · `button` · `xml/Includes_BezelDialogs.xml` L324
| field | value |
|---|---|
| onup | `130` |
| ondown | `170` |

## Control 300 · `button` · `xml/Includes_BezelDialogs.xml` L482
| field | value |
|---|---|

## Control 300 · `button` · `xml/Includes_BezelDialogs.xml` L668
| field | value |
|---|---|
| left | `226` |
| top | `706` |
| width | `138` |
| height | `38` |
| onleft | `8` |
| onright | `9603` |
| onup | `9603` |
| ondown | `9603` |

## Control 300 · `label` · `xml/Includes_MediaMenu.xml` L165
| field | value |
|---|---|
| visible | `Control.IsVisible(31) ¦ Control.IsVisible(5) ¦ Control.IsVisible(6) ¦ Control.IsVisible(7) ¦ Control.IsVisible(8)` |

