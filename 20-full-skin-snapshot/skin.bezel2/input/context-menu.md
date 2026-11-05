# Section menu (context) — context-menu

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `context-menu` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/context-menu.md) · [layout](../layout/context-menu.md) · [state](../state/context-menu.md) · [motion](../motion/context-menu.md) · [art](../art/context-menu.md) · [input](../input/context-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/context-menu.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 9000 | `Close` | `Close` | `noop` | `noop` | `` |

**Semantics from behavior (verbatim lines):**
- Where:** Options+Info template shell (black left mask, BezelLogo, 450 fanart crop `BzCIStage`, title at 150,150, `BzCIStripBG` strip, rows at 582,166)
- Simple.** BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.
- How it works.** The keymap sends menu keys to the background script instead of Kodi. `bz_dtap.info()` then picks the menu. Kodi's own contextmenu is closed first in case it opened anyway. That is a race: Kodi can open its menu before the notify arrives. On a double-tap the script also sets `bz_dtapinfo` for 0.8 s.
- `bz_ctx` handler: closes Kodi `contextmenu` (up to 40 × 25 ms), then `info()`.
- Simple.** Up and Down move through the rows and stop at the ends. Left or Right closes. Select runs the row. Back closes.
- How it works.** Most rows close 1119 first and then fire the action on a 0-second AlarmClock. That way the action lands on the window underneath, with the right focused item, instead of on the dialog.
- | Up / Down | `onup`/`ondown` `noop` on 9000: no wrap, no escape |
- | Left / Right | `Close` |
- | Select | e.g. 7901 `Dialog.Close(1119,true)` + `AlarmClock(bzsc,Action(Select),00:00,silent)` |
- | Back | close |
- `<defaultcontrol always="true">9000</defaultcontrol>`, `DepthDialog+`, no pop-in anim (5.33.29). Rows use `BzCIBtn`. The left mask (`-60,-60` 630×1200 `FF000000`) is still **on** here. Only the Info dialogs disabled theirs (info-options.md).
- Music/Video playlist:** Play from here 7911 · Item info 7912 · Move up/down 7913/7914 · Remove 7915 · Shuffle 7916 (SendClick 20) · Repeat 7917 (26) · Save 7918 (21) · Clear 7919 (22)
