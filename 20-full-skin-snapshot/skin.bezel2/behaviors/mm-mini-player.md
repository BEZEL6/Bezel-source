# MM mini player

**Object:** the small player above the MM rows · Kodi: audio row `6957` Prev · `6958` Play / Pause · `6959` Next · `6961` Stop · `6960` FULL; video group `6966` Play / Pause · `6967` Stop (Includes_Bezel)
**Where:** top band of the MM strip while something plays (the rows move down 120 px)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
While something plays, a compact player sits at the top of the main menu. Music: previous, play / pause, next, stop and FULL (fullscreen). Video: the poster, title, year · time / duration, play / pause and stop. Up from MUSIC reaches it, Down goes back to the rows. The transport buttons keep the menu open; FULL closes the menu and goes fullscreen. When you skip a track the player doesn't blink away.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hidden | nothing playing | playback starts | rows at their normal top |
| Audio row | audio playing | stop | 5 icon buttons; rows 120 px lower |
| Video group | video playing | stop | poster + title + time; 2 buttons |
| Focused | Up from MUSIC | Down / Back | 24 × 3 white underline (audio) or a rounded pill (video) |

### Timeline
| What | Duration | Curve |
|---|---|---|
| video group fade-in | 200 | sine |
| video focus pill | 150 fade | sine |
| skip track | player stays (1.5 s media hold) | — |

### Interruptions
Track change: the brief "no media" gap between tracks never hides the player or moves the rows (1.5 s hold).

### Continuity
Transport keys never close the menu (423 MMINISTAY).

### Layering
Over the strip chrome, above the rows.

### Geometry
| Piece | Value (in the strip) |
|---|---|
| Audio buttons | top 80, 44 × 46: Prev 124 · Play 166 · Next 208 · Stop 250 (42 px pitch); FULL 302, 76 wide |
| Icons | 28 × 28; focus underline 24 × 3 |
| Divider | 350 × 2 at top 140, 40 % white |
| Video poster / title | poster 80 × 120 at 20, 12; title at 116, 12 (22 px bold); line 2 (17 px, 67 % white) |

### Art
No button backgrounds; white icons; video poster = playing item's poster.

### Input
| Action | Result |
|---|---|
| Left / Right | move between buttons |
| Select | the button's action |
| Down | rows |
| Up | nothing |
| Back | close the menu → list |
| 5 s idle on a button | focus back to where it came from |

### Speed targets
Transport acts at once.

### Never
- No closing the MM on transport (423).
- No player blink on Next (435 MPKEEP).

### Acceptance checks
1. Play music, open the MM → player shown, rows lower; Up from MUSIC → Play / Pause.
2. Next → track changes, menu stays, player doesn't blink.
3. FULL → fullscreen music; Back → MM.

## Kodi implementation (sandbox)

### How it works
- List 6996 slides 0,120 (time 0) on `$EXP[bz_mpup]` (media + 1.5 s hold, 435 MPKEEP). 6996 onup: video → 6966; `bz_mpup` → 6958.
- 6957–6959, 6961, 6966, 6967: `PlayerControl(…)` (+ `Dialog.Close(1120)` if open).
- 6960 FULL: clear `bz_nav` / `bz_navtune` / `bz_navbez`; video → `ActivateWindow(fullscreenvideo)`; else `$EXP[bz_m1121ok]` → `ActivateWindow(1121)`, else `ActivateWindow(visualisation)`.
- WARM: while audio plays under the MM the poster lane hides (`bz_mmmushide`, see mm-warm).
- Pill idle covers 6958–6961 / 6910 (only while `bz_nav` and no `bz_navsub`).

### Wiring
| Key | Action |
|---|---|
| Up | noop |
| Down | 6996 |
| Back | clear nav props → 60 |
| Video focus | `mm_round.png` (border 20), text F0 white / focused `FF23160E` |

### Kodi workarounds (do not port)
The 1.5 s `bz_mpup` hold: Kodi reports no media for a moment between tracks.

## Related
[mm-list](mm-list.md) · [np-bar](np-bar.md) · [mm-warm](mm-warm.md) · [music-fanart-fs](music-fanart-fs.md)
