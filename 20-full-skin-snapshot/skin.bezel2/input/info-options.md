# Options + Info — info-options

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `info-options` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/info-options.md) · [layout](../layout/info-options.md) · [state](../state/info-options.md) · [motion](../motion/info-options.md) · [art](../art/info-options.md) · [input](../input/info-options.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/info-options.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 9000 | `Close` | `Close` | `noop` | `9000` | `` |
| 9969 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9969 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9971 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9971 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9974 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9978 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9978 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9979 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9979 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9980 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |
| 9980 | `` | `` | `9000` | `` | `ClearProperty(bz_ci_more)` |
| 9990 | `` | `` | `` | `` | `ClearProperty(bz_ci_more)` |

**Semantics from behavior (verbatim lines):**
- Status:** draft. This doc matches the live tree. The left fanart mask has been off since 5.33.205. Rob has not approved it.
- Simple.** One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.
- ## Left fanart
- Simple.** The left fanart stays visible while the menu is open.
- Wiring.** The old left black mask (`-60,-60` 630×1200 `FF000000` `bezel/white.png`) is `visible=false` in DialogVideoInfo / DialogMusicInfo / DialogAddonInfo (5.33.205). Video still has `BezelBlack` when `!Window.IsVisible(videos)`.
- More (`1`):** Choose art 7710 · Refresh 6 · Set rating 7 · Director 13 / watched 9095 / Add to favourites 9097 / Remove from library 9098 (video) · Other 12 (music) · Section options 9980 (music) · ‹ Back 9096.
- Section (`sec`):** View type 9979 · Sort 9971 · Filter / Order · Update library · Party mode · Go to playlist · Get more · Edit nodes · Add-on settings · Clearart toggle 9969 (`bz_tvclear_off`, video) · Visualizer 9974 (music) · ‹ Back 9990/9967.
- Simple.** Up and Down move. Left or Right closes. Back on a sub-page goes back to Main. Back on Main closes.
- | Up | `noop` | `noop` |
- | Down (last row) | `50` cast list | `9000` (stays) |
- | Left / Right | `Close` | `Close` |
- | Back on sub page | `ClearProperty(bz_ci_more)` + `AlarmClock(bzci_back,SetFocus(9980),00:00,silent)` | same |
