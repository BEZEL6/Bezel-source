# Pause screen (dialog 1116) — pause-overlay

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `pause-overlay` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/pause-overlay.md) · [layout](../layout/pause-overlay.md) · [state](../state/pause-overlay.md) · [motion](../motion/pause-overlay.md) · [art](../art/pause-overlay.md) · [input](../input/pause-overlay.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/pause-overlay.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |

**Semantics from behavior (verbatim lines):**
- Pause a film or episode and the picture dims. The poster slides in on the right, with the title, a subtitle line and "PAUSED · time / duration" plus a thin progress bar. Press Play and it all goes away.
- The condition requires full-screen video, paused, with video, not buffering, and none of the OSDs open. Opening the Video OSD (Select/Menu) or subtitle/audio settings hides the pause screen instantly, so the two never overlap.
- There are no focusable controls, so it never takes keys. Play, Select and Back all go to the player or OSD underneath.
- The dim fades in over about half a second while the poster glides in from the right. Text is right-aligned to the poster's left edge.
- The whole group fades in 0→100 over 600 ms cubic out and fades out over 250 ms. At the same time, the poster group slides from 906 px to the right into place over 600 ms, so the motion and fade finish together. The poster has its own rounded shadow image behind it.
- | Title | top 628, left −540, width 500, right-aligned, `[UPPERCASE]$VAR[BzVOSDTitle]`, font `bz_mm48b` |
- ## Keys / touch
- None of its own (no focusable controls). Play resumes and hides it; Select/Menu opens the Video OSD, which hides it.
