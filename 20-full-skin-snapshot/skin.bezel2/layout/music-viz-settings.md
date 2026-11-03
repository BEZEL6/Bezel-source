# Music OSD / viz settings (dialog 1105) — music-viz-settings

**Object:** `music-viz-settings` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-viz-settings.md) · [layout](../layout/music-viz-settings.md) · [state](../state/music-viz-settings.md) · [motion](../motion/music-viz-settings.md) · [art](../art/music-viz-settings.md) · [input](../input/music-viz-settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-viz-settings.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/music-viz-settings.md).

## Control 5000 · `grouplist` · `xml/Custom_1105_MusicOSDSettings.xml` L20
| field | value |
|---|---|
| width | `600` |
| height | `700` |
| orientation | `vertical` |
| itemgap | `0` |
| onup | `5000` |
| ondown | `5000` |

## Control 5001 · `radiobutton` · `xml/Custom_1105_MusicOSDSettings.xml` L27
| field | value |
|---|---|
| width | `600` |
| onclick (first) | `Skin.ToggleSetting(hide_background_fanart)` |

## Control 5002 · `radiobutton` · `xml/Custom_1105_MusicOSDSettings.xml` L34
| field | value |
|---|---|
| onclick (first) | `Skin.ToggleSetting(animate_background_fanart)` |

## Control 5004 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L40
| field | value |
|---|---|
| width | `600` |
| onclick (first) | `Dialog.Close(1105)` |

## Control 5005 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L49
| field | value |
|---|---|
| width | `600` |
| onclick (first) | `Addon.Default.OpenSettings(xbmc.player.musicviz)` |

## Control 5006 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L55
| field | value |
|---|---|
| width | `600` |
| visible | `Visualisation.HasPresets` |
| onclick (first) | `ActivateWindow(visualisationpresetlist)` |

## Control 5007 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L62
| field | value |
|---|---|
| width | `600` |
| onclick (first) | `Skin.SetAddon(LyricScript_Path,xbmc.python.lyrics)` |

## Control 5008 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L69
| field | value |
|---|---|
| width | `600` |
| visible | `!String.IsEmpty(Skin.String(LyricScript_Path))` |
| onclick (first) | `Addon.OpenSettings($INFO[Skin.String(LyricScript_Path)])` |

## Control 5009 · `button` · `xml/Custom_1105_MusicOSDSettings.xml` L76
| field | value |
|---|---|
| width | `600` |
| onclick (first) | `Dialog.Close(all)` |

