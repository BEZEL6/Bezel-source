# Play Next (1120 non-album mode)

**Object:** `Custom_1120_PlayNext.xml` dialog `1120` with `bz_dfs_mode` ≠ album · main `6400`, **big album pill** `6401`, tiles `6405`/`6406`; album viz in `MusicVisualisation.xml` (same pill `6401` via `BezelBigAlbumPill`, `6407`/`6408`, `bz_pnoff` + `bz_dfs_mode`)  
**Last updated:** 2026-10-31 · live tree (sides fade 3s/2s)  
**Status:** draft — matches live; not Rob-approved, not re-smoked

## What it does
**Naming:** 1120 mode control `6401` = **big album pill** (ALBUM ↔ PREV/NEXT). Not fan art pill `6391`.

1120 and FS album viz share Skin.String `bz_dfs_mode`: `album` = sides hidden, empty/reset = PREV/NEXT sides. The **big album pill** toggles on both windows.

## Keys (1120)
| Key | Behavior |
|---|---|
| Select on 6400 | Play/Pause (sets `bz_pnfoc=6403` when pausing → ghost logo) |
| Left / Right on 6400 | Previous / Next track |
| Up | Big album pill 6401 |
| Down on 6400 | noop |
| Select / Left / Right on big album pill | Toggle album ↔ Play Next |
| Up / Down on big album pill | Back to 6400 |
| Back | `bz_fsret=true` (1 s), close 1120 |
| Tap prev / next tile (6405/6406) | `Playlist.PlayOffset(music,∓1)` (shown only when that track exists) |

onunload: clears `bz_pnfoc`/`bz_pnsel` and refocuses the album rail for `bz_at_fsslide` (6368 / 6378 / 6398 / 6383).

## Fanart FS Play Next sides
In visualisation, `bz_pnoff=1` = sides off. Double-Select on 6390 clears it (sides on / album viz). 6409 right hit is bounce-only (does not clear `bz_pnoff`). 6410 → `bz_npmode=upnext`. Side tiles 6407/6408 play offset ∓1.

## Sides fade-in (WindowOpen)
Shared `BezelFSPlayNext` params `sdelay` / `sfade`: **3 s delay, 2 s fade** on both Dialogue FS (1120, explicit) and FS album viz / Play Next sides (MusicVisualisation, include defaults). Centre album + NP appear immediately; prev/next side albums fade in after the delay.

## Slide speed
`bz_at_fsslide`: 1 = 480 ms · 2 = 380 · 3/empty = 280 · 4 = 180. It is shared with Dialogue FS and viz preview-next.

## Cast / stub shadows
Stub cast opacity follows the shared sway clock (`bz_castL`/`bz_castR`, 5.33.170 BUG-021). Overall level = Tuner Viz opacity (5.33.171). Cast is gated on Cover.

## Related
big-album-pill.md · 
dialogue-fs.md · fanart-fs.md · sway-animations.md
