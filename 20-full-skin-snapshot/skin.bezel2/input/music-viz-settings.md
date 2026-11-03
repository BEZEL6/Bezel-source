# Music OSD / viz settings (dialog 1105) — music-viz-settings

**Object:** `music-viz-settings` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-viz-settings.md) · [layout](../layout/music-viz-settings.md) · [state](../state/music-viz-settings.md) · [motion](../motion/music-viz-settings.md) · [art](../art/music-viz-settings.md) · [input](../input/music-viz-settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-viz-settings.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 5000 | `` | `` | `5000` | `5000` | `` |

**Semantics from behavior (verbatim lines):**
- All rows sit in one vertical grouplist (5000). Kodi moves focus inside it, and Up/Down at either end stays put (onup/ondown point back to 5000).
- | Up / Down | Move; ends stay |
- | Select | Toggle / run row |
- | Back | Close (Kodi default) |
