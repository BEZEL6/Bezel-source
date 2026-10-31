# Play Next (1120 non-album mode)

**Object:** `Custom_1120_PlayNext.xml` dialog `1120` with `bz_dfs_mode` ≠ album · main `6400`, mode pill `6401`, prev/next tiles `6405`/`6406`; Fanart variant in `MusicVisualisation.xml` (`6407`/`6408`, `6409`/`6410`, `bz_pnoff`)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
1120 has two modes, set by Skin.String `bz_dfs_mode`: `album` = Dialogue FS, empty/reset = Play Next with prev/next tiles. The pill toggles between them.

## Keys (1120)
| Key | Behavior |
|---|---|
| Select on 6400 | Play/Pause (sets `bz_pnfoc=6403` when pausing → ghost logo) |
| Left / Right on 6400 | Previous / Next track |
| Up | Pill 6401 |
| Down on 6400 | noop |
| Select / Left / Right on pill | Toggle album ↔ Play Next |
| Up / Down on pill | Back to 6400 |
| Back | `bz_fsret=true` (1 s), close 1120 |
| Tap prev / next tile (6405/6406) | `Playlist.PlayOffset(music,∓1)` (shown only when that track exists) |

onunload: clears `bz_pnfoc`/`bz_pnsel` and refocuses the album rail for `bz_at_fsslide` (6368 / 6378 / 6398 / 6383).

## Fanart FS Play Next sides
In visualisation, `bz_pnoff=1` = sides off. 6409 clears it (sides on), 6410 → `bz_npmode=upnext`, and side tiles 6407/6408 play offset ∓1.

## Slide speed
`bz_at_fsslide`: 1 = 480 ms · 2 = 380 · 3/empty = 280 · 4 = 180. It is shared with Dialogue FS and viz preview-next.

## Cast / stub shadows
Stub cast opacity follows the shared sway clock (`bz_castL`/`bz_castR`, 5.33.170 BUG-021). Overall level = Tuner Viz opacity (5.33.171). Cast is gated on Cover.

## Related
dialogue-fs.md · fanart-fs.md · sway-animations.md
