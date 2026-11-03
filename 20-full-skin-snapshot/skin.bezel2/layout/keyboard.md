# Keyboard (DialogKeyboard 10103) — keyboard

**Object:** `keyboard` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keyboard.md) · [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid). - File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob. - Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKe

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keyboard.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/keyboard.md).

## Control 300 · `button` · `xml/Includes_BezelDialogs.xml` L482
| field | value |
|---|---|

## Control 300 · `button` · `xml/Includes_BezelDialogs.xml` L668
| field | value |
|---|---|
| left | `226` |
| top | `706` |
| width | `138` |
| height | `38` |
| onleft | `8` |
| onright | `9603` |
| onup | `9603` |
| ondown | `9603` |

## Control 300 · `label` · `xml/Includes_MediaMenu.xml` L165
| field | value |
|---|---|
| visible | `Control.IsVisible(31) ¦ Control.IsVisible(5) ¦ Control.IsVisible(6) ¦ Control.IsVisible(7) ¦ Control.IsVisible(8)` |

## Control 312 · `edit` · `xml/Includes_BezelDialogs.xml` L112
| field | value |
|---|---|
| left | `30` |
| top | `116` |
| width | `1240` |
| height | `72` |

## Control 312 · `edit` · `xml/Includes_BezelDialogs.xml` L572
| field | value |
|---|---|
| left | `16` |
| top | `64` |
| width | `348` |
| height | `46` |
| onleft | `9601` |
| onright | `9601` |
| onup | `9601` |
| ondown | `9601` |

## Control 9601 · `wraplist` · `xml/Includes_BezelDialogs.xml` L575
| field | value |
|---|---|
| left | `22` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `SetProperty(bz_kbcaps,1,home)` |
| onright | `9602` |
| onup | `9601` |
| ondown | `9601` |

## Control 9602 · `wraplist` · `xml/Includes_BezelDialogs.xml` L615
| field | value |
|---|---|
| left | `136` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `9601` |
| onright | `9603` |
| onup | `9602` |
| ondown | `9602` |

## Control 9603 · `wraplist` · `xml/Includes_BezelDialogs.xml` L639
| field | value |
|---|---|
| left | `250` |
| top | `162` |
| width | `100` |
| height | `506` |
| orientation | `vertical` |
| focusposition | `5` |
| scrolltime | `180` |
| onleft | `9602` |
| onright | `300` |
| onup | `9603` |
| ondown | `9603` |

