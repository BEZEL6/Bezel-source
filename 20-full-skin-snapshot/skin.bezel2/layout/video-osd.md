# Video OSD — video-osd

**Object:** `video-osd` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/video-osd.md) · [layout](../layout/video-osd.md) · [state](../state/video-osd.md) · [motion](../motion/video-osd.md) · [art](../art/video-osd.md) · [input](../input/video-osd.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/video-osd.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/video-osd.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 6501 · `button` · `xml/Includes_Bezel.xml` L2759
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetFocus(60)` |

## Control 6501 · `button` · `xml/VideoOSD.xml` L24
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6509` |
| ondown | `6502` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6502 · `button` · `xml/Includes_Bezel.xml` L2760
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,A,home)` |

## Control 6502 · `button` · `xml/VideoOSD.xml` L35
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6501` |
| ondown | `6503` |
| onclick (first) | `PlayerControl(Rewind)` |

## Control 6503 · `button` · `xml/Includes_Bezel.xml` L2761
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,B,home)` |

## Control 6503 · `button` · `xml/VideoOSD.xml` L46
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6502` |
| ondown | `6504` |
| onclick (first) | `PlayerControl(Forward)` |

## Control 6504 · `button` · `xml/Includes_Bezel.xml` L2762
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,C,home)` |

## Control 6504 · `button` · `xml/VideoOSD.xml` L57
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6503` |
| ondown | `6505` |
| onclick (first) | `PlayerControl(Stop)` |

## Control 6505 · `button` · `xml/Includes_Bezel.xml` L2763
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,D,home)` |

## Control 6505 · `button` · `xml/VideoOSD.xml` L68
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6504` |
| ondown | `6506` |
| onclick (first) | `ActivateWindow(osdsubtitlesettings)` |

## Control 6506 · `button` · `xml/Includes_Bezel.xml` L2764
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,E,home)` |

## Control 6506 · `button` · `xml/VideoOSD.xml` L79
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6505` |
| ondown | `6507` |
| onclick (first) | `ActivateWindow(osdaudiosettings)` |

## Control 6507 · `button` · `xml/Includes_Bezel.xml` L2765
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,F,home)` |

## Control 6507 · `button` · `xml/VideoOSD.xml` L90
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6506` |
| ondown | `6508` |
| onclick (first) | `ActivateWindow(videobookmarks)` |

## Control 6508 · `button` · `xml/Includes_Bezel.xml` L2766
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,G,home)` |

## Control 6508 · `button` · `xml/VideoOSD.xml` L101
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6507` |
| ondown | `6509` |
| onclick (first) | `ActivateWindow(osdvideosettings)` |

## Control 6509 · `button` · `xml/Includes_Bezel.xml` L2767
| field | value |
|---|---|
| width | `36` |
| height | `31` |
| onclick (first) | `SetProperty(bezel_jump,H,home)` |

## Control 6509 · `button` · `xml/VideoOSD.xml` L112
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `780` |
| height | `72` |
| onleft | `Dialog.Close(videoosd)` |
| onright | `noop` |
| onup | `6508` |
| ondown | `6501` |
| onclick (first) | `Action(Info)` |

