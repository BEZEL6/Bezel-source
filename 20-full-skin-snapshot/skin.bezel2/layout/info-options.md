# Options + Info — info-options

**Object:** `info-options` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/info-options.md) · [layout](../layout/info-options.md) · [state](../state/info-options.md) · [motion](../motion/info-options.md) · [art](../art/info-options.md) · [input](../input/info-options.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/info-options.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/info-options.md).

## Control 443 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEmpty(ListItem.SetID)` |
| onclick (first) | `Dialog.Close(all,true)` |

## Control 7710 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,chooseart,$INFO[ListItem.DBType],$INFO[ListItem.DBID])` |

## Control 7710 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,chooseart,$INFO[ListItem.DBType],$INFO[ListItem.DBID])` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

## Control 9000 · `grouplist` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| left | `582` |
| top | `166` |
| width | `360` |
| height | `420` |
| orientation | `vertical` |
| itemgap | `2` |
| onleft | `Close` |
| onright | `Close` |
| onup | `noop` |
| ondown | `9000` |

## Control 9000 · `grouplist` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| left | `582` |
| top | `166` |
| width | `360` |
| height | `276` |
| orientation | `vertical` |
| itemgap | `2` |
| onleft | `Close` |
| onright | `Close` |
| onup | `noop` |
| ondown | `50` |

## Control 9081 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,artist)` |
| onclick (first) | `QueueMedia($VAR[BzPlayNextPath],playnext)` |

## Control 9081 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + [String.IsEqual(ListItem.DBType,movie) ¦ String.IsEqual(ListItem.DBType,episode) ¦ String.IsEqual(ListItem.DBType,musicvideo)]` |
| onclick (first) | `QueueMedia($VAR[BzPlayNextPath],playnext)` |

## Control 9082 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more))` |
| onclick (first) | `Dialog.Close(musicinformation)` |

## Control 9082 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + [String.IsEqual(ListItem.DBType,movie) ¦ String.IsEqual(ListItem.DBType,episode) ¦ String.IsEqual(ListItem.DBType,musicvideo)]` |
| onclick (first) | `Dialog.Close(movieinformation)` |

## Control 9083 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,artist) + !String.IsEmpty(ListItem.Artist)` |
| onclick (first) | `Dialog.Close(all,true)` |

## Control 9084 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + String.IsEqual(ListItem.DBType,artist) + !String.IsEmpty(ListItem.DBID)` |
| onclick (first) | `Dialog.Close(all,true)` |

## Control 9085 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more)) + String.IsEqual(ListItem.DBType,tvshow)` |
| onclick (first) | `Dialog.Close(all,true)` |

## Control 9089 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more))` |
| onclick (first) | `SetProperty(bz_ci_more,1)` |

## Control 9089 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more))` |
| onclick (first) | `SetProperty(bz_ci_more,1)` |

## Control 9095 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| visible | `String.IsEmpty(Window.Property(bz_ci_more))` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,fav)` |

## Control 9095 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEqual(Window.Property(bz_ci_more),1) + !String.IsEqual(ListItem.DBType,season)` |
| onclick (first) | `Dialog.Close(movieinformation)` |

## Control 9097 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,fav)` |

## Control 9098 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| visible | `String.IsEqual(Window.Property(bz_ci_more),1) + !String.IsEmpty(ListItem.DBID) + !String.IsEqual(ListItem.DBType,season)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,remove,$INFO[ListItem.DBType],$INFO[ListItem.DBID])` |

## Control 9969 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec) + String.IsEmpty(Container.FolderPath) + String.IsEmpty(Container.PluginName)` |
| onclick (first) | `Dialog.Close(musicinformation)` |

## Control 9969 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec) + [String.IsEqual(ListItem.DBType,tvshow) ¦ String.IsEqual(ListItem.DBType,season) ¦ String.IsEqual(ListItem.DBType,episode)]` |
| onclick (first) | `Skin.ToggleSetting(bz_tvclear_off)` |

## Control 9971 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Dialog.Close(musicinformation)` |

## Control 9971 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Dialog.Close(movieinformation)` |

## Control 9974 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Addon.Default.Set(xbmc.player.musicviz)` |

## Control 9978 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Skin.Reset(bz_albview_a)` |

## Control 9978 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec) + Container.Content(addons)` |
| onclick (first) | `Dialog.Close(musicinformation)` |

## Control 9979 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Skin.Reset(bz_grid_music)` |

## Control 9979 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `Dialog.Close(movieinformation)` |

## Control 9980 · `button` · `xml/DialogMusicInfo.xml` L14
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| onclick (first) | `SetProperty(bz_ci_more,sec)` |

## Control 9980 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| onup | `9000` |
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEmpty(Window.Property(bz_ci_more))` |
| onclick (first) | `SetProperty(bz_ci_more,sec)` |

## Control 9990 · `button` · `xml/DialogVideoInfo.xml` L13
| field | value |
|---|---|
| onback | `ClearProperty(bz_ci_more)` |
| visible | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| onclick (first) | `ClearProperty(bz_ci_more)` |

