# Power menu

**Object:** power menu · Kodi: dialog `1118` (`Custom_1118_PowerMenu.xml`, zorder 2) · list `7800`
**Where:** in the strip column (x 570, top 120), replacing the MM strip in the same spot
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Select POWER on the main menu and a short list takes the strip's place: SHUTDOWN, QUIT KODI, SUSPEND / SLEEP, then (under a separator) TUNER. Below: BEZEL and its version, the design credit with a small flag, and the Kodi version. Up / Down move, Select runs the row, Back goes straight back to the main menu on POWER. TUNER opens the Bezel Tuner; Back from the Tuner's section rail comes back here, and TUNER opens it again.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Open | MM POWER; Kodi's own shutdown menu; Back on the Tuner rail | Back; a row | the list in the strip column; the MM strip hidden the same frame (never two strips) |
| Tuner | TUNER row | Tuner rail Back → Open | Tuner over the MM |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | 400 fade-in, no zoom / slide | sine out |
| close | instant; focus back on the MM POWER row | — |
| media playing | column 120 px lower (instant) | — |

### Interruptions
- First Down after opening moves to QUIT KODI (focus is really on row 0 from the first frame).
- Rapid Back from the Tuner: lands on this menu, then the MM; never a random window.

### Continuity
While this menu is up the strip chrome, dust and art stay exactly as the MM had them; the Tuner is gone (not drawn behind).

### Layering
MM art and dim < power list (in the strip column) < system dialogs.

### Geometry
| Piece | Value |
|---|---|
| Column | 570, 120 (+120 down with media) |
| List | top 40, 390 × 224, rows 56 px |
| Separator | top 206 |
| Footer | BEZEL + version top 282; credit + flag 322; Kodi version 860 |

### Art
Focused row: the shared Bezel highlight tinted with the MM bar colour; TUNER in Bezel blue.

### Input
| Action | Result |
|---|---|
| Up / Down | move |
| Left / Right | nothing |
| Select | SHUTDOWN / QUIT / SUSPEND / TUNER |
| Back | main menu (POWER row) |

### Speed targets
Open ≤ 400 ms; first Down responds.

### Never
- No zoom or slide (K48).
- No Tuner left drawn under the power menu (465 → 467).
- No colour strip missing after leaving the Tuner (467 TUNERPWR).
- Tuner re-entry always works (469 TUNERREOPEN).
- No double strip (MM strip hides the same frame).

### Acceptance checks
1. MM → POWER → Down once → QUIT KODI focused.
2. TUNER → Tuner → Back on the rail → this menu with the colour strip; TUNER → Tuner opens.
3. Back → MM on POWER.

## Kodi implementation (sandbox)

### How it works
- **onload** (in order): `ClearProperty(bz_tunesrc)`, `ClearProperty(bz_navtune)` (467: the Tuner closes before the first frame), `bz_pwrswap=1` (6996 hides with no animation), `CancelAlarm(bzpwrf)`, `SetFocus(7800,0,absolute)` + the same by a 0 s alarm (322).
- **onunload:** `bz_tunesrc` ≠ `pwr` → `AlarmClock(bzpwrf,SetFocus(6996),00:00)`; always `AlarmClock(bzpwrsw,ClearProperty(bz_pwrswap),00:01)`.
- **Openers:** `DialogButtonMenu.xml` onload (Kodi's shutdown menu → 1118), MM POWER, Tuner rail 7001 Back for every source except `fsctrl` (only `ActivateWindow(1118)`; 1118's onload clears the flags — 469).
- **TUNER row:** `bz_tunesrc=pwr`, `bz_navtune=true`, clear `bz_navbez` / `bz_navset`, `Dialog.Close(1118)`, `AlarmClock(bz_tunp,SetFocus(6970))`.

### Wiring
| Row | onclick |
|---|---|
| SHUTDOWN | `Shutdown()` |
| QUIT KODI | `Quit()` |
| SUSPEND / SLEEP | `Suspend()` |
| TUNER | above |
| List 7800 | onleft / onright noop; onback `SetProperty(bz_nav,true,home)`; scrolltime 150 |
| Anim | `BezelSecFadeIn` |
| Highlight | `BzATHiTex` coloured `$VAR[BzMMBarCol]` |

### Kodi workarounds (do not port)
- Double focus on load: Kodi's default focus hand-off eats the first Down.
- `bz_pwrswap`: hides the MM strip without its exit animation.
- Clearing the Tuner flags in onload: Kodi runs actions after a modal `ActivateWindow` only when the modal closes.

## Related
[mm-list](mm-list.md) · [skin-settings-tuner](skin-settings-tuner.md) · [section-transitions](section-transitions.md)
