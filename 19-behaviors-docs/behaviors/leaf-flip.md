# Leaf flip (family index)

**Object:** the book-page leaf animation family · Kodi: hinge group (camera 1440,520, `FOLDLOCK`) · `bz_flip.py idle_hinge()` · Home `bz_hf_a` / `bz_hf_b` / `bz_hf_ph` / `bz_hf_g`
**Where:** big album
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** idle use live (off by default), other uses not shipped · **Lock:** **LOCKED** (look and timing = [idle-big-album-fold](idle-big-album-fold.md))

## Simple
"Leaf flip" is the page-turn animation: the cover is cut at the spine and its right half turns like a book page to show the next cover. It has its own clock and its own state. It is not the sway and not the whole-cover flip. Anywhere Bezel wants a page turn uses this; today only the idle big album does.

## Feel contract (any framework)
The full contract (states, timeline, shadows, geometry, checks) is in [idle-big-album-fold](idle-big-album-fold.md). Family rules:

### States
| Use | Status |
|---|---|
| Idle big album (Music list, nothing playing) | live, off by default (Tuner) |
| While playing, next song | **not a leaf**: album changes while playing use the sway-tree next-song fade (900 ms) |
| Fullscreen side albums | planned, not shipped |
### Timeline
Two phases of 1400 ms, sine in-out, pivot at the spine (x 1440). Hold 10 s (5 s under the MM).
### Interruptions
Focus change aborts within 50 ms.
### Continuity
Own clock: never the sway clock, never triggered by play start.
### Layering
See the fold file.
### Geometry
Spine x 1440 on the 600 × 600 album at 1140, 220.
### Art
Half covers, half frames, fold shadows (fold file).
### Input
None; Tuner toggle.
### Speed targets
Exactly 1400 ms per phase.
### Never
- Never share the sway clock or the whole-cover flip (0 → 90 / −90 → 0, ≈ 1857 ms, kept only for the music → video path).
- No tap-to-flip track list (deleted 309: "we don't use it anymore").
### Acceptance checks
See the fold file.

## Kodi implementation (sandbox)

### How it works
Python drives `bz_hf_ph` = 1 / 2 with `waitForAbort(1.4)`; XML hinge group (visible `!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(bz_hf_a)`) runs the rotations. Gate `Skin.HasSetting(bz_leafflip)`.

### Wiring
| Piece | Where |
|---|---|
| Owned props | `bz_hf_a`, `bz_hf_b`, `bz_hf_ph`, `bz_hf_g` |
| Not owned | `bz_cov_side` (whole-cover flip), `bz_sway*` / `bz_big_*` (sway) |
| Driver | `bz_flip.py idle_hinge()`; future uses get their own entry point with the same props and timing |

### Kodi workarounds (do not port)
Phase stepping from Python (see the fold file).

## Related
[idle-big-album-fold](idle-big-album-fold.md) · [sway-animations](sway-animations.md) · [big-album](big-album.md)
