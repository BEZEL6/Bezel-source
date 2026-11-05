# Music OSD settings (Kodi popup)

**Object:** Kodi's music OSD settings popup · Kodi: dialog `1105` (`Custom_1105_MusicOSDSettings.xml`) · grouplist `5000` · rows `5001`, `5002`, `5004`–`5009`
**Where:** Kodi-internal popup; no Bezel route opens it
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** present, unreachable from Bezel (no opener) · **Lock:** none

## Simple
A short Kodi-style list of visualisation options: hide or animate the background fanart, pick a visualisation, open its settings or presets, pick a lyrics add-on, get more visualisations. Bezel doesn't open it; visualisation choices live in [music controls](music-controls.md). It is kept only in case Kodi opens it by its internal id.

## Feel contract (any framework)
**Do not port.** A port gets visualisation choice and settings from Music controls only.

### States
Open / closed (Kodi popup).
### Timeline
Kodi standard popup open / close.
### Interruptions
—
### Continuity
—
### Layering
Over the current screen, as a dialog.
### Geometry
Kodi popup layout.
### Art
Kodi popup chrome.
### Input
Up / Down move (ends stay), Select toggles / runs, Back closes.
### Speed targets
—
### Never
No Bezel visualisation layer behind fullscreen chrome (416 NOBZVIZ removed Bezel's own viz add-on).
### Acceptance checks
—

## Kodi implementation (sandbox)

### How it works
- One vertical grouplist 5000; fanart rows are radiobuttons that flip a skin bool (tick = not hidden); rows that open another dialog close this one first; presets row only when the viz has presets; lyrics settings only when a lyrics add-on is chosen.
- No `ActivateWindow(1105)` anywhere in xml or scripts.
- Bezel's own viz add-on is gone (416): `bz_dustviz.py` at startup only forces `musicfiles.selectaction` off and disables `visualization.bezel` if present.

### Wiring
| Item | Value |
|---|---|
| defaultcontrol | 5000 |
| Window anim | `Animation_DialogPopupOpenClose` |

### Kodi workarounds (do not port)
The whole dialog.

## Related
[music-controls](music-controls.md) · [fanart-fs](fanart-fs.md)
