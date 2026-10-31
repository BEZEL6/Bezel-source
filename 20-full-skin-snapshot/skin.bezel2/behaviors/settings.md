# Kodi Settings

**Object:** `Settings.xml` · list `9000`; sub windows handled by `bz_dtap.py` noctx keymap (`bz_setback`)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Kodi Settings home, opened from MM SETTINGS (Select only; no Left/Right on the MM row).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move (wrap within 9000) |
| Left | noop |
| Right | stays 9000 |
| Select | Open category window |
| Back (Settings home) | `bz_nav=true` now + 1 s re-arm alarm `bz_setmm` → MM restored on the opener row (Videos and Music) |
| Back in a sub-settings list | noctx keymap → `NotifyAll(bz,bz_setback)`; bz_dtap returns to the parent category list (system/service/pvr/player/media/interface/game settings) |

## Transitions
Fade-in only, 400 ms sine at every Settings level (5.33.177; section-transitions.md).

## Related
mm-list.md · section-transitions.md · keymaps.md · media-sources.md
