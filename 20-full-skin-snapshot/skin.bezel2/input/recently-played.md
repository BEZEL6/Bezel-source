# Recently played — recently-played

**Object:** `recently-played` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/recently-played.md) · [layout](../layout/recently-played.md) · [state](../state/recently-played.md) · [motion](../motion/recently-played.md) · [art](../art/recently-played.md) · [input](../input/recently-played.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/recently-played.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6100 | `60` | `60` | `` | `` | `` |
| 6500 | `SetProperty(bz_nav,true,home)` | `60` | `` | `` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Opens Music on recently played albums. That path is registered as the nav root, so Back there opens the MM. Draft: not Rob-approved.
- ## Back / Left to MM
- Back at the recently-played list opens the main menu.
- Left opens it whenever the A–Z bar isn't showing.
- Inside an album, Back steps out first.
- Left uses list 60's onleft: A–Z bars 6500/6100 hidden + `bz_navok` → MM.
- Same as music-list.md: Up/Down (Up wrap to the ALL row 6097 when it's visible), Select opens or plays, Left (A–Z hidden + navok) → MM, Back at root (`bz_atroot`) → MM.
- ## Touch
