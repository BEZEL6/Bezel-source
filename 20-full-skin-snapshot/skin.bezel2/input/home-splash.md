# Home / startup splash — home-splash

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `home-splash` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/home-splash.md) · [layout](../layout/home-splash.md) · [state](../state/home-splash.md) · [motion](../motion/home-splash.md) · [art](../art/home-splash.md) · [input](../input/home-splash.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [home-splash baselines](../port-refs/home-splash/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/home-splash.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|

**Semantics from behavior (verbatim lines):**
- How it works.** The menu is armed **before** Music opens. On Shield the music window can take more than 3 s, and before 4.7.11 `bz_nav` was never set under the splash. Music opens at `musicdb://` and then updates to Artists, so Back steps up one level instead of to the sources root. After the splash it re-asserts `bz_nav`, in case something closed the menu early under the splash (4.7.8+). After a further 6 s it clears `bz_startfade`.
- `ActivateWindow(Music,musicdb://)` → wait up to 60×50 ms → `Container.Update(musicdb://artists/)` (t5011).
