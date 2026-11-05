# Motion tokens

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, generated from live tree · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Bezel moves almost everything with **sine in/out**. A few numbers carry the feel: section **fade-in 400 ms** (no fade-out), MM warm A/B swap **1500 ms**, idle album fold **1400 ms per phase + 10 s hold (LOCKED)**, art zoom **1200 ms**. Copy these exact values and curves into the native animation system.

## Deep (rebuild detail)
### Named tokens (from behaviors + live code)
| token | value | where | lock |
|---|---|---|---|
| section.fadeIn | 400 ms sine in/out; fade-out OFF | [section-transitions](section-transitions.md) | Rob style (Oct 30) |
| warm.abSwap | 1500 ms fixed A/B crossfade | [mm-warm](mm-warm.md) | LOCKED (WARM 2.0) |
| fold.phase1 / phase2 | 1400 ms sine in/out each; rotatey 0→+90 then −90→0, centre x1440 | [idle-big-album-fold](idle-big-album-fold.md) | **LOCKED** |
| fold.hold | 10 s (`HOLD=10.0` bz_flip.py) | idem | **LOCKED** |
| bigAlbum.zoom | 1200 ms sine inout, 150↔100 %, centre 1440,420; stop waits 500 ms delay | Includes_Bezel.xml ~L1090 | tunable |
| art.fadetime | 300 ms (big album image fadetime) | Includes_Bezel.xml | tunable |
| miniPlayer.latch | ≥ 2.5 s (K22) | [mm-mini-player](mm-mini-player.md) | rule |
| fsSlide | `bz_at_fsslide` 480/380/280/180 ms | [dialogue-fs](dialogue-fs.md) | Tuner |

### Easing usage across all XML
| tween | count |
|---|---|
| sine | 3990 |
| quadratic | 390 |
| cubic | 107 |
| back | 37 |
| linear | 30 |
| elastic | 24 |
| circle | 22 |

### Most-used time+tween pairs
| ms | tween | count |
|---|---|---|
| 300 | sine | 93 |
| 250 | sine | 63 |
| 150 | sine | 60 |
| 600 | sine | 39 |
| 400 | sine | 36 |
| 200 | sine | 35 |
| 1500 | sine | 32 |
| 3250 | sine | 28 |
| 1200 | sine | 20 |
| 1000 | sine | 16 |
| 500 | sine | 16 |
| 8500 | sine | 14 |
| 1400 | sine | 12 |
| 480 | sine | 8 |
| 190 | linear | 8 |
| 280 | sine | 7 |
| 5000 | sine | 7 |
| 380 | sine | 6 |
| 180 | sine | 6 |
| 800 | sine | 6 |
| 1250 | sine | 6 |
| 120 | sine | 6 |
| 350 | sine | 4 |
| 300 | cubic | 3 |
| 450 | sine | 3 |
| 400 | cubic | 3 |
| 600 | cubic | 2 |
| 2500 | sine | 2 |
| 1800 | sine | 2 |
| 550 | sine | 2 |

Notes: `time="0"` = instant conditional set; 30000–600000 ms values are slow ambient loops (dust drift / sway clocks), see [dust](dust.md) and [sway-animations](sway-animations.md).
