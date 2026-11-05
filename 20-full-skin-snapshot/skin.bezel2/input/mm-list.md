# MM list (Main Menu strip) — mm-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-list` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-list.md) · [layout](../layout/mm-list.md) · [state](../state/mm-list.md) · [motion](../motion/mm-list.md) · [art](../art/mm-list.md) · [input](../input/mm-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [mm-list baselines](../port-refs/mm-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 6897 | `ClearProperty(bz_mmidle,home)` | `ClearProperty(bz_mmidle,home)` | `ClearProperty(bz_mmidle,home)` | `ClearProperty(bz_mmidle,home)` | `ClearProperty(bz_mmidle,home)` |
| 6898 | `6996` | `ClearProperty(bz_nav,home)` | `6996` | `6996` | `ClearProperty(bz_nav,home)` |
| 6958 | `6957` | `6959` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6966 | `noop` | `6967` | `noop` | `6996` | `ClearProperty(bz_nav,home)` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |

**Semantics from behavior (verbatim lines):**
- Simple.** Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.
- How it works.** Opening just sets Home `bz_nav=true`. The strip, the dim and the warm underlay all follow `$EXP[bz_navmenu]`. Section lists use `$EXP[bz_navok]` before opening, so the menu cannot reopen during a nav lock or grace window. While the menu is open, the focus bounces send any focus that lands on list 60 back to 6996, unless a pick is in progress (`bz_mmpick`). The underlay stays warm behind the strip (mm-warm.md, LOCKED).
- Geometry: left 0, top 40, 390×728, `scrolltime` 150.
- | Row | sec | Select |
- Every non-library GO entry first runs `ClearProperty(bz_nav)`. `bz_mm.py` drops a repeat Select within 300 ms (`MMLOCK_S=0.30`). Before GO it runs `store()` (`Skin.String(bz_lastart_<sec>)`), sets `bz_mmpick=true` and closes 1112 if open.
- Simple.** Up and Down move through the rows. Down from the last row wraps to MUSIC. Up from MUSIC goes to the mini-player when something plays. Left and Right on MUSIC/MOVIES/TV change the primed pill.
- | Down (last) | `SetFocus(6996,0,absolute)`, wraps to MUSIC |
- | Up (first) | video → `6966`; audio → `6958`; nothing → `SetFocus(6996,12,absolute)` |
- | Select | open (table above) |
- | Back | close MM → list 60 |
- | Right / Left on MUSIC / MOVIES / TV | pill forward / back (chip only, does **not** enter the list) |
- | Left / Right on SETTINGS and other rows | *none* (Select only) |
