# MM list (Main Menu strip) — mm-list

**Object:** `mm-list` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-list.md) · [layout](../layout/mm-list.md) · [state](../state/mm-list.md) · [motion](../motion/mm-list.md) · [art](../art/mm-list.md) · [input](../input/mm-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [mm-list baselines](../port-refs/mm-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/mm-list.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 6894 · `group` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| visible | `String.IsEmpty(Window(Home).Property(bz_mmidle))` |

## Control 6897 · `button` · `xml/Includes_Bezel.xml` L551
| field | value |
|---|---|
| left | `-20` |
| top | `-20` |
| width | `2` |
| height | `2` |
| onleft | `ClearProperty(bz_mmidle,home)` |
| onright | `ClearProperty(bz_mmidle,home)` |
| onup | `ClearProperty(bz_mmidle,home)` |
| ondown | `ClearProperty(bz_mmidle,home)` |
| onback | `ClearProperty(bz_mmidle,home)` |
| visible | `$EXP[bz_navmenu]` |
| onclick (first) | `ClearProperty(bz_mmidle,home)` |

## Control 6898 · `button` · `xml/Includes_Bezel.xml` L531
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| onleft | `6996` |
| onright | `ClearProperty(bz_nav,home)` |
| onup | `6996` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| visible | `$EXP[bz_navmenu]` |
| onclick (first) | `ClearProperty(bz_nav,home)` |

## Control 6899 · `group` · `xml/Includes_Bezel.xml` L530
| field | value |
|---|---|
| visible | `!Window.IsActive(fullscreenvideo) + !Window.IsActive(visualisation)` |

## Control 6958 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `176` |
| top | `80` |
| width | `44` |
| height | `46` |
| onleft | `6957` |
| onright | `6959` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6966 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `112` |
| top | `78` |
| width | `122` |
| height | `44` |
| onleft | `noop` |
| onright | `6967` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `PlayerControl(Play)` |

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

