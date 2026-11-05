# Add-ons browser — addons

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `addons` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/addons.md) · [layout](../layout/addons.md) · [state](../state/addons.md) · [motion](../motion/addons.md) · [art](../art/addons.md) · [input](../input/addons.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Pick ADD-ONS in the Main Menu and Kodi's add-on browser opens in BEZEL chrome with a random backdrop. Press Back at the top level and the Main Menu opens again.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/addons.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/addons.md).

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

## Control 9000 · `grouplist` · `xml/Custom_1119_SecCtx.xml` L16
| field | value |
|---|---|
| left | `582` |
| top | `166` |
| width | `360` |
| height | `430` |
| orientation | `vertical` |
| itemgap | `2` |
| onleft | `Close` |
| onright | `Close` |
| onup | `noop` |
| ondown | `noop` |

## Control 9000 · `grouplist` · `xml/DialogAddonInfo.xml` L13
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `440` |
| orientation | `vertical` |
| itemgap | `0` |
| onleft | `Close` |
| onright | `Close` |
| onup | `noop` |
| ondown | `noop` |
| onback | `Close` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

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

## Control 9140 · `list` · `xml/Custom_1131_BzAddons.xml` L13
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `720` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9140).ListItem.Property(sid)],-1)` |
| onright | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Container(9140).ListItem.Property(sid)],1)` |
| onup | `9140` |
| ondown | `9140` |
| onback | `Dialog.Close(1131)` |

