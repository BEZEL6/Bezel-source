# Play Next (1120 non-album mode) — play-next

**Object:** `play-next` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/play-next.md) · [layout](../layout/play-next.md) · [state](../state/play-next.md) · [motion](../motion/play-next.md) · [art](../art/play-next.md) · [input](../input/play-next.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/play-next.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/play-next.md).

## Control 6368 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6378 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6383 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

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

## Control 6398 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6400 · `button` · `xml/Custom_1120_PlayNext.xml` L18
| field | value |
|---|---|
| left | `660` |
| top | `220` |
| width | `600` |
| height | `600` |
| onleft | `PlayerControl(Previous)` |
| onright | `PlayerControl(Next)` |
| onup | `6401` |
| ondown | `SetProperty(bz_noop,1,home)` |
| onback | `SetProperty(bz_fsret,true,home)` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

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

## Control 6405 · `button` · `xml/Custom_1120_PlayNext.xml` L25
| field | value |
|---|---|
| left | `90` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(-1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,-1)` |

## Control 6406 · `button` · `xml/Custom_1120_PlayNext.xml` L25
| field | value |
|---|---|
| left | `1290` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,1)` |

## Control 6407 · `button` · `xml/MusicVisualisation.xml` L43
| field | value |
|---|---|
| left | `90` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(-1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,-1)` |

## Control 6408 · `button` · `xml/MusicVisualisation.xml` L43
| field | value |
|---|---|
| left | `1290` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,1)` |

## Control 6409 · `button` · `xml/MusicVisualisation.xml` L46
| field | value |
|---|---|
| left | `1100` |
| top | `220` |
| width | `680` |
| height | `680` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6410 · `button` · `xml/MusicVisualisation.xml` L45
| field | value |
|---|---|
| left | `960` |
| top | `0` |
| width | `960` |
| height | `1080` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `Skin.SetString(bz_npmode,upnext)` |

## Control 6420 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| onleft | `PlayerControl(Previous)` |
| onright | `PlayerControl(Next)` |
| onup | `6401` |
| ondown | `SetProperty(bz_noop,1,home)` |
| onback | `6422` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

