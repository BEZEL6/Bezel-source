# MM warm (WARM 2.0.1) — LOCKED — mm-warm

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-warm` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-warm.md) · [layout](../layout/mm-warm.md) · [state](../state/mm-warm.md) · [motion](../motion/mm-warm.md) · [art](../art/mm-warm.md) · [input](../input/mm-warm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
These are the fixed numbers and switches for the whole warm system.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [mm-warm baselines](../port-refs/mm-warm/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-warm.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/mm-warm.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 124 · `button` · `xml/Includes_BezelDialogs.xml` L223
| field | value |
|---|---|
| onup | `104` |
| ondown | `144` |

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

## Control 6996 · `list` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `0` |
| top | `40` |
| width | `390` |
| height | `728` |
| scrolltime | `150` |
| onleft | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` |
| onright | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` |
| onup | `6966` |
| ondown | `SetFocus(6996,0,absolute)` |
| visible | `$EXP[bz_navmenu] + !Window.IsVisible(1118) + !String.IsEqual(Window(Home).Property(bz_navtune),true) + !String.IsEqual(Window(Home).Property(bz_navbez),true)` |

## Control 9880 · `fadelabel` · `xml/Includes_Bezel.xml` L690
| field | value |
|---|---|
| left | `-4000` |
| top | `0` |
| width | `20` |
| height | `20` |
| visible | `!Skin.HasSetting(bezel_norotate)` |

