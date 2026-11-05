# Sway animations — shared clock, album, poster, stub cast — sway-animations

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `sway-animations` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/sway-animations.md) · [layout](../layout/sway-animations.md) · [state](../state/sway-animations.md) · [motion](../motion/sway-animations.md) · [art](../art/sway-animations.md) · [input](../input/sway-animations.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- The big album (Music) and the poster (Movies/TV) slowly rock left and right, like a picture tilting on a wall.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/sway-animations.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/sway-animations.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 10000 ms, 12250 ms, 1810 ms, 2000 ms, 2200 ms, 2700 ms, 3450 ms, 5000 ms, 5500 ms
