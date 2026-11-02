# Idle Big Album fold (book-page leaf) — idle-big-album-fold

**Object:** `idle-big-album-fold` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/idle-big-album-fold.md) · [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [idle-big-album-fold baselines](../port-refs/idle-big-album-fold/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/idle-big-album-fold.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/idle-big-album-fold.md).

## Hand-verified geometry (Includes_Bezel.xml ~L1096–1121, hinge group has no id)
**Simple:** a 600×600 square cut into two 300×600 halves at x1440; the camera sits on the slit so the page is edge-on at 90°.

| piece | x | y | w | h | notes |
|---|---|---|---|---|---|
| Big album (base, outside hinge) | 1140 | 220 | 600 | 600 | `art_mask.png` diffuse, fadetime 300, zoom 150↔100 centre 1440,420 |
| Hinge group | — | — | — | — | `<camera x="1440" y="520"/>`; visible `!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(bz_hf_a)` |
| A-left static | 1140 | 220 | 300 | 600 | aspectratio scale align left, `bz_hf_a` |
| B-right next (preloaded) | 1440 | 220 | 300 | 600 | align right, `bz_hf_b` |
| Half frame L | 1139 | 219 | 301 | 602 | `bz_frame_half_l.png` border 8 |
| Half frame R | 1440 | 219 | 301 | 602 | `bz_frame_half_r.png` |
| Static half glare L | 1140 | 220 | 300 | 600 | `art_mask_hl.png`, flipx, `$VAR[BzATGlare8C]` |
| ph1 leaf (A right) | 1440 | 220 | 300 | 600 | group hidden when ph=2; rotatey 0→90 centre 1440 |
| ph2 leaf (B left) | 1140 | 220 | 300 | 600 | group visible ph=2; rotatey −90→0 centre 1440 |

Z-order (bottom→top): A-left · B-right · half frames · static glares · shadows · ph1 leaf (+frame_r, glare) · ph2 leaf (+frame_l, glare). Outside music/hinge: glare group L1121.
**Port:** one 600×600 view, two half-image layers, a 3D Y-rotation anchored at the slit (SwiftUI `rotation3DEffect(axis:(0,1,0), anchor:.leading/.trailing)` with perspective ≈ camera distance on slit).
Baseline: `port-refs/idle-big-album-fold/` (259 mid-fold, pre-lock — recapture on 267 for an approved baseline).
