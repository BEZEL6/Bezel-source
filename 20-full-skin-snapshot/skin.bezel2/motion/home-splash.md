# Home / startup splash — home-splash

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `home-splash` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/home-splash.md) · [layout](../layout/home-splash.md) · [state](../state/home-splash.md) · [motion](../motion/home-splash.md) · [art](../art/home-splash.md) · [input](../input/home-splash.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

**See screen:** [home-splash baselines](../port-refs/home-splash/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/home-splash.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/home-splash.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 50 ms
