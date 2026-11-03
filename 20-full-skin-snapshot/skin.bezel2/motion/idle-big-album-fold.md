# Idle Big Album fold (book-page leaf) — idle-big-album-fold

**Object:** `idle-big-album-fold` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/idle-big-album-fold.md) · [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

**See screen:** [idle-big-album-fold baselines](../port-refs/idle-big-album-fold/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/idle-big-album-fold.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/idle-big-album-fold.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|

**Timings named in behavior:** 1400 ms

**LOCKED (Rob Nov 1 2026):** ph1 1400 ms sine in/out, ph2 1400 ms sine in/out, hold 10 s, shadows 1400 ms sine synced to `bz_hf_ph`. Not tunable.
