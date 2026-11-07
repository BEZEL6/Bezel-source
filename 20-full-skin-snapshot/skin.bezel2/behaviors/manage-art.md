# MANAGE ART (media art + library info manager)

**Object:** Warm-strip dialog `1133` (`Custom_1133_ManageArt.xml`), MM row `manageart`, route `bz_mm.py manageart`
**Where:** over the current section, in the colour strip (right) with an art / info panel on the stage (left, 540 wide)
**Last updated:** 2026-11-06 · 5.33.477 · **Status:** SHELL ONLY (frame + placeholder row) · **Plan:** project doc `MEDIA_MANAGER_PLAN.md`

## Simple
One screen for managing artwork and library info. The strip always lists artists; the left panel shows the picked artist's art, albums and details. Edits are staged until SAVE ALL; CANCEL discards. Opened from the MM row after SETTINGS (just opens the screen) and, later, from a section's Options / Info menu on the focused item. **This build is the shell:** it opens, shows the frame and one placeholder row, and Back returns. Nothing is read from or written to the library.

## Feel contract (any framework)
### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Open | Select MANAGE ART in the MM | Back | strip chrome + title + row; left panel frame; section art held behind |

### Timeline
Same fade-in as the other Warm-strip dialogs (Settings 1130): the strip chrome is already up from the MM; no slide.

### Continuity
Back returns the way Settings does (`bz_nav` set, dialog closes). Section, Warm art and poster never unload under it.

### Geometry (1920 × 1080)
Left panel x `bz_stage_x`, y 120, 540 × 900. Strip x `bz_strip_x`, width `bz_strip_w`, list top 112 inside the strip.

### Never
Do not add a second screen or modal: everything stays on this one. Do not write to the library before SAVE ALL. A chosen dark cover is ordinary album art (no custom art key, no display mode).

## Kodi implementation (sandbox)
### How it works
`ActivateWindow(1133)` after `SetProperty(bz_setopen)` and `ClearProperty(bz_nav)`, as for Settings / Add-ons / Sources. 1133 is registered in `bz_set_hub` / `SETTINGS_TREE` (hub) so the global artwork group shows, and in the Warm-strip hide lists (list 60 fades, double-tap hint).
### Kodi workarounds (do not port)
Library access will go through Kodi JSON-RPC from Python (see the plan's probe results); Bezel's own library replaces this later, so the screen talks only to a small library contract.
