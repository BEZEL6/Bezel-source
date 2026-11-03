# Touch / tap inputs — touch-group

**Object:** `touch-group` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/touch-group.md) · [layout](../layout/touch-group.md) · [state](../state/touch-group.md) · [motion](../motion/touch-group.md) · [art](../art/touch-group.md) · [input](../input/touch-group.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/touch-group.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6001 | `SetProperty(bz_nav,true,home)` | `60` | `6001` | `60` | `` |
| 6886 | `60` | `60` | `60` | `60` | `60` |

**Semantics from behavior (verbatim lines):**
- # Touch / tap inputs
- Object:** Cross-object. The logo-back button (`Includes_Bezel.xml`), the tap targets in `Includes_Bezel.xml` / `Custom_1120_PlayNext.xml`, and the double-tap service `scripts/bz_dtap.py`, plus the Tuner rows `dtap` / `dtapwin`
- Where:** Global (logo), music strip, Fanart FS, Play Next 1120, every section window (double-tap)
- Status:** Live in 5.33.207. Touch only does what each object's doc specifies. Double-tap Select is a Tuner option. There is **no touch master toggle** in the live tree. Draft: not Rob-approved.
- Touch only does what Rob specified per object. Each object's file lists its own touch actions.
- ## Logo = Back
- Tap the BEZEL logo in the top-left corner to go back. This works everywhere except fullscreen video and the video OSD.
- It has no ID, so remote focus never lands on it. Only a mouse or touch can hit it.
- Where `BezelLogoButton` 6001 exists, that button sits above it and handles the tap itself.
- | onclick | `Action(Back)` (see bezel-logo-back.md) |
- ## Tap targets
- These are ordinary focusable controls, so a tap does the same thing as pressing Select on them.
