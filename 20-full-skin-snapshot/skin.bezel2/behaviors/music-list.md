# Music section list

**Object:** `MyMusicNav.xml` · list `60` (MM closed)  
**Last updated:** 2026-10-31 · A-Z jump bar no black bg
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Left / Back at root → open MM (`mm-list.md`). Select opens item / plays.

## Keys
| Key | Behavior |
|-----|----------|
| Up | Move up; at top row → ALL button `6097` if visible, else stay (sets Home `bz_topedge`; no native wrap — 5.33.120) |
| Down | Move down; at last row → `6097` if visible, else stay (`bz_bottomedge`; never wraps to `..`) |
| Select | Open / play item |
| Left / Back at root | Open MM |

## Touch
Big album while playing → Dialogue FS 1120 (Rob).

## Code notes
MyMusicNav.xml; side buttons: Update library, Playlist, node editor, More add-ons


## A-Z jump bar
Grouplists `6100` (Music artists/songs) and `6500` (Movies/TV) at left **78**. Letters only — **no black fade/background** behind the bar (`BezelAZFade` emptied Oct 31 2026; was `fade_top`/`fade_bottom`).

## Related
mm-list.md · dialogue-fs.md

## Layout / now playing (live 5.33.194)
- List 60 sits in a vertical grouplist (450×900 true clip, t4533); grouplist owns onup/ondown (Kodi overwrites a single child's nav).
- MM open: list chrome hides; strip 6996 owns focus; underlay = `musicdb://artists/` (see mm-warm.md).
- While audio plays, the big album lives in album grouplist `6397` (speed rails `6367`… per `bz_at_fsslide`; default mid-high = 6397/6398/6399). **5.33.121:** the compact NP block rides grouplist 6397 with the big album — no separate −1100 slide. **5.33.125:** no 1120 fade; Music NP stays with the album; FS copy hidden over music.
- Tap big album → Dialogue FS 1120 (dialogue-fs.md). Pills: ARTISTS→ALBUMS→GENRES→RECENT SONGS→RECENT ALBUMS (mm-list.md).

## Related (more)
now-playing.md · dialogue-fs.md · section-transitions.md · mm-warm.md
