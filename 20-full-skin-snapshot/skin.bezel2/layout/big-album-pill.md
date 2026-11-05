# Big album pill — big-album-pill

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `big-album-pill` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/big-album-pill.md) · [layout](../layout/big-album-pill.md) · [state](../state/big-album-pill.md) · [motion](../motion/big-album-pill.md) · [art](../art/big-album-pill.md) · [input](../input/big-album-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The **big album pill** is the ALBUM ↔ PREV/NEXT mode control. It looks the same, sits in the same place and works the same on Dialogue FS and on full screen album viz. It is **not** the fan art pill (`6391`, fanart-fs.md).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/big-album-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/big-album-pill.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

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

