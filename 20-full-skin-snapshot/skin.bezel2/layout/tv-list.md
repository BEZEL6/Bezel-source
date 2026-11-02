# TV Shows list — tv-list

**Object:** `tv-list` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/tv-list.md) · [layout](../layout/tv-list.md) · [state](../state/tv-list.md) · [motion](../motion/tv-list.md) · [art](../art/tv-list.md) · [input](../input/tv-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [tv-list baselines](../port-refs/tv-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/tv-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/tv-list.md).

## Control 150 · `button` · `xml/Includes_BezelDialogs.xml` L324
| field | value |
|---|---|
| onup | `130` |
| ondown | `170` |

## Control 6098 · `button` · `xml/Includes_Bezel.xml` L2730
| field | value |
|---|---|
| left | `bz_list_x` |
| top | `bz_top` |
| width | `450` |
| height | `60` |
| visible | `$EXP[bz_allrow] + !$EXP[bz_navmenu]` |

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

## Control 6299 · `button` · `xml/Includes_Bezel.xml` L3063
| field | value |
|---|---|
| left | `-400` |
| top | `0` |
| width | `10` |
| height | `10` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |

## Control 6299 · `button` · `xml/Custom_1117_MediaSources.xml` L10
| field | value |
|---|---|
| left | `-10` |
| top | `-10` |
| width | `1` |
| height | `1` |

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

## Control 6600 · `panel` · `xml/Includes_Bezel.xml` L3091
| field | value |
|---|---|
| left | `962` |
| top | `90` |
| width | `904` |
| height | `984` |
| orientation | `vertical` |
| scrolltime | `350` |
| onleft | `60` |
| onback | `60` |
| visible | `$EXP[bz_gridm] + !$EXP[bz_np]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,gridclick)` |

## Control 6600 · `panel` · `xml/Includes_Bezel.xml` L3143
| field | value |
|---|---|
| left | `962` |
| top | `90` |
| width | `888` |
| height | `975` |
| orientation | `vertical` |
| scrolltime | `350` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onback | `60` |
| visible | `$EXP[bz_gridv]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,gridclick)` |

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

