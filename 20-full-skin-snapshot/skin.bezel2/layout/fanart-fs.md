# Fanart FS (visualisation) — fanart-fs

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `fanart-fs` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fanart-fs.md) · [layout](../layout/fanart-fs.md) · [state](../state/fanart-fs.md) · [motion](../motion/fanart-fs.md) · [art](../art/fanart-fs.md) · [input](../input/fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fanart-fs.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/fanart-fs.md).

## Control 6297 · `button` · `xml/MusicVisualisation.xml` L37
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6299 · `button` · `xml/Custom_1112_NowPlaying.xml` L44
| field | value |
|---|---|
| left | `-400` |
| top | `0` |
| width | `10` |
| height | `10` |

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

## Control 6299 · `button` · `xml/MusicVisualisation.xml` L38
| field | value |
|---|---|
| left | `-400` |
| top | `0` |
| width | `10` |
| height | `10` |

## Control 6385 · `button` · `xml/Custom_1112_NowPlaying.xml` L45
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6385 · `button` · `xml/MusicVisualisation.xml` L39
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6390 · `button` · `xml/Includes_Bezel.xml` L2951
| field | value |
|---|---|
| left | `120` |
| top | `120` |
| width | `840` |
| height | `900` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

## Control 6391 · `button` · `xml/Includes_Bezel.xml` L3011
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `6390` |
| onright | `6392` |
| onup | `6390` |
| ondown | `ActivateWindow(1115)` |
| onback | `ClearProperty(bz_np,home)` |
| onclick (first) | `ActivateWindow(1115)` |

## Control 6401 · `button` · `xml/Includes_Bezel.xml` L997
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `Skin.Reset(bz_dfs_mode)` |
| onright | `Skin.Reset(bz_dfs_mode)` |
| onup | `$PARAM[main]` |
| ondown | `$PARAM[main]` |
| onback | `SetProperty(bz_fsret,true,home)` |
| onclick (first) | `Skin.Reset(bz_dfs_mode)` |

## Control 6401 · `button` · `xml/Custom_1115_MusicControls.xml` L26
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6410` |
| ondown | `6402` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6403 · `button` · `xml/Includes_Bezel.xml` L1038
| field | value |
|---|---|
| left | `252` |
| top | `252` |
| width | `96` |
| height | `96` |
| onleft | `6402` |
| onright | `6404` |
| onup | `6401` |
| onback | `Dialog.Close(1120)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6403 · `button` · `xml/Custom_1115_MusicControls.xml` L28
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6402` |
| ondown | `6404` |
| onclick (first) | `PlayerControl(Next)` |

## Control 6407 · `button` · `xml/MusicVisualisation.xml` L43
| field | value |
|---|---|
| left | `90` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(-1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,-1)` |

## Control 6407 · `button` · `xml/Custom_1115_MusicControls.xml` L33
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6406` |
| ondown | `6408` |
| onclick (first) | `PlayerControl(Random)` |

## Control 6408 · `button` · `xml/MusicVisualisation.xml` L43
| field | value |
|---|---|
| left | `1290` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,1)` |

## Control 6408 · `button` · `xml/Custom_1115_MusicControls.xml` L34
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6407` |
| ondown | `6409` |
| onclick (first) | `PlayerControl(Repeat)` |

## Control 6409 · `button` · `xml/MusicVisualisation.xml` L46
| field | value |
|---|---|
| left | `1100` |
| top | `220` |
| width | `680` |
| height | `680` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6409 · `button` · `xml/Custom_1115_MusicControls.xml` L36
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6408` |
| ondown | `6411` |
| onclick (first) | `Dialog.Close(1115)` |

## Control 6410 · `button` · `xml/MusicVisualisation.xml` L45
| field | value |
|---|---|
| left | `960` |
| top | `0` |
| width | `960` |
| height | `1080` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `Skin.SetString(bz_npmode,upnext)` |

## Control 6410 · `button` · `xml/Custom_1115_MusicControls.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6413` |
| ondown | `6401` |
| onclick (first) | `Dialog.Close(1115)` |

## Control 6886 · `button` · `xml/Includes_Bezel.xml` L2268
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |
| onback | `60` |
| onclick (first) | `ActivateWindow(1121)` |

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

