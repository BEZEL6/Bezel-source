# Kodi Settings — settings

**Object:** `settings` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/settings.md) · [layout](../layout/settings.md) · [state](../state/settings.md) · [motion](../motion/settings.md) · [art](../art/settings.md) · [input](../input/settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/settings.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/settings.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 120 · `button` · `xml/Includes_BezelDialogs.xml` L203
| field | value |
|---|---|
| onup | `100` |
| ondown | `140` |

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

## Control 9000 · `list` · `xml/Settings.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `696` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `noop` |
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

## Control 9000 · `grouplist` · `xml/Custom_1117_MediaSources.xml` L19
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `720` |
| orientation | `vertical` |
| itemgap | `0` |
| visible | `!Window.IsActive(1132)` |

## Control 9130 · `list` · `xml/Custom_1130_BzSettings.xml` L16
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `708` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9130).ListItem.Property(sid)],-1)` |
| onright | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9130).ListItem.Property(sid)],1)` |
| onup | `9130` |
| ondown | `9130` |
| onback | `ClearProperty(bz_setx,home)` |
| visible | `String.IsEmpty(Window(Home).Property(bz_setpg))` |

## Control 9131 · `list` · `xml/Custom_1130_BzSettings.xml` L66
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `708` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9131).ListItem.Property(sid)],-1)` |
| onright | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9131).ListItem.Property(sid)],1)` |
| onup | `9131` |
| ondown | `9131` |
| onback | `RunScript(special://skin/scripts/bz_set.py,pgback)` |
| visible | `String.IsEqual(Window(Home).Property(bz_setpg),services)` |

## Control 9132 · `list` · `xml/Custom_1130_BzSettings.xml` L89
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `708` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9132).ListItem.Property(sid)],-1)` |
| onright | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9132).ListItem.Property(sid)],1)` |
| onup | `9132` |
| ondown | `9132` |
| onback | `RunScript(special://skin/scripts/bz_set.py,pgback)` |
| visible | `String.IsEqual(Window(Home).Property(bz_setpg),display) ¦ String.IsEqual(Window(Home).Property(bz_setpg),audio) ¦ String.IsEqual(Window(Home).Property(bz_setpg),input) ¦ String.IsEqual(Window(Home).Property(bz_setpg),pow` |

## Control 9139 · `button` · `xml/Custom_1130_BzSettings.xml` L104
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1` |
| height | `1` |

