# NP bar / now-playing chrome — np-bar

**Object:** `np-bar` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/np-bar.md) · [layout](../layout/np-bar.md) · [state](../state/np-bar.md) · [motion](../motion/np-bar.md) · [art](../art/np-bar.md) · [input](../input/np-bar.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/np-bar.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/np-bar.md).

## Control 111 · `button` · `xml/Includes_BezelDialogs.xml` L185
| field | value |
|---|---|
| onup | `171` |
| ondown | `131` |

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

## Control 6385 · `button` · `xml/MyMusicNav.xml` L111
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

## Control 6397 · `grouplist` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| orientation | `horizontal` |
| itemgap | `0` |
| scrolltime | `280` |
| visible | `[String.IsEmpty(Skin.String(bz_at_fsslide)) ¦ String.IsEqual(Skin.String(bz_at_fsslide),3)]` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

## Control 9000 · `grouplist` · `xml/MyMusicNav.xml` L57
| field | value |
|---|---|
| top | `50` |

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

