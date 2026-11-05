# MM mini-player — mm-mini-player

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-mini-player` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-mini-player.md) · [layout](../layout/mm-mini-player.md) · [state](../state/mm-mini-player.md) · [motion](../motion/mm-mini-player.md) · [art](../art/mm-mini-player.md) · [input](../input/mm-mini-player.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-mini-player.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/mm-mini-player.md).

## Control 120 · `button` · `xml/Includes_BezelDialogs.xml` L203
| field | value |
|---|---|
| onup | `100` |
| ondown | `140` |

## Control 128 · `button` · `xml/Includes_BezelDialogs.xml` L243
| field | value |
|---|---|
| onup | `108` |
| ondown | `148` |

## Control 6910 · `button` · `xml/Includes_Bezel.xml` L542
| field | value |
|---|---|
| left | `318` |
| top | `34` |
| width | `116` |
| height | `52` |
| onleft | `noop` |
| onright | `noop` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `Dialog.Close(1112,true)` |

## Control 6957 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `128` |
| top | `80` |
| width | `44` |
| height | `46` |
| onleft | `noop` |
| onright | `6958` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `PlayerControl(Previous)` |

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

## Control 6959 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `224` |
| top | `80` |
| width | `44` |
| height | `46` |
| onleft | `6958` |
| onright | `6960` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `PlayerControl(Next)` |

## Control 6960 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `286` |
| top | `86` |
| width | `86` |
| height | `34` |
| onleft | `6959` |
| onright | `noop` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `Dialog.Close(1112,true)` |

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

## Control 6967 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `242` |
| top | `78` |
| width | `122` |
| height | `44` |
| onleft | `6966` |
| onright | `noop` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `PlayerControl(Stop)` |

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

