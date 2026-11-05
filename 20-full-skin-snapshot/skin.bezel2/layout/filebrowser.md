# File browser — filebrowser

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `filebrowser` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/filebrowser.md) · [layout](../layout/filebrowser.md) · [state](../state/filebrowser.md) · [motion](../motion/filebrowser.md) · [art](../art/filebrowser.md) · [input](../input/filebrowser.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/filebrowser.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/filebrowser.md).

## Control 411 · `label` · `xml/FileBrowser.xml` L10
| field | value |
|---|---|
| left | `34` |
| top | `30` |
| width | `340` |
| height | `48` |

## Control 412 · `label` · `xml/FileBrowser.xml` L11
| field | value |
|---|---|
| left | `36` |
| top | `78` |
| width | `336` |
| height | `24` |

## Control 413 · `button` · `xml/FileBrowser.xml` L17
| field | value |
|---|---|
| width | `70` |
| height | `32` |

## Control 414 · `button` · `xml/FileBrowser.xml` L18
| field | value |
|---|---|
| width | `100` |
| height | `32` |

## Control 415 · `button` · `xml/FileBrowser.xml` L19
| field | value |
|---|---|
| width | `120` |
| height | `32` |
| visible | `Control.IsEnabled(415)` |

## Control 416 · `button` · `xml/FileBrowser.xml` L20
| field | value |
|---|---|
| width | `120` |
| height | `32` |
| visible | `Control.IsEnabled(416)` |

## Control 450 · `panel` · `xml/FileBrowser.xml` L12
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `672` |
| scrolltime | `150` |
| onleft | `9100` |
| onright | `9100` |
| onup | `450` |
| ondown | `9100` |

## Control 451 · `panel` · `xml/FileBrowser.xml` L13
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `672` |
| scrolltime | `150` |
| onleft | `9100` |
| onright | `9100` |
| onup | `451` |
| ondown | `9100` |

## Control 9100 · `grouplist` · `xml/FileBrowser.xml` L16
| field | value |
|---|---|
| left | `20` |
| top | `808` |
| width | `360` |
| height | `32` |
| orientation | `horizontal` |
| itemgap | `10` |
| onleft | `9100` |
| onright | `9100` |
| onup | `450` |
| ondown | `450` |

