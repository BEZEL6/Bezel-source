# Skin settings / BEZEL Tuner — skin-settings-tuner

**Object:** `skin-settings-tuner` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/skin-settings-tuner.md) · [layout](../layout/skin-settings-tuner.md) · [state](../state/skin-settings-tuner.md) · [motion](../motion/skin-settings-tuner.md) · [art](../art/skin-settings-tuner.md) · [input](../input/skin-settings-tuner.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [skin-settings-tuner baselines](../port-refs/skin-settings-tuner/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/skin-settings-tuner.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 140 | `` | `` | `120` | `160` | `` |
| 150 | `` | `` | `130` | `170` | `` |
| 6968 | `noop` | `noop` | `` | `` | `ClearProperty(bz_navbez,home)` |
| 6970 | `SetProperty(bz_tune_dirty,1,home)` | `SetProperty(bz_tune_dirty,1,home)` | `noop` | `noop` | `ClearProperty(bz_navtune,home)` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |

**Semantics from behavior (verbatim lines):**
- Object:** `Includes_Tuner.xml`: group `6975`, Tuner list `6970` (left 570), BEZEL settings list `6968` · `SkinSettings.xml` · `scripts/bz_tune.py` + `bz_tune.json` · `scripts/bz_dtap.py` (`bz_tune_dirty` reload)
- Status:** Live in 5.33.207. Left/Right change a row's value straight away. Changes that need a skin reload are batched 1.2 s after the last change. Back returns to whoever opened the Tuner. There's **no touch master row** in the live tree. Draft: not Rob-approved.
- The Tuner is BEZEL's own settings list, drawn on the main menu's dark side. Open it from Power › TUNER (or from the music controls or BEZEL settings). Back takes you back to wherever you came from.
- Back reads `bz_tunesrc` and returns to that opener:
- Opened from the BEZEL settings list (`bz_navbez`) → back to list 6968.
- Back always clears `bz_navtune` and `bz_tunesrc`, so the group hides immediately (BUG-007).
- | List 6970 | left 570 · onup/ondown noop (native list move) |
- | List 6968 | BEZEL settings list, left 570 / top 140 / 390×870 |
- Highlight a row and press Left or Right to step its value. A bar and the value text show where you are.
- XML step chains.** 6970's onleft/onright carry generated per-row conditional `Skin.SetString` chains, so a step needs no Python start-up. Each step also sets `bz_tune_dirty`.
- Loop tidy-up.** The same loop clears a stale `bz_navtune` whenever `bz_nav` isn't true (every 5 ticks).
- ## Touch-related rows
