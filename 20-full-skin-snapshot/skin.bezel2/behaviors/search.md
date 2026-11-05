# Search

**Object:** Search hub · Kodi: dialog `1107` (`Custom_1107_SearchDialog.xml`), list `9000`
**Where:** MM SEARCH; strip column (570, 120)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
SEARCH opens a small Bezel hub in the strip (same look as Settings and Add-ons): SEARCH LOCAL LIBRARY, SEARCH ADD-ONS, SEARCH YOUTUBE. Each row shows a short description under the divider. Missing search add-ons are installed / enabled when you pick them. Back closes it and reopens the main menu.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hub | MM SEARCH | Back → MM; a row → that search | header SEARCH · "KODI · SEARCH", » rows, description |

### Timeline
400 fade-in (sine out).

### Interruptions
—

### Continuity
Under it the section list and double-tap hint hide; the held art stays.

### Layering
Art < strip hub < dialogs.

### Geometry
Strip box at 570, 120 (MM strip chrome box).

### Art
None of its own (held MM art behind).

### Input
Up / Down move; Select runs; Back → MM.

### Speed targets
—

### Never
No blank art behind the hub.

### Acceptance checks
MM → SEARCH → SEARCH ADD-ONS → Kodi's add-on search; Back → MM.

## Kodi implementation (sandbox)

### How it works
- Opened by `ActivateWindow(1107)` from the MM row. Rows: `script.globalsearch` (install / enable if missing), `ActivateWindow(addonbrowser,addons://search/)`, `plugin.video.youtube` search (install / enable if missing). Description from item property `desc`.
- Back closes 1107 and sets `bz_nav`. While 1107 is visible list 60 and the double-tap hint hide (as for 1130 / 1131 / 1117 / 1132). `BezelSecFadeInDialog`.

### Wiring
| Item | Value |
|---|---|
| Strip chrome | `BezelMMStripChrome` box |
| Fade | `BezelSecFadeInDialog` |

### Kodi workarounds (do not port)
Installing add-ons on demand.

## Related
[mm-list](mm-list.md) · [addons](addons.md) · [settings](settings.md)
