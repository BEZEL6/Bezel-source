# Playlists — playlists

**Object:** `playlists` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/playlists.md) · [layout](../layout/playlists.md) · [state](../state/playlists.md) · [motion](../motion/playlists.md) · [art](../art/playlists.md) · [input](../input/playlists.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/playlists.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/playlists.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 203 · `label` · `xml/MyPlaylist.xml` L52
| field | value |
|---|---|

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

## Control 7904 · `button` · `xml/Custom_1119_SecCtx.xml` L45
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)] ¦ [Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)] ¦ [Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,fav)` |

## Control 7911 · `button` · `xml/Custom_1119_SecCtx.xml` L26
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7912 · `button` · `xml/Custom_1119_SecCtx.xml` L27
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7913 · `button` · `xml/Custom_1119_SecCtx.xml` L28
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7914 · `button` · `xml/Custom_1119_SecCtx.xml` L29
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7915 · `button` · `xml/Custom_1119_SecCtx.xml` L30
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7916 · `button` · `xml/Custom_1119_SecCtx.xml` L31
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7917 · `button` · `xml/Custom_1119_SecCtx.xml` L32
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7918 · `button` · `xml/Custom_1119_SecCtx.xml` L33
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7919 · `button` · `xml/Custom_1119_SecCtx.xml` L34
| field | value |
|---|---|
| visible | `[Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

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

## Control 9000 · `grouplist` · `xml/MyPlaylist.xml` L49
| field | value |
|---|---|
| top | `50` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

