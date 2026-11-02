# Power menu (dialog 1118) — power-menu

**Object:** `power-menu` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/power-menu.md) · [layout](../layout/power-menu.md) · [state](../state/power-menu.md) · [motion](../motion/power-menu.md) · [art](../art/power-menu.md) · [input](../input/power-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/power-menu.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 6970 | `SetProperty(bz_tune_dirty,1,home)` | `SetProperty(bz_tune_dirty,1,home)` | `noop` | `noop` | `ClearProperty(bz_navtune,home)` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |
| 7800 | `noop` | `noop` | `` | `` | `SetProperty(bz_nav,true,home)` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. The first-Down handoff fix (real list focus on open) and the TUNER row (BUG-005) are both in. Opens with no zoom or slide transition, only the standard fade-in. Draft: not Rob-smoked.
- Select POWER on the main menu and a small list replaces the menu strip in the same spot: Shutdown, Quit Kodi, Suspend, Tuner. Back takes you straight back to the main menu on the POWER row.
- 2. That explicit focus matters: without it, Kodi's default focus hand-off ate the first Down press. SHUTDOWN looked focused, but QUIT needed two presses.
- 3. On close, if the user didn't go into the Tuner, a zero-delay alarm refocuses strip 6996 after the dialog is gone. One second later `bz_pwrswap` is cleared, so the strip's normal animations come back.
- 4. While media is playing the column shifts down 120 px (time 0) to clear the mini-player.
- | Openers | `DialogButtonMenu.xml` onload (Kodi's power/shutdown menu → 1118) · `Includes.xml` ~L1296 (MM POWER) · Tuner Back when `bz_tunesrc=pwr` (`Includes_Tuner.xml` ~L496: clear `bz_navtune`, `ActivateWindow(1118)`) |
- Up/Down moves through four rows. Left and Right do nothing. Select runs the row.
- TUNER opens the BEZEL Tuner on the main menu. Back from the Tuner reopens this power menu.
- Because `bz_tunesrc=pwr` is set *before* the close, `onunload` skips the 6996 refocus, so it doesn't fight the Tuner's 6970 focus. The Tuner's Back handler sees `pwr`, clears `bz_navtune` and reopens 1118. The new `onload` then clears `bz_tunesrc` again.
- ## Touch
