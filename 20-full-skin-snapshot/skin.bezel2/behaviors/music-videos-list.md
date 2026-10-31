# Music videos list

**Object:** `MyVideoNav.xml` list `60` with `videodb://musicvideos/` (`bz_mm.py GO['mv']`)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Music videos library in the same video window as Movies/TV. It shares that window's nav, grouplist and Up wrap.

## Keys
| Key | Behavior |
|---|---|
| Up | Top row → ALL `6098` if visible, else stay (`bz_topedge`, 5.33.120) |
| Select | Open / play |
| Left / Back at root | Open MM |
| Side 9000 | radiobutton 16 visible for MusicVideos content (Kodi option); Update library 619; Playlist 612 |

## Notes
No pill and no MM row of its own. The `mv` GO entry exists in `bz_mm.py`.

## Related
movies-list.md · tv-list.md
