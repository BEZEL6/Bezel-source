# Power menu (dialog 1118)

**Object:** `Custom_1118_PowerMenu.xml` dialog `1118` (zorder 2) · list `7800` (SHUTDOWN / QUIT KODI / SUSPEND / SLEEP / TUNER)
**Where:** Over the Main Menu, in the strip column at x 570
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. The first-Down handoff fix (real list focus on open) and the TUNER row (BUG-005) are both in. Opens with no zoom or slide transition, only the standard fade-in. Draft: not Rob-smoked.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
Select POWER on the main menu and a small list replaces the menu strip in the same spot: Shutdown, Quit Kodi, Suspend, Tuner. Back takes you straight back to the main menu on the POWER row.

### How it works
1. 1118 opens over the MM. On `onload` it:
   - clears any old Tuner source (`bz_tunesrc`)
   - sets `bz_pwrswap=1`, so the MM strip 6996 skips its slide animations and hides that same frame (no double strip)
   - puts real focus on row 0 with `SetFocus(7800,0,absolute)`
2. That explicit focus matters: without it, Kodi's default focus hand-off ate the first Down press. SHUTDOWN looked focused, but QUIT needed two presses.
3. On close, if the user didn't go into the Tuner, a zero-delay alarm refocuses strip 6996 after the dialog is gone. One second later `bz_pwrswap` is cleared, so the strip's normal animations come back.
4. While media is playing the column shifts down 120 px (time 0) to clear the mini-player.

### Wiring
| Item | Value |
|---|---|
| Window | dialog 1118, zorder 2 (above Now Playing 1112) |
| Anim | `BezelSecFadeIn` (WindowOpen fade 0→100, 400 ms sine out). No zoom/slide (t4939 / K48) |
| defaultcontrol | 7800 (no `always`) |
| onload | `ClearProperty(bz_tunesrc,home)` · `SetProperty(bz_pwrswap,1,home)` (t4943 / K52: 6996 skips slides) · `SetFocus(7800,0,absolute)` |
| onunload | if `bz_tunesrc`≠`pwr` → `AlarmClock(bzpwrf,SetFocus(6996),00:00)` · always `AlarmClock(bzpwrsw,ClearProperty(bz_pwrswap,home),00:01)` |
| Group | 570,120; Conditional slide 0,120 time 0 when `Player.HasMedia` |
| Openers | `DialogButtonMenu.xml` onload (Kodi's power/shutdown menu → 1118) · `Includes.xml` ~L1296 (MM POWER) · Tuner Back when `bz_tunesrc=pwr` (`Includes_Tuner.xml` ~L496: clear `bz_navtune`, `ActivateWindow(1118)`) |

---

## Rows and keys

### Simple
Up/Down moves through four rows. Left and Right do nothing. Select runs the row.

### How it works
7800 is a static list of 56 px rows. The focused row draws the shared BEZEL highlight texture tinted with the MM bar colour, so it matches the main strip. A decorative separator sits between SUSPEND and TUNER. TUNER is a normal fourth list item (no separate button), so focus moves through it like any other row.

### Wiring
| Row | onclick |
|---|---|
| SHUTDOWN | `Shutdown()` |
| QUIT KODI | `Quit()` |
| SUSPEND / SLEEP | `Suspend()` |
| TUNER | `SetProperty(bz_tunesrc,pwr,home)` · `SetProperty(bz_navtune,true,home)` · `ClearProperty(bz_navbez)` · `ClearProperty(bz_navset)` · `Dialog.Close(1118)` · `AlarmClock(bz_tunp,SetFocus(6970),00:00)` |

- List 7800: top 40, 390×224, scrolltime 150, `onleft`/`onright` noop, `onback` `SetProperty(bz_nav,true,home)` (BUG-024).
- Focused layout: `BzATHiTex` image coloured `$VAR[BzMMBarCol]`.
- Separator image at top 206.

---

## TUNER round trip

### Simple
TUNER opens the BEZEL Tuner on the main menu. Back from the Tuner reopens this power menu.

### How it works
Because `bz_tunesrc=pwr` is set *before* the close, `onunload` skips the 6996 refocus, so it doesn't fight the Tuner's 6970 focus. The Tuner's Back handler sees `pwr`, clears `bz_navtune` and reopens 1118. The new `onload` then clears `bz_tunesrc` again.

### Wiring
`Includes_Tuner.xml` 6970 onback: `[bz_tunesrc=pwr]` → `ClearProperty(bz_navtune)` + `ActivateWindow(1118)`.

---

## Footer
- "BEZEL" + `System.AddonVersion` label at top 282.
- "design by. Robert Politano" + `us_flag` at 322.
- Kodi build label at 860.

## Touch
None specified.

## Related
mm-list.md · skin-settings-tuner.md · section-transitions.md

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/power-menu.md) · [state](../state/power-menu.md) · [motion](../motion/power-menu.md) · [art](../art/power-menu.md) · [input](../input/power-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## First Down hardening (5.33.322, Rob t2409 — current)
- onload order: `ClearProperty(bz_tunesrc)` · `SetProperty(bz_pwrswap,1)` · `CancelAlarm(bzpwrf,true)` (drops a pending close-alarm `SetFocus(6996)` from a previous close, e.g. Tuner→Back reopen) · `SetFocus(7800,0,absolute)` · `AlarmClock(bzpwrfoc,SetFocus(7800,0,absolute),00:00)` (re-asserts one tick later after the 6996→7800 hand-off). One Down from SHUTDOWN moves to QUIT.
