# Kodi Settings — settings

**Object:** `settings` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/settings.md) · [layout](../layout/settings.md) · [state](../state/settings.md) · [motion](../motion/settings.md) · [art](../art/settings.md) · [input](../input/settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/settings.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 120 | `` | `` | `100` | `140` | `` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |
| 9000 | `noop` | `9000` | `9000` | `9000` | `SetProperty(bz_nav,true,home)` |
| 9130 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9130` | `9130` | `ClearProperty(bz_setx,home)` |
| 9131 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9131` | `9131` | `RunScript(special://skin/scripts/bz_set.py,pgback)` |
| 9132 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9132` | `9132` | `RunScript(special://skin/scripts/bz_set.py,pgback)` |

**Semantics from behavior (verbatim lines):**
- ## BEZEL Settings 1130 — Back (current, 5.33.240)
- Back on home list 9130: clear `bz_setx` → `SetProperty(bz_setret,1,home)` → `SetProperty(bz_nav,true,home)` → 1 s `AlarmClock(bz_setmm, bz_nav=true)` re-arm → `Dialog.Close(1130)`. MM opens before the dialog closes; re-arm covers a close that lands on the section after the first set.
- Sub-page 9131 Back → `pgback` (back to 9130 on SERVICES), unchanged.
- Object:** `Settings.xml` (Settings home, list `9000`) · `SettingsCategory.xml` sub-pages · Back in sub-lists handled by `scripts/bz_dtap.py` (`bz_setback`)
- Status:** Live in 5.33.207. Back from Settings home reopens the MM with a 1 s re-arm. Back in a sub-list returns to its category list. Every Settings level fades in 400 ms sine. Draft: not Rob-approved.
- SETTINGS on the main menu opens Kodi's settings home. Up and Down move, and Select opens a category. Back takes you straight back to the main menu.
- The list traps focus: Left does nothing, and Right/Up/Down stay on 9000.
- Back runs two steps:
- The re-arm covers the race where Kodi's own window change back to the opener (Videos or Music) lands after the first set and closes the MM again. The second set restores it on the opener row.
- ## Sub-settings Back
- Inside a settings category, Back from the right-hand list returns you to the category list on the left first, instead of leaving the page.
- Instead, `bz_dtap.py` writes `special://profile/keymaps/zz_bezel2_noctx.xml`. In each settings window, that file maps Back/Backspace to `NotifyAll(bz,bz_setback)`.
