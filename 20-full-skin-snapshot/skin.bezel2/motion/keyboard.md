# Keyboard (DialogKeyboard 10103) — keyboard

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `keyboard` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keyboard.md) · [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid). - File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob. - Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKe

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/keyboard.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/keyboard.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** —

No object-specific animations on referenced controls; uses section fade-in (400 ms sine) from [section-transitions](section-transitions.md).
