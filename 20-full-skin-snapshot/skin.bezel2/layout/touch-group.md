# Touch / tap inputs — touch-group

**Object:** `touch-group` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/touch-group.md) · [layout](../layout/touch-group.md) · [state](../state/touch-group.md) · [motion](../motion/touch-group.md) · [art](../art/touch-group.md) · [input](../input/touch-group.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/touch-group.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/touch-group.md).

## Control 6001 · `button` · `xml/Includes_Bezel.xml` L639
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `120` |
| height | `116` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onright | `60` |
| onup | `6001` |
| ondown | `60` |
| visible | `!$EXP[bz_navmenu]` |
| onclick (first) | `ClearProperty(bz_np,home)` |

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

