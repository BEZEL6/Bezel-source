# Skin settings / BEZEL Tuner — skin-settings-tuner

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `skin-settings-tuner` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/skin-settings-tuner.md) · [layout](../layout/skin-settings-tuner.md) · [state](../state/skin-settings-tuner.md) · [motion](../motion/skin-settings-tuner.md) · [art](../art/skin-settings-tuner.md) · [input](../input/skin-settings-tuner.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [skin-settings-tuner baselines](../port-refs/skin-settings-tuner/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/skin-settings-tuner.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/skin-settings-tuner.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 140 · `button` · `xml/Includes_BezelDialogs.xml` L274
| field | value |
|---|---|
| onup | `120` |
| ondown | `160` |

## Control 150 · `button` · `xml/Includes_BezelDialogs.xml` L324
| field | value |
|---|---|
| onup | `130` |
| ondown | `170` |

## Control 6968 · `list` · `xml/Includes_Tuner.xml` L484
| field | value |
|---|---|
| left | `570` |
| top | `140` |
| width | `390` |
| height | `870` |
| orientation | `vertical` |
| scrolltime | `200` |
| onleft | `noop` |
| onright | `noop` |
| onback | `ClearProperty(bz_navbez,home)` |
| onclick (first) | `Skin.ToggleSetting(bz_allseasons)` |

## Control 6970 · `list` · `xml/Includes_Tuner.xml` L497
| field | value |
|---|---|
| left | `570` |
| top | `140` |
| width | `390` |
| height | `870` |
| orientation | `vertical` |
| scrolltime | `200` |
| onleft | `SetProperty(bz_tune_dirty,1,home)` |
| onright | `SetProperty(bz_tune_dirty,1,home)` |
| onup | `noop` |
| ondown | `noop` |
| onback | `ClearProperty(bz_navtune,home)` |

## Control 6975 · `group` · `xml/Includes_Tuner.xml` L493
| field | value |
|---|---|
| visible | `$EXP[bz_navmenu] + String.IsEqual(Window(Home).Property(bz_navtune),true)` |

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

