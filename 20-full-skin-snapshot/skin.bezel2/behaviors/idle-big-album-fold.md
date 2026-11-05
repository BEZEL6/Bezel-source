# Idle big album fold (book-page leaf)

**Object:** idle big album page turn · Kodi: hinge group in `Includes_Bezel.xml` (camera 1440,520, `FOLDLOCK` marker) · `bz_flip.py idle_hinge()` · Home `bz_hf_a` / `bz_hf_b` / `bz_hf_ph` / `bz_hf_g`
**Where:** big album, Music list with nothing playing (and under the MM when Music is the warm screen)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live, **off by default** (Tuner › Album / Poster › Leaf flip) · **Lock:** **LOCKED** (Rob, Nov 1 2026: "Leaf anim 100%. Lock in"). Do not change timing, shadows, frames, glare or geometry unless Rob asks.

## Simple
When the Music list is idle (nothing playing) and Leaf flip is on, the big album turns like a book page every 10 seconds (5 s under the menu). The cover is cut down the middle. Its right half lifts off the spine and swings toward you while the next cover shows underneath; then the next cover's left half lands over the old left half. The page is solid, shadows sell the lift and landing, the white border is sliced and rides with the page, and the glare steps aside for the turn and comes back after.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Off | Tuner Leaf flip off (default); music playing; not on the Music list / warm Music under the MM | — | plain idle album (with its own dissolve) |
| Hold | idle Music cover shown and settled | hold time passes | cover A; next cover B loaded underneath (hidden) |
| Phase 1 (lift) | end of hold | 1400 ms | A's right half turns 0° → +90° about the spine |
| Phase 2 (land) | end of phase 1 | 1400 ms | B's left half turns −90° → 0° over A's left half |
| Dimmed | MM dim / global dim active | dim lifts | single opaque cover, no fold (hold paused) |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| hold | 10 000 (Music list) / 5 000 (under the MM) | — | — |
| ph1 − 500 | glare fades out | 500 | sine |
| ph1 0 | right leaf of A: rotate 0 → +90° (spine x 1440) | 1400 | sine in-out |
| ph1 | leaf darkens 0 → 45 %; right "under" gradient 70 → 0; cast 100 → 0; outer gradient 0 → 60 | 1400 | sine in-out |
| ph2 0 | left leaf of B: rotate −90 → 0° | 1400 | sine in-out |
| ph2 | landing leaf 45 → 0 %; left gradient 0 → 70; spine shadow 0 → 100; outer gradient 60 → 0 | 1400 | sine in-out |
| end | A := B (same pixels, seamless); glare back | 600 | sine |

### Interruptions
- Focus change (new artist / album row): fold aborts within 50 ms and re-arms with the new cover (a one-frame focus hop within 0.3 s is ignored).
- Music starts, MM nav into a submenu, a modal opens: fold stops; props clear.
- Dim lands mid-fold: fold aborts and re-arms when the dim lifts.
- Cold start: for the first 6 s the cover list is re-read once a second; a late list restarts the hold from A.

### Continuity
- The fold has its own clock; it never shares the sway clock and is never triggered by play start.
- Arms only after the idle cover is fully shown and its dissolve is done (no snap over a dissolve).
- End of the fold is pixel-identical to the next cover: no swap flash.

### Layering
Base cover < static half-frames (always on) < B right half (preloaded) < static A left < shadows < leaves (each with its own half-frame) < glare (faded out during the turn).

### Geometry
| Piece | Value |
|---|---|
| Cover | 1140, 220, 600 × 600; halves 300 × 600 meeting at x 1440 (the spine) |
| Rotation | about x 1440; camera 1440, 520 (90° is exactly edge-on) |
| Perspective | free edge swings toward the viewer (grows past top / bottom) |

### Art
- Covers: Artist row: current + that artist's albums by year (wraps); Album row: album ↔ artist thumb. Default (placeholder) art skipped; needs ≥ 2 covers.
- Leaves opaque (no alpha); half-frames `bz_frame_half_l/r`; shadows `hf_shd_grad_l/r`, `hf_shd_grad_r_outer`, `hf_shd_hinge_l`, `hf_shd_cast`.
- Glare: the one 600 × 600 album glare (no half glares since 414).

### Input
None; Tuner on / off.

### Speed targets
1400 ms per phase exactly; no hitch at arm.

### Never
- No sharing of the sway clock; no trigger on play start.
- No snap or hitch on arm (438 LEAFTUNE).
- No ghost glare / shadow-only flip under a dim (313).
- No glare pop (261, 263, 414).

### Acceptance checks
1. Tuner Leaf flip on, nothing playing, Music artist row focused: after 10 s the page turns in two 1.4 s phases; glare steps out and back.
2. Move focus mid-turn: turn stops at once, new cover shows.
3. Open the MM over Music: folds every 5 s.
4. Turn Leaf flip off: plain cover, no folds.

## Kodi implementation (sandbox)

### How it works
- `idle_hinge()` loop: `HOLD = 10.0` (5.0 under the MM). `ok()` = Leaf flip on (`Skin.HasSetting(bz_leafflip)`) and [idle path `!Player.HasAudio + Window.IsActive(music) + Control.HasFocus(60)` with no `bz_nav`] or `mmw()` (`bz_nav`, Music warm under the MM, focus 6996, no `bz_mmwarm`, no `bz_navtune` / `bz_navbez`, no modal, no audio); `bz_randpend` blocks.
- Sets `bz_hf_a` (current), `bz_hf_b` (next, at hold start = preload), `bz_hf_ph` = 1 / 2 with `waitForAbort(1.4)` each, `bz_hf_g` for the glare fade (500 out before ph1, 600 back after).
- Arms only after `bz_m_idle_art` shows the cover and its A/B dissolve is done (438); hinge images `background="true"`; no lock while `Container(60).ListItem.DBID` is empty (355).
- `dim()` mirrors `bz_lfdim` (MM dim or global dim 1–6): pauses the hold; under dim the XML shows a single opaque A stack (313).
- Hinge group visible `!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(bz_hf_a)`.

### Wiring
| Piece | Where |
|---|---|
| Driver | `bz_flip.py idle_hinge()`, `ok()`, `mmw()`, `dim()`, `covers()` |
| Props | `bz_hf_a`, `bz_hf_b`, `bz_hf_ph`, `bz_hf_g`; expression `bz_lfdim` |
| Toggle | `Skin.HasSetting(bz_leafflip)` (default off, 405) |
| Media | `bezel/bz_frame_half_l/r.png`, `hf_shd_grad_l/r.png`, `hf_shd_grad_r_outer.png`, `hf_shd_hinge_l.png`, `hf_shd_cast.png` |
| Restart | XML / media → ReloadSkin; `bz_flip.py` → full Kodi restart |

### Kodi workarounds (do not port)
- Python stepping the phases with `waitForAbort(1.4)`: Kodi has no chained animations; a port runs one 2.8 s timeline.
- Separate half images per cover: Kodi can't clip one image into halves.

## Related
[leaf-flip](leaf-flip.md) · [big-album](big-album.md) · [sway-animations](sway-animations.md) · [music-list](music-list.md)
