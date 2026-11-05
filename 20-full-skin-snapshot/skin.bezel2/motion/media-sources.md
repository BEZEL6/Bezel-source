# Media sources — media-sources

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `media-sources` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/media-sources.md) · [layout](../layout/media-sources.md) · [state](../state/media-sources.md) · [motion](../motion/media-sources.md) · [art](../art/media-sources.md) · [input](../input/media-sources.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/media-sources.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/media-sources.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 200 ms, 200ms, 300ms
