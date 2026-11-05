# Music videos list

**Object:** music videos library · Kodi: `MyVideoNav.xml` list `60` on `videodb://musicvideos/` (`bz_mm.py GO['mv']`), ALL `6098`, A–Z `6500`
**Where:** the video window with music-video content (no MM row of its own)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live (reachable from Kodi paths / sources only) · **Lock:** none

## Simple
Music videos open in the same screen as Movies and TV and behave exactly like them: strip list, fanart stage, poster, the same keys. The main menu has no MUSIC VIDEOS row (removed in 5.33.60); the screen appears when you browse to music videos another way.

## Feel contract (any framework)
Same contract as [movies-list](movies-list.md) (states, timeline, interruptions, continuity, layering, geometry, art, input, speed). Differences only:

### States
Titles list; folders by Kodi's music-video nodes. Section options adds Party Mode for music videos.
### Timeline
As Movies.
### Interruptions
As Movies.
### Continuity
As Movies.
### Layering
As Movies.
### Geometry
As Movies.
### Art
Music video poster / fanart / thumb; no art → title only.
### Input
As Movies.
### Speed targets
As Movies.
### Never
No MM row (5.33.60 removed MUSIC VIDEOS + PLAYLISTS from the MM).
### Acceptance checks
Open a music-videos path: strip list, poster, Back steps up.

## Kodi implementation (sandbox)

### How it works
- `bz_mm.py` detects the section as `mv` when `Window.IsActive(videos) + Container.Content(musicvideos)`; GO `bz_cmd.py go videodb://musicvideos/`.
- Navigation, ALL row, A–Z bar, Back / root-arm rules as the Music / Movies lists.

### Wiring
| Item | Value |
|---|---|
| GO | `RunScript(bz_cmd.py,go,videodb://musicvideos/)` |
| Section options | 9982 Party Mode (`SendClick(16)`, `Container.Content(MusicVideos)`) |

### Kodi workarounds (do not port)
As Movies.

## Related
[movies-list](movies-list.md) · [music-list](music-list.md)
