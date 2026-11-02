# Keymaps (BEZEL profile keymaps) — keymaps

**Object:** `keymaps` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keymaps.md) · [layout](../layout/keymaps.md) · [state](../state/keymaps.md) · [motion](../motion/keymaps.md) · [art](../art/keymaps.md) · [input](../input/keymaps.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A skin cannot ship keymaps, so BEZEL writes its own into the Kodi profile while BEZEL is the skin. It removes them again as soon as you switch skins, so other skins behave normally.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keymaps.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/keymaps.md).

## Control 6422 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L51
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6422 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,2,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` |
| onup | `6421` |
| ondown | `6423` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` |

## Control 9880 · `fadelabel` · `xml/Includes_Bezel.xml` L690
| field | value |
|---|---|
| left | `-4000` |
| top | `0` |
| width | `20` |
| height | `20` |
| visible | `!Skin.HasSetting(bezel_norotate)` |

