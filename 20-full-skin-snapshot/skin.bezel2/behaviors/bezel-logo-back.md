# Bezel logo = Back

**Object:** `Includes_Bezel.xml` unnamed button 120×116 at 0,0 (5.33.117 t816); `BezelLogoButton` `6001` above it where present  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Global touch/mouse target over the top-left Bezel logo. Tap → `Action(Back)`. It has no id, so it can't take remote focus. Hidden in `FullscreenVideo` and `VideoOSD`.

## Keys
| Input | Behavior |
|---|---|
| Tap / click logo | Back (same as remote Back in that window) |
| Remote | Not focusable (no id); 6001 handles focus where a section has it |

## Related visuals
- Big Logo spin (t4908): Conditional rotate −360°, centre 60,58, 1100 ms when Home `bz_biglogo_spin=true`. `bz_flip` pulses it every 30 s.
- In Dialogue FS / Play Next the logo also acts as Back (dialogue-fs.md).

## Related
dialogue-fs.md · play-next.md · touch-group.md
