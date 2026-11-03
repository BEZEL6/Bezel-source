# Fullscreen pill (Music list) — fullscreen-pill

**Object:** `fullscreen-pill` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-pill.md) · [layout](../layout/fullscreen-pill.md) · [state](../state/fullscreen-pill.md) · [motion](../motion/fullscreen-pill.md) · [art](../art/fullscreen-pill.md) · [input](../input/fullscreen-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/fullscreen-pill.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6886 | `60` | `60` | `60` | `60` | `60` |

**Semantics from behavior (verbatim lines):**
- Object:** button `6886` inside `BezelFSLeftStage` (Includes_Bezel), in a horizontal grouplist at 786,136 (158×32, aligned right)
- Where:** Music section list, over the left fanart stage, while audio plays
- Simple.** A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).
- How it works.** The pill is inside the fanart left stage, so it rides the stage slide in and out and never pops on its own. Its group hides in every case where it would be wrong or on top of something: in viz, fullscreen video, Dialogue FS, 1112, while the Play Next return latch runs, with the MM open, or outside artists/albums/songs. It was hard-hidden in 5.33.154/.155 and restored under BUG-018 (.169/.173).
- Simple.** Select opens full screen. Any direction or Back returns to the list.
