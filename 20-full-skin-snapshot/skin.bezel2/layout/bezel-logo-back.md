# BEZEL logo / Back button — bezel-logo-back

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `bezel-logo-back` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/bezel-logo-back.md) · [layout](../layout/bezel-logo-back.md) · [state](../state/bezel-logo-back.md) · [motion](../motion/bezel-logo-back.md) · [art](../art/bezel-logo-back.md) · [input](../input/bezel-logo-back.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The BEZEL logo sits top-left and takes the skin tint. About every 30 seconds it does one spin.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/bezel-logo-back.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/bezel-logo-back.md).

## Control 6001 · `button` · `xml/Includes_Bezel.xml` L639
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `120` |
| height | `116` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onright | `60` |
| onup | `6001` |
| ondown | `60` |
| visible | `!$EXP[bz_navmenu]` |
| onclick (first) | `ClearProperty(bz_np,home)` |

