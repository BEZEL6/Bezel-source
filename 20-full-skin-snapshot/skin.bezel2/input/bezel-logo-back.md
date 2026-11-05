# BEZEL logo / Back button — bezel-logo-back

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `bezel-logo-back` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/bezel-logo-back.md) · [layout](../layout/bezel-logo-back.md) · [state](../state/bezel-logo-back.md) · [motion](../motion/bezel-logo-back.md) · [art](../art/bezel-logo-back.md) · [input](../input/bezel-logo-back.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The BEZEL logo sits top-left and takes the skin tint. About every 30 seconds it does one spin.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/bezel-logo-back.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6001 | `SetProperty(bz_nav,true,home)` | `60` | `6001` | `60` | `` |

**Semantics from behavior (verbatim lines):**
- # BEZEL logo / Back button
- Where:** Top-left of every BEZEL window, at 28,26 (64×64). Hidden in FullscreenVideo / VideoOSD.
- Simple.** The BEZEL logo sits top-left and takes the skin tint. About every 30 seconds it does one spin.
- Spin: `rotate` 0 → -360, center 60,58, 1100 ms, tween back, easing out, `condition=String.IsEqual(Window(Home).Property(bz_biglogo_spin),true)`.
- ## Tap = Back (touch)
- Simple.** Tapping the logo is the same as pressing Back.
- How it works.** `BezelLogo` carries an unnamed button over the logo area that runs `Action(Back)`. It has the same visibility rule as the logo, so it does nothing in fullscreen video.
- Wiring.** Button at 0,0, 120×116, `onclick Action(Back)` (5.33.117 t816).
- Simple.** On some screens you can move focus onto the logo and press Select. That steps back one level in the order that fits the screen.
- 2. Else a video back layer (`bz_vback`) → raise `bz_vback_close`.
- 3. Else a back layer (`bz_back`) → raise `bz_back_close`.
- 5. Else `Action(Back)`.
