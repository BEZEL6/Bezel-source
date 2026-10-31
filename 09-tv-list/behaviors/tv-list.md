# TV Shows list

**Object:** `MyVideoNav.xml` · list `60` (tvshows nodes)  
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Opened from MM TV pill sub. Left/Back at root → MM.

## Keys
| Key | Behavior |
|-----|----------|
| Up | Move up; at top row → ALL button `6098` if visible, else stay (Home `bz_topedge`; no native wrap — 5.33.120) |
| Down | Move down; at last row → `6098` if visible, else stay (`bz_bottomedge`) |
| Select | Open season/episode / play |
| Left / Back at root | Open MM |

## Touch
None specified.

## Code notes
MyVideoNav.xml


## Clearlogo / clearart (colour strip)
- Header logo at colour-strip top (`Includes_Bezel.xml` t4153 / `BzTVClear`).
- **MM closed:** single image `fadetime` **300** (same as poster browse).
- **MM open:** A/B lane `bz_clr_a/b` + `bz_clr_side` / `bz_clr_on` / `bz_clr_empty` from `bz_flip.py` `_ab_clear` — same settle 0.25 s + load 0.5 s as fan/pos; XML Visible/Hidden **1500 ms** sine inout (matches fanart + poster A/B).
- Title fallback when no clear art / `bz_tvclear_off` / `bz_clr_empty`.

## Related
mm-list.md · movies-list.md

## Live notes (5.33.194)
- Pills: SHOWS→WATCHING→YEARS→ACTORS→RECENT→GENRES (`bz_mm.py SUBS`: titles, inprogresstvshows, years, actors, recentlyaddedepisodes, genres).
- Shares Movies list grouplist/nav (6098 ALL). Movies poster hold / fanart bridge do not apply to TV art.
- Known open: Movies→TV highlight can jump back to Movies.
