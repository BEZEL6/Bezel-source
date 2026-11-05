# Media sources — media-sources

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `media-sources` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/media-sources.md) · [layout](../layout/media-sources.md) · [state](../state/media-sources.md) · [motion](../motion/media-sources.md) · [art](../art/media-sources.md) · [input](../input/media-sources.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/media-sources.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/media-sources.md).

## Control 120 · `button` · `xml/Includes_BezelDialogs.xml` L203
| field | value |
|---|---|
| onup | `100` |
| ondown | `140` |

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

## Control 311 · `label` · `xml/Includes_BezelDialogs.xml` L107
| field | value |
|---|---|
| left | `30` |
| top | `20` |
| width | `1230` |
| height | `62` |

## Control 311 · `label` · `xml/Includes_BezelDialogs.xml` L570
| field | value |
|---|---|
| left | `20` |
| top | `14` |
| width | `340` |
| height | `40` |

## Control 312 · `edit` · `xml/Includes_BezelDialogs.xml` L112
| field | value |
|---|---|
| left | `30` |
| top | `116` |
| width | `1240` |
| height | `72` |

## Control 312 · `edit` · `xml/Includes_BezelDialogs.xml` L572
| field | value |
|---|---|
| left | `16` |
| top | `64` |
| width | `348` |
| height | `46` |
| onleft | `9601` |
| onright | `9601` |
| onup | `9601` |
| ondown | `9601` |

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

## Control 7100 · `button` · `xml/Custom_1117_MediaSources.xml` L20
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7131` |
| ondown | `7101` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_set.py,x2,bz_msx,v)` |

## Control 7101 · `button` · `xml/Custom_1117_MediaSources.xml` L21
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7100` |
| ondown | `7102` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `SetProperty(bz_msret,1,home)` |

## Control 7102 · `button` · `xml/Custom_1117_MediaSources.xml` L22
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7101` |
| ondown | `7103` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `UpdateLibrary(video)` |

## Control 7103 · `button` · `xml/Custom_1117_MediaSources.xml` L23
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7102` |
| ondown | `7104` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `CleanLibrary(video)` |

## Control 7104 · `button` · `xml/Custom_1117_MediaSources.xml` L24
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7103` |
| ondown | `7105` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `ExportLibrary(video)` |

## Control 7105 · `button` · `xml/Custom_1117_MediaSources.xml` L25
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7104` |
| ondown | `7106` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `SetProperty(bz_msfocus,7105,home)` |

## Control 7111 · `button` · `xml/Custom_1117_MediaSources.xml` L28
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7110` |
| ondown | `7112` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `SetProperty(bz_msret,1,home)` |

## Control 7112 · `button` · `xml/Custom_1117_MediaSources.xml` L29
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7111` |
| ondown | `7113` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `UpdateLibrary(music)` |

## Control 7114 · `button` · `xml/Custom_1117_MediaSources.xml` L31
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7113` |
| ondown | `7115` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `ExportLibrary(music)` |

## Control 7115 · `button` · `xml/Custom_1117_MediaSources.xml` L32
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7114` |
| ondown | `7116` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `SetProperty(bz_msfocus,7115,home)` |

## Control 7121 · `button` · `xml/Custom_1117_MediaSources.xml` L35
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `noop` |
| onright | `noop` |
| onup | `7120` |
| ondown | `7130` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `SetProperty(bz_msret,1,home)` |

## Control 7131 · `button` · `xml/Custom_1117_MediaSources.xml` L37
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `48` |
| onleft | `RunScript(special://skin/scripts/bz_set.py,cyc,videolibrary.backgroundupdate,-1)` |
| onright | `RunScript(special://skin/scripts/bz_set.py,cyc,videolibrary.backgroundupdate,1)` |
| onup | `7130` |
| ondown | `7100` |
| onback | `SetProperty(bz_nav,true,home)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_set.py,cyc,videolibrary.backgroundupdate,1)` |

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

## Control 9000 · `grouplist` · `xml/Includes_MediaMenu.xml` L49
| field | value |
|---|---|
| left | `0` |
| top | `50` |
| width | `470` |
| height | `100%` |
| onleft | `9000` |
| onright | `50` |
| onup | `9000` |
| ondown | `14100` |
| onback | `50` |

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

## Control 9150 · `list` · `xml/Custom_1132_BzSources.xml` L10
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `720` |
| orientation | `vertical` |
| scrolltime | `150` |
| onleft | `noop` |
| onright | `noop` |
| onup | `9150` |
| ondown | `9150` |
| onback | `Dialog.Close(1132)` |
| onclick (first) | `SetProperty(bz_msret,1,home)` |

## Control 9601 · `wraplist` · `xml/Includes_BezelDialogs.xml` L575
| field | value |
|---|---|
| left | `22` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `SetProperty(bz_kbcaps,1,home)` |
| onright | `9602` |
| onup | `9601` |
| ondown | `9601` |

## Control 9602 · `wraplist` · `xml/Includes_BezelDialogs.xml` L615
| field | value |
|---|---|
| left | `136` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `9601` |
| onright | `9603` |
| onup | `9602` |
| ondown | `9602` |

## Control 9603 · `wraplist` · `xml/Includes_BezelDialogs.xml` L639
| field | value |
|---|---|
| left | `250` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `9602` |
| onright | `300` |
| onup | `9603` |
| ondown | `9603` |

- 5.33.362: Add Source title uses bz_mm28 (width 356) so full ADD VIDEO/MUSIC/PICTURE SOURCE fits; Warm strip unchanged.
