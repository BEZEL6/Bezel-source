# MM auto-hide and pill idle return

**Object:** (1) MM auto-hide · (2) pill idle return · Kodi: `bz_flip.py mm_autohide` (+ `_pill_idle`), `$EXP[bz_mmhid]`, Home `bz_mmhide` / `bz_mmwake`, Tuner Main menu › Auto-hide menu (`bz_at_mmhide`)
**Where:** (1) the MM over any section · (2) every pill and the A–Z bar
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
**Auto-hide.** If you leave the main menu open and don't touch anything for the chosen time (Off by default; 30 s, 1, 2 or 5 min), the menu, colour strip and backdrop fade away and only the art keeps playing, like a screensaver: the poster and the fanart (with the item's clear logo or title on the stage) and PRESS ANY BUTTON next to the Bezel logo. Any key brings the menu back on the row you left; that first key only wakes it.
**Pill idle.** If focus sits on a pill (FULLSCREEN, the cycle pill, the big album pill, an MM header pill, an A–Z letter) for 5 seconds without input, focus goes back to where it came from.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| MM shown | — | idle ≥ setting | menu |
| Hidden | idle ≥ setting, strip focused, nothing else open | any key | art only, undimmed fanart + logo / title, PRESS ANY BUTTON |
| Waking | first key | 350 ms | menu fades back; the key does nothing else |
| Pill focused | focus on a pill | 5 s idle → return; any key | pill |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| idle ≥ setting | menu, strip, backdrop fade out; undimmed fanart fades in | 1500 | sine |
| key | menu fades back; fanart overlay out | 250 | sine |
| pill idle 5000 | focus jumps back (no animation) | — | — |

### Interruptions
- Up / Down as the waking key: if it moved the strip, the move is undone.
- Playback starts / a dialog opens while hidden: wakes.
- Pill idle fires once per idle period.

### Continuity
Focus stays on the strip the whole time (no focus parking). Art never stops.

### Layering
Hidden: section art (dimmed as usual) < undimmed fanart copy over the stage < logo / title < PRESS ANY BUTTON.

### Geometry
| Piece | Value |
|---|---|
| PRESS ANY BUTTON | 108, 36 / 108, 58 (right of the logo) |
| Clear logo | 150, 660, 640 × 250, bottom-left kept |
| Title | 150, 920 (46 px alone; 24 px under a logo) |
| Fanart copy | 120, 120, 840 × 900 |

### Art
Clear logo (show / artist / clear art) of the art on screen, else its title.

### Input
Any key wakes (and only wakes). Pills: 5 s idle returns.

### Speed targets
Wake within 250 ms.

### Never
- No old park-button auto-hide (398: removed as "glitchy and broken"; this is the fresh 428 system).
- No Music labels showing through Movies fanart while hidden (444 MMHIDEFAN).
- Only the poster and fanart stay when hidden (444 "just poster and fanart").

### Acceptance checks
1. Tuner auto-hide 30 s; MM open on MOVIES, wait → menu fades, poster + fanart + logo, PRESS ANY BUTTON.
2. Press Down → menu back on MOVIES (not moved).
3. Focus FULLSCREEN pill, wait 5 s → focus back on the list.

## Kodi implementation (sandbox)

### How it works
- **Auto-hide:** `mm_autohide` (20 Hz) reads `xbmc.getGlobalIdleTime()`; `secs = _MMH_S[bz_at_mmhide]` (0 Off, 1 30 s, 2 1 min, 3 2 min, 4 5 min). Hides only with the setting on, `bz_nav=true`, strip focused, splash done, no Tuner / settings card / submenu / kset / mmstart / pick / secload, no modal, no fullscreen video. Sets `bz_mmhide`; opacity-only Conditional fade pairs (1500 out / 250 back, `reversible=false`) on group 6894, the MM veil and `BezelGlobalBackdrop`. Wake: idle drops → `bz_mmwake` latch 0.35 s; 6996 Select / Left / Right / Back carry `String.IsEmpty(bz_mmhide)`; a moving Up / Down is undone with `SetFocus(6996,<row>,absolute)`. mm_warm doesn't warm while hidden.
- **Stage:** `$EXP[bz_mmhid]` group: `BezelFanartLayer` (black backing + MM lanes, not under SecDim), fade in 1500 / out 250. Poster layer 6401 uses `BezelSecDimArt` (no mmdim while hidden). `bz_mmh_logo` / `bz_mmh_title` refresh every 50 ms (virtual row `bz_vart_logo` / `bz_vart_title`, else list 60 clearlogo / tvshow.clearlogo / artist.clearlogo / clearart, Label / TVShowTitle), written through `_v60_set`.
- **Pill idle:** every 5th tick (4 Hz) `_pill_idle(idle)`: `System.CurrentControlId` + window / dialog id. `_PILL_HOME`: 6886 → 60, 6391 → 6390, 6421 → 6420, 6401 → (FS main), 6958–6961 / 6910 → 6996 (only while `bz_nav` and no `bz_navsub`), 6101–6127 → 60. Off a pill the last control + window are remembered; on a pill idle ≥ 5 s → `SetFocus` remembered (same window) or the pill's home. ≈ 8 Kodi calls / s.

### Wiring
| Item | Value |
|---|---|
| Tuner | `bz_at_mmhide` (`BzATVal_mmhide`, `BzATBar_mmhide`) |
| Home | `bz_mmhide`, `bz_mmwake`, `bz_mmh_logo`, `bz_mmh_title` |
| Expression | `bz_mmhid` |
| Includes | `BezelFanartLayer`, `BezelSecDimArt`, `BezelGlobalBackdrop` |

### Kodi workarounds (do not port)
- The wake latch and undo-move: Kodi delivers the waking key to the focused control.
- The undimmed fanart copy: Kodi dims whole groups, so the art is redrawn on top.

## Related
[mm-list](mm-list.md) · [mm-warm](mm-warm.md) · [fullscreen-pill](fullscreen-pill.md) · [skin-settings-tuner](skin-settings-tuner.md)
