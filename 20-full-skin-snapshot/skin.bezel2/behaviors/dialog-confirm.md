# Confirm (Yes / No)

**Object:** Kodi's yes / no and OK dialogs · Kodi: `DialogConfirm.xml`, grouplist `9000` with buttons `10` (No) / `11` (Yes) / `12` (custom), includes `BzStdProgress` / `BzRefreshProgress`, `BzMSUnderlay`
**Where:** CONFIRM rows in the colour strip (570, 120, 390 × 900), message on the fanart stage (140, 220)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Every Yes / No question looks like the main menu: a CONFIRM strip with the choices as rows and the message on the left, over the Warm background (black + the MM fanart at MM dim). **No** is the first row and has focus, so a stray Select never confirms. Up / Down move, Select chooses, Back = No. Over fullscreen video or music it uses a light dim instead, so playback stays visible. Nothing else can steal its focus.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Question | an app action asks | Yes / No / Back | Warm underlay, CONFIRM rows, message |
| Over playback | asked during fullscreen video / music | same | dim (70 %) instead of the Warm underlay |
| Refresh layout | music info refresh with progress | same | refresh layout with progress |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | 200 fade | cubic out |
| close | 150 fade | cubic in |

### Interruptions
Background scripts never move focus while it's up (No / Yes always focused).

### Continuity
—

### Layering
Screen < Warm underlay (or dim) < strip chrome < rows / message.

### Geometry
Rows 390 × 58 from the strip top; title label 0, 30 (410 × 46); message textbox 0, 106 (410 × 480); progress 0, 610 (410 × 12).

### Art
Warm underlay: MM fanart lane at MM dim over black.

### Input
Up / Down move; Select chooses; Back = No; Left / Right nothing.

### Speed targets
—

### Never
- No focus loss on Yes / No (420 MODALGUARD, 432 CONFIRMFOCUS).
- No Yes as default.

### Acceptance checks
Remove a movie from library → CONFIRM, No focused; Back → nothing removed.

## Kodi implementation (sandbox)

### How it works
- defaultcontrol `always` 9000; `DepthDialog+`. Layout: `Window.IsActive(musicinformation) + Window.IsActive(progressdialog)` → `BzRefreshProgress`, else `BzStdProgress` (`BzMSUnderlay` visible `!fullscreenvideo + !visualisation`, else the B3 dim).
- Focus guards: `bz_flip.py _modal_blocks_strip()` (no strip focus while a modal is up); `_bz_fg_install(xbmc)` in every Bezel script drops `SetFocus` while yesno / ok dialogs are visible.
- Bezel caller: `bz_ctx.py remove <type> <id>` → Yes → `Dialog.Close(all)` → `VideoLibrary.Remove*` → `Container.Refresh`.

### Wiring
| Item | Value |
|---|---|
| Ids | 10 No, 11 Yes, 12 custom, 1 title, 9 message, 20 progress |
| Includes | `BzStdProgress`, `BzRefreshProgress`, `BzMSUnderlay`, `BezelMMStripChrome` |

### Kodi workarounds (do not port)
Script-side `SetFocus` filter: Kodi's `SetFocus` targets the topmost modal and unfocuses its control first.

## Related
[info-options](info-options.md) · [context-menu](context-menu.md) · [dialog-busy](dialog-busy.md)
