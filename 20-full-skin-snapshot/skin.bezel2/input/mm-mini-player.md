# MM mini-player — mm-mini-player

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-mini-player` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-mini-player.md) · [layout](../layout/mm-mini-player.md) · [state](../state/mm-mini-player.md) · [motion](../motion/mm-mini-player.md) · [art](../art/mm-mini-player.md) · [input](../input/mm-mini-player.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-mini-player.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 120 | `` | `` | `100` | `140` | `` |
| 128 | `` | `` | `108` | `148` | `` |
| 6910 | `noop` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6957 | `noop` | `6958` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6958 | `6957` | `6959` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6959 | `6958` | `6960` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6960 | `6959` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6966 | `noop` | `6967` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6967 | `6966` | `noop` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |

**Semantics from behavior (verbatim lines):**
- Where:** Above the MM strip (the strip slides down 120 when `Player.HasMedia`)
- Simple.** While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.
- | id | left | Icon | onclick | left / right |
- 6957–6959 extra clicks: 1120 active → `Dialog.Close(1120)`. Otherwise `ClearProperty(bz_np,home)` + `Action(Back)`.
- | id | Pos | Label | onclick | left / right |
- | 6966 | 112,78 122×44 | `$VAR[BzOSDPlayLbl]` | `PlayerControl(Play)` + the same 1120 / `bz_np` + Back clicks | noop / 6967 |
- | Up | noop |
- | Down | 6996 |
- | Back | clear `bz_nav` / `bz_navtune` / `bz_navbez` (close MM) → 60 |
