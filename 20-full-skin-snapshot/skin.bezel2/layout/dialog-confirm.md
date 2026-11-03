# Confirm dialog — dialog-confirm

**Object:** `dialog-confirm` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialog-confirm.md) · [layout](../layout/dialog-confirm.md) · [state](../state/dialog-confirm.md) · [motion](../motion/dialog-confirm.md) · [art](../art/dialog-confirm.md) · [input](../input/dialog-confirm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's yes/no question in the Main Menu style: a CONFIRM strip with rows and the message on the left. **No** is the first row and gets focus, so a stray Select never confirms by accident. BEZEL uses it for things like "Remove from library".

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/dialog-confirm.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/dialog-confirm.md).

## Control 112 · `button` · `xml/Includes_BezelDialogs.xml` L191
| field | value |
|---|---|
| left | `30` |
| top | `236` |
| width | `1240` |
| height | `72` |
| itemgap | `6` |
| onup | `172` |
| ondown | `132` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

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

