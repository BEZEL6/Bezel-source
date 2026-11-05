# Touch and double-tap

**Object:** cross-object touch rules and double-tap Select · Kodi: logo touch button (`BezelLogo`), per-object touch buttons, `scripts/bz_dtap.py`, Tuner `dtap` / `dtapwin`
**Where:** global
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Touch only does what each object's file says. Globally: tapping the Bezel logo is Back. Remote "double-tap": one Select acts after a short pause, two quick Selects open Options / Info. Both the on / off and the pause length are Tuner settings. There is no touch master switch.

## Feel contract (any framework)

### States
| State | On screen |
|---|---|
| Double-tap on (default) | single Select delayed by the tap window |
| Double-tap off | Select acts at once; no double action |

### Timeline
Tap window 150–600 ms (default 300 ms; 15 steps); a single tap more than 0.6 s late is dropped.

### Interruptions
Focus moved or navigation locked during the window → the single tap is dropped.

### Continuity
Only in screens (never in dialogs, the keyboard, the OSD or fullscreen video).

### Layering
Touch targets sit over the object they control; remote focus never lands on touch-only targets.

### Geometry
Logo touch area 0, 0, 120 × 116. Fullscreen music, Dialogue FS and Play Next touch areas: see those files.

### Art
None (invisible targets).

### Input
| Touch / key | Result |
|---|---|
| Tap logo | Back |
| Tap a focusable control | same as Select on it |
| Fullscreen music | album double-tap → album view; tap → play / pause; right half → Up Next; logo → close; side albums → previous / next |
| Dialogue FS | side albums → play them |
| Select × 2 in the window | Options / Info |

### Speed targets
—

### Never
No touch master toggle (it never existed in the live tree).

### Acceptance checks
Tap the logo → Back; double-Select a list row → Options / Info; Tuner double-tap off → Select is instant.

## Kodi implementation (sandbox)

### How it works
- Touch-only buttons have no id (or forward focus to the main control) so remote focus never lands.
- Double-tap: see [keymaps](keymaps.md) (`bz_dtap.py`, `STEPS` 150 … 600, `bz_at_dtapwin`, off = `Skin.HasSetting(bz_dtap_off)`).

### Wiring
| Item | Value |
|---|---|
| Tuner | `dtap` (`bz_dtap_off`), `dtapwin` (`bz_at_dtapwin`) |
| Script | `scripts/bz_dtap.py` |

### Kodi workarounds (do not port)
The replayed Select and focus-forwarding buttons.

## Related
[keymaps](keymaps.md) · [bezel-logo-back](bezel-logo-back.md) · [music-fanart-fs](music-fanart-fs.md) · [dialogue-fs](dialogue-fs.md) · [context-menu](context-menu.md)
