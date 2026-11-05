# Options + Info — info-options

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `info-options` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/info-options.md) · [layout](../layout/info-options.md) · [state](../state/info-options.md) · [motion](../motion/info-options.md) · [art](../art/info-options.md) · [input](../input/info-options.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/info-options.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/info-options.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** —

No object-specific animations on referenced controls; uses section fade-in (400 ms sine) from [section-transitions](section-transitions.md).
