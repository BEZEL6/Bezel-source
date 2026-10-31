# Movies list

**Object:** `MyVideoNav.xml` · list `60` (movies nodes)  
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Opened from MM MOVIES pill sub. Left/Back at root → MM.

## Keys
| Key | Behavior |
|-----|----------|
| Up | Move up; at top row → ALL button `6098` if visible, else stay (Home `bz_topedge`; no native wrap — 5.33.120) |
| Down | Move down; at last row → `6098` if visible, else stay (`bz_bottomedge`) |
| Select | Open / play |
| Left / Back at root | Open MM |

## Touch
None specified.

## Code notes
MyVideoNav.xml

## Related
mm-list.md · tv-list.md · video-osd.md

## Live notes (5.33.194)
- Pills: TITLES→RECENTLY ADDED→YEARS→ACTORS→SETS→GENRES (`bz_mm.py SUBS`).
- Actors cover column slides list grouplist down 450 (`bz_actcov`, t4464).
- Poster hold: `bz_flip.py` sets Home `bz_movposter_hold` (non-Default poster) so Movies poster art holds across MM / TV highlight; 5.33.189 movies-only fanart bridge (unused on TV/Music). See mm-warm.md.
- Section open = fade-in only (section-transitions.md).
