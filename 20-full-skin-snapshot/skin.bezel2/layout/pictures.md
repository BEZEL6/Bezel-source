# Pictures — pictures

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `pictures` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/pictures.md) · [layout](../layout/pictures.md) · [state](../state/pictures.md) · [motion](../motion/pictures.md) · [art](../art/pictures.md) · [input](../input/pictures.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/pictures.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/pictures.md).

## Control 621 · `button` · `xml/MyPics.xml` L239
| field | value |
|---|---|
| onback | `SetProperty(bz_nav,true,home)` |
| visible | `Container.Content(addons)` |
| onclick (first) | `ActivateWindow(addonbrowser,addons://more/image/,return)` |

## Control 624 · `button` · `xml/MyPics.xml` L233
| field | value |
|---|---|
| onback | `SetProperty(bz_nav,true,home)` |
| visible | `!String.IsEmpty(Container.PluginName)` |
| onclick (first) | `Addon.OpenSettings($INFO[Container.PluginName])` |

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

