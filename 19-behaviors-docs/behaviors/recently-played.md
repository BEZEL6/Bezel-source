# Recently played

**Object:** MM row RECENTLY PLAYED · Kodi: `bz_mm.py GO['recent']` → Music window `musicdb://recentlyplayedalbums/` with `bz_navroot` set
**Where:** main menu → Music
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
RECENTLY PLAYED on the main menu opens Music on the albums you played most recently, with the small album cover at the top of the strip above the rows. It behaves exactly like the Music Albums list. Back at the top reopens the main menu on the RECENTLY PLAYED row.

## Feel contract (any framework)
Same as the Music list's Albums level ([music-list](music-list.md)); differences:

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Recent albums | MM RECENTLY PLAYED | Select → songs; Back → MM (row RECENTLY PLAYED) | half list: small cover on top, album rows |
### Timeline
As section entry (400 fade-in, rows after 350).
### Interruptions
Fast Back-Back from the songs never overshoots into the MM.
### Continuity
The MM reopens on RECENTLY PLAYED, not MUSIC.
### Layering
As the Music list.
### Geometry
As the Music list (small cover 570, 120, 390 × 390).
### Art
As the Music list.
### Input
As the Music list.
### Speed targets
As the Music list.
### Never
- No old list-group cover in the stage corner (472 ALBUMHALF).
- No plain 60 px list without the cover (466 ALBUMCOVER).
### Acceptance checks
MM → RECENTLY PLAYED → small cover above the rows; Back → MM on RECENTLY PLAYED.

## Kodi implementation (sandbox)

### How it works
- Opener: `SetProperty(bz_navroot,musicdb://recentlyplayedalbums/,home)` + `RunScript(bz_cmd.py,tomusic,musicdb://recentlyplayedalbums/)` (load-then-close).
- Root: bz_flip sets `bz_rootarm` / `bz_atnavroot` after 0.6 s because the folder equals `bz_navroot`; `bz_atroot` makes list 60 Back open the MM.
- MM reopen row: path starts with `musicdb://recentlyplayed` → row 3.
- Half list via `bz_mhalf` (`Container.Content(albums)`).

### Wiring
| Item | Value |
|---|---|
| Home | `bz_navroot`, `bz_rootarm`, `bz_atnavroot` |
| Expressions | `bz_atroot`, `bz_mhalf`, `bz_covercol` |

### Kodi workarounds (do not port)
Root arm delay (Kodi Back queueing).

## Related
[music-list](music-list.md) · [mm-list](mm-list.md)
