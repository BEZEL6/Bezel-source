# Busy indicator

**Object:** Kodi's "working" indicator · Kodi: `DialogBusy.xml` (`busydialog`), label `10` hidden, include `BezelATBusyOpen` (Tuner delay)
**Where:** over any screen while Kodi works
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
The busy indicator waits a moment before it shows, so quick loads never flash it, and it stays out of the way while music or video plays, while caching and during Bezel's own art changes. Tab pressed while it's up is remembered and opens fullscreen music afterwards.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hidden | work shorter than the delay; audio / video playing; caching; art flip; startup | — | nothing |
| Shown | work longer than the delay | done | busy indicator (no logo, no label) |

### Timeline
| What | Duration | Curve |
|---|---|---|
| show | after the Tuner delay, 300 fade | — |
| hide | 300 fade after 500 delay (not during video) | — |

### Interruptions
Tab / Display while busy → queued fullscreen music.

### Continuity
Never covers playback.

### Layering
Top (DepthMax).

### Geometry
Kodi busy layout.

### Art
Spinner only; no Bezel logo; no text.

### Input
None (Kodi cancel where allowed).

### Speed targets
Short work never shows it.

### Never
No flash on quick loads; no busy over music / video.

### Acceptance checks
Open a large section: indicator only if it takes longer than the delay.

## Kodi implementation (sandbox)

### How it works
- Group visible only when CinemaVision isn't running, not the startup window, `!Player.Caching`, not audio-only playback, `bz_flipping` empty, no video / fullscreenvideo …; Visible fade 300 ms; WindowClose fade 100 → 0 300 ms delay 500 when `!Player.HasVideo`.
- Keymap: busydialog / busydialognocancel tab / display → `bz_tabq=true`; bz_flip opens 1121 when the busy state ends.

### Wiring
| Item | Value |
|---|---|
| Include | `BezelATBusyOpen` (Tuner open delay) |
| Home | `bz_flipping`, `bz_tabq` |

### Kodi workarounds (do not port)
Hiding Kodi's dialog instead of not raising it.

## Related
[keymaps](keymaps.md) · [now-playing](now-playing.md) · [skin-settings-tuner](skin-settings-tuner.md)
