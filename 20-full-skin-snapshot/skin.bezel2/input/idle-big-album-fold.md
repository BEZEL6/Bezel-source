# Idle Big Album fold (book-page leaf) — idle-big-album-fold

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `idle-big-album-fold` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/idle-big-album-fold.md) · [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [idle-big-album-fold baselines](../port-refs/idle-big-album-fold/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/idle-big-album-fold.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 60 (music list — the fold has no focusable control) | any nav key stops the fold (`bz_nav`/back gate in `ok()`) | ″ | ″ | ″ | ″ — hand-verified from bz_flip.py `idle_hinge()` |

**Semantics from behavior (verbatim lines):**
- When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.
- Book page, left 1 | right 2.** Each cover is two 300×600 half images meeting invisibly at the slit x1440 (group 1140,220 600×600). Layers: A-left static (1140), B-right next cover (1440), preloaded under the page during the hold.
- ph1 (lift → centre):** A-right leaf rotatey 0→+90.
- ph2 (centre → land):** B-left leaf rotatey −90→0 lands over A-left. The back of the page is the next cover's front.
- Opaque leaf.** The leaf images have no alpha or colordiffuse. Global dim (`bz_at_gdim`) doesn't touch the big album.
- Static left: `hf_shd_grad_l` (darkest at slit) stays at 0 through ph1, then 0→70 in ph2. `hf_shd_hinge_l` stays at 0 in ph1, then 0→100 in ph2.
- Under/next right: `hf_shd_grad_r` 70→0 in ph1 and 0 in ph2. `hf_shd_cast` 100→0 in ph1 and 0 in ph2. `hf_shd_grad_r_outer` (darkest at slit → light outer) 0→60 in ph1, 60→0 in ph2.
- Frames.** The full `bz_frame_soft` is hidden while the hinge stack shows. The static half-frames `bz_frame_half_l/r` are always on, so the back cover keeps its border with no pop. Each leaf carries its own half-frame that rides the rotatey (ph1: `_r`, ph2: `_l`).
- | Loop | `bz_flip.py` `idle_hinge()`: `HOLD=10.0`; `ok()` = `!Player.HasAudio + Window.IsActive(music) + Control.HasFocus(60)` and no nav/randpend/back |
