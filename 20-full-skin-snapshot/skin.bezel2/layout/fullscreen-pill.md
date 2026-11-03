# Fullscreen pill (Music list) — fullscreen-pill

**Object:** `fullscreen-pill` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-pill.md) · [layout](../layout/fullscreen-pill.md) · [state](../state/fullscreen-pill.md) · [motion](../motion/fullscreen-pill.md) · [art](../art/fullscreen-pill.md) · [input](../input/fullscreen-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fullscreen-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/fullscreen-pill.md).

## Control 6886 · `button` · `xml/Includes_Bezel.xml` L2268
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |
| onback | `60` |
| onclick (first) | `ActivateWindow(1121)` |

