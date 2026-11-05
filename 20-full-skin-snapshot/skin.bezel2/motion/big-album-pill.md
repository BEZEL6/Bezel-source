# Big album pill — big-album-pill

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `big-album-pill` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/big-album-pill.md) · [layout](../layout/big-album-pill.md) · [state](../state/big-album-pill.md) · [motion](../motion/big-album-pill.md) · [art](../art/big-album-pill.md) · [input](../input/big-album-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The **big album pill** is the ALBUM ↔ PREV/NEXT mode control. It looks the same, sits in the same place and works the same on Dialogue FS and on full screen album viz. It is **not** the fan art pill (`6391`, fanart-fs.md).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/big-album-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/big-album-pill.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 1000 ms, 600 ms
