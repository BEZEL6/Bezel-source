# Section menu (context) — context-menu

**Object:** `context-menu` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/context-menu.md) · [layout](../layout/context-menu.md) · [state](../state/context-menu.md) · [motion](../motion/context-menu.md) · [art](../art/context-menu.md) · [input](../input/context-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/context-menu.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/context-menu.md).

## Control 7901 · `button` · `xml/Custom_1119_SecCtx.xml` L17
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7902 · `button` · `xml/Custom_1119_SecCtx.xml` L18
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7903 · `button` · `xml/Custom_1119_SecCtx.xml` L19
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)] + !String.IsEmpty(ListItem.Property(Addon.ID)) + ListItem.Property(addon.isinstalled)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7904 · `button` · `xml/Custom_1119_SecCtx.xml` L45
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)] ¦ [Window.IsActive(musicplaylist) ¦ Window.IsActive(videoplaylist)] ¦ [Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,fav)` |

## Control 7905 · `button` · `xml/Custom_1119_SecCtx.xml` L20
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7906 · `button` · `xml/Custom_1119_SecCtx.xml` L21
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)] ¦ [Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7907 · `button` · `xml/Custom_1119_SecCtx.xml` L22
| field | value |
|---|---|
| visible | `[Window.IsActive(programs) ¦ Window.IsActive(games) ¦ Window.IsActive(addonbrowser)] ¦ [Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7908 · `button` · `xml/Custom_1119_SecCtx.xml` L23
| field | value |
|---|---|
| visible | `Window.IsActive(programs)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7909 · `button` · `xml/Custom_1119_SecCtx.xml` L24
| field | value |
|---|---|
| visible | `Window.IsActive(games)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7910 · `button` · `xml/Custom_1119_SecCtx.xml` L25
| field | value |
|---|---|
| visible | `Window.IsActive(addonbrowser)` |
| onclick (first) | `Dialog.Close(1119,true)` |

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

## Control 7920 · `button` · `xml/Custom_1119_SecCtx.xml` L35
| field | value |
|---|---|
| visible | `[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7921 · `button` · `xml/Custom_1119_SecCtx.xml` L36
| field | value |
|---|---|
| visible | `[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)] ¦ [Window.IsActive(tvguide) ¦ Window.IsActive(radioguide)] ¦ [Window.IsActive(tvsearch) ¦ Window.IsActive(radiosearch)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7922 · `button` · `xml/Custom_1119_SecCtx.xml` L37
| field | value |
|---|---|
| visible | `[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)] ¦ [Window.IsActive(tvguide) ¦ Window.IsActive(radioguide)] ¦ [Window.IsActive(tvsearch) ¦ Window.IsActive(radiosearch)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7923 · `button` · `xml/Custom_1119_SecCtx.xml` L38
| field | value |
|---|---|
| visible | `[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7924 · `button` · `xml/Custom_1119_SecCtx.xml` L39
| field | value |
|---|---|
| visible | `[Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7926 · `button` · `xml/Custom_1119_SecCtx.xml` L41
| field | value |
|---|---|
| visible | `[Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7927 · `button` · `xml/Custom_1119_SecCtx.xml` L42
| field | value |
|---|---|
| visible | `[Window.IsActive(tvtimers) ¦ Window.IsActive(radiotimers) ¦ Window.IsActive(tvtimerrules) ¦ Window.IsActive(radiotimerrules)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7929 · `button` · `xml/Custom_1119_SecCtx.xml` L44
| field | value |
|---|---|
| visible | `[Window.IsActive(tvtimers) ¦ Window.IsActive(radiotimers) ¦ Window.IsActive(tvtimerrules) ¦ Window.IsActive(radiotimerrules)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7930 · `button` · `xml/Custom_1119_SecCtx.xml` L46
| field | value |
|---|---|
| visible | `[[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)] ¦ [Window.IsActive(tvguide) ¦ Window.IsActive(radioguide)] ¦ [Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)] ¦ [Window.IsActive(tvtimers)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7931 · `button` · `xml/Custom_1119_SecCtx.xml` L47
| field | value |
|---|---|
| visible | `[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)]` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7932 · `button` · `xml/Custom_1119_SecCtx.xml` L48
| field | value |
|---|---|
| visible | `[[Window.IsActive(tvchannels) ¦ Window.IsActive(radiochannels)] ¦ [Window.IsActive(tvguide) ¦ Window.IsActive(radioguide)] ¦ [Window.IsActive(tvrecordings) ¦ Window.IsActive(radiorecordings)] ¦ [Window.IsActive(tvtimers)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7940 · `button` · `xml/Custom_1119_SecCtx.xml` L49
| field | value |
|---|---|
| visible | `Window.IsActive(pictures) + !ListItem.IsFolder` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7941 · `button` · `xml/Custom_1119_SecCtx.xml` L50
| field | value |
|---|---|
| visible | `Window.IsActive(pictures) + ListItem.IsFolder + !ListItem.IsParentFolder` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7942 · `button` · `xml/Custom_1119_SecCtx.xml` L51
| field | value |
|---|---|
| visible | `Window.IsActive(pictures) + !ListItem.IsFolder` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7943 · `button` · `xml/Custom_1119_SecCtx.xml` L52
| field | value |
|---|---|
| visible | `Window.IsActive(pictures)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7944 · `button` · `xml/Custom_1119_SecCtx.xml` L53
| field | value |
|---|---|
| visible | `Window.IsActive(pictures)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7945 · `button` · `xml/Custom_1119_SecCtx.xml` L54
| field | value |
|---|---|
| visible | `Window.IsActive(pictures)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7946 · `button` · `xml/Custom_1119_SecCtx.xml` L55
| field | value |
|---|---|
| visible | `Window.IsActive(pictures)` |
| onclick (first) | `Dialog.Close(1119,true)` |

## Control 7947 · `button` · `xml/Custom_1119_SecCtx.xml` L56
| field | value |
|---|---|
| visible | `Window.IsActive(pictures)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_ctx.py,fav)` |

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

