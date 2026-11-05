# Busy dialog — dialog-busy

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `dialog-busy` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialog-busy.md) · [layout](../layout/dialog-busy.md) · [state](../state/dialog-busy.md) · [motion](../motion/dialog-busy.md) · [art](../art/dialog-busy.md) · [input](../input/dialog-busy.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It is Kodi's "working…" indicator, restyled. It waits a moment before showing, so quick loads never flash it. It stays out of the way during music, video, caching and flips.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/dialog-busy.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/dialog-busy.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 1200 ms, 200 ms, 300 ms, 500 ms
