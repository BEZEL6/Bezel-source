# Bezel logo (Back)

**Object:** the Bezel logo top left · Kodi: include `BezelLogo` (image + touch button), include `BezelLogoButton` (focusable `6001`), spin clock in `bz_flip.py`
**Where:** top left of every Bezel screen (hidden in fullscreen video and the video OSD)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
The Bezel logo sits top left in the skin tint and does one spin about every 30 seconds. Tapping it is Back. On some screens you can also move focus onto it and press Select to step back one level.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Resting | — | spin clock | logo |
| Spinning | every 30 s | 1.1 s | one full turn |
| Focused (some screens) | Left / Up to it | Right / Down | focus version of the logo |
| Hidden | fullscreen video / video OSD; MM open (focusable copy); info up (fades) | — | — |

### Timeline
| What | Duration | Curve |
|---|---|---|
| spin 0 → −360° about the logo centre | 1100, every 30 000 | back out |

### Interruptions
Spin never overlaps (cleared after 1.2 s; retried 2 s later if busy).

### Continuity
Same spot and tint on every screen.

### Layering
Over the screen's chrome.

### Geometry
Logo 64 × 64 at 28, 26 (centre 60, 58). Touch area 0, 0, 120 × 116. Other top-row chrome (e.g. the album pill) is centred on y 58.

### Art
`logo.png`, coloured by the skin tint.

### Input
| Action | Result |
|---|---|
| Tap logo | Back |
| Select on focused logo | first of: close fullscreen / Now Playing → close a video back layer → focus the list → Back |
| Left on focused logo | open the MM |

### Speed targets
—

### Never
No track-list flip from the logo (deleted 309).

### Acceptance checks
Tap the logo in a section → Back; wait 30 s → one spin.

## Kodi implementation (sandbox)

### How it works
- `BezelLogo`: image `bezel/logo.png` 28,26 64 × 64, `colordiffuse=$PARAM[col]` (normally `BzLogoCol`); rotate 0 → −360, centre 60,58, 1100 ms, tween back, easing out, Conditional on `bz_biglogo_spin`. Unnamed button 0,0 120 × 116 `onclick Action(Back)` (no id → remote never lands). Visible unless FullscreenVideo / VideoOSD.
- `bz_flip.py`: sets `bz_biglogo_spin=true` every 30 s, clears after 1.2 s.
- `BezelLogoButton` 6001: visible `!$EXP[bz_navmenu]` (not fullscreen video / OSD), fades while `bz_infoup`; onclick in order: `bz_np` → close; `bz_vback` → `bz_vback_close`; else focus 60 (or 9000); else `Action(Back)`; onright / ondown → 60; onleft (`$EXP[bz_navok]`) → `bz_nav=true`; onup → 6001.
- Used in 1121, Kodi FS, 1119, info dialogs, settings windows, EventLog, FileManager and the section windows.

### Wiring
| Item | Value |
|---|---|
| Includes | `BezelLogo` (param `col`), `BezelLogoButton` |
| Home | `bz_biglogo_spin`, `bz_np`, `bz_vback`, `bz_vback_close`, `bz_infoup` |

### Kodi workarounds (do not port)
The unnamed touch button and the close-latches (`bz_vback_close`): Kodi lets the owning layer run its own exit.

## Related
[touch-group](touch-group.md) · [mm-list](mm-list.md) · [big-album-pill](big-album-pill.md)
