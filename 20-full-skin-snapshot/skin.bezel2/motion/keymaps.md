# Keymaps (BEZEL profile keymaps) — keymaps

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `keymaps` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keymaps.md) · [layout](../layout/keymaps.md) · [state](../state/keymaps.md) · [motion](../motion/keymaps.md) · [art](../art/keymaps.md) · [input](../input/keymaps.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A skin cannot ship keymaps, so BEZEL writes its own into the Kodi profile while BEZEL is the skin. It removes them again as soon as you switch skins, so other skins behave normally.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keymaps.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/keymaps.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 20 ms, 25 ms, 600 ms
