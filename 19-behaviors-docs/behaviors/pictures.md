# Pictures

**Object:** Pictures section · Kodi: `MyPics.xml`, view `63` (`View_63_BezelPictureList`), side `9000` (`6`, `7`, `9`, `624`, `621`), section menu `1119` (7940–7947), `BezelFSUnderlay`
**Where:** MM PICTURES
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
PICTURES opens your picture sources in Bezel chrome with a fade-in. Back at the top (or Left anywhere) opens the main menu; inside a folder Back goes up. Menu / double-Select opens the section menu. With music playing, Tab or Display opens Bezel's fullscreen music over Pictures.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Sources | MM PICTURES | Select → folder; Back → MM | sources list |
| Folder | Select | Back → parent | thumbs / list |
| Section menu | Menu / double Select | action / Back | section menu |
| Fullscreen music | Tab / Display with music | Back | fullscreen music over Pictures |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | 400 fade-in | sine out |
| fullscreen music over it | 300 fade (black cover + fanart stage) | sine |

### Interruptions
Back at the root from the side menu also opens the MM.

### Continuity
The big album stays on screen while music plays (under the MM it's the held art).

### Layering
Pictures < MM dim < big album layer < MM / fullscreen chrome.

### Geometry
Kodi picture view inside the Bezel chrome.

### Art
Picture thumbnails; held MM art under the menu.

### Input
| Action | Result |
|---|---|
| Left | MM (when allowed) |
| Back | parent folder; root → MM |
| Menu / double Select | section menu |
| Tab / Display | fullscreen music (if playing) |

### Speed targets
Open ≤ 400 ms.

### Never
No blank art behind the MM when coming back from Pictures (WARM HOLD: keeps the last Music / Movies / TV art).

### Acceptance checks
MM → PICTURES → folder → Back → Back → MM. With music: Tab → fullscreen music → Back → Pictures.

## Kodi implementation (sandbox)

### How it works
- Opener `GO['pictures']`: `ClearProperty(bz_nav,home)` + `ActivateWindow(pictures)`.
- `BezelWindowFade`; `BezelSecDim` on the parent group; defaultcontrol `always` 63.
- Root = folder path empty or `sources://pictures/`; 63 and every side button: root + `!$EXP[bz_navmenu]` onback → `bz_nav=true`; 63 onleft `$EXP[bz_navok]` → `bz_nav=true`.
- `pictures` is in `bz_dtap.py` SECW → 1119.
- `BezelFSUnderlay` at the end of `<controls>` (472, see [music-fanart-fs](music-fanart-fs.md)).

### Wiring
| Item | Value |
|---|---|
| Includes | `DefaultBackground`, `BezelFanartCycler`, `ListThumbInfoPanel`, `BezelDtapHint`, `MediaMenu*`, `BezelFSUnderlay` |
| Section menu | 1119 rows 7940–7947 |

### Kodi workarounds (do not port)
Root detection by folder path; the fullscreen underlay copy.

## Related
[context-menu](context-menu.md) · [mm-list](mm-list.md) · [music-fanart-fs](music-fanart-fs.md)
