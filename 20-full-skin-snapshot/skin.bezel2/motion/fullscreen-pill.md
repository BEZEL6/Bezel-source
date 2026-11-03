# Fullscreen pill (Music list) — fullscreen-pill

**Object:** `fullscreen-pill` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-pill.md) · [layout](../layout/fullscreen-pill.md) · [state](../state/fullscreen-pill.md) · [motion](../motion/fullscreen-pill.md) · [art](../art/fullscreen-pill.md) · [input](../input/fullscreen-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fullscreen-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/fullscreen-pill.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** —

No object-specific animations on referenced controls; uses section fade-in (400 ms sine) from [section-transitions](section-transitions.md).
