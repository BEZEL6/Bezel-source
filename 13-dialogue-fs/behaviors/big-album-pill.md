# Big album pill

**Object:** Shared include `BezelBigAlbumPill` → control `6401` (`bz_dfs_mode`) on Dialogue FS `Custom_1120_PlayNext.xml` **and** FS album viz `MusicVisualisation.xml`  
**Last updated:** 2026-10-31  
**Status:** live on both windows — id stays `6401`

## Name
**Big album pill** — ALBUM ↔ PREV/NEXT mode control. Same chrome, position (upper right `1360,60`), and behavior on Dialogue FS and full screen album viz. Not the fan art pill (`6391`).

## Modes
| Label | `bz_dfs_mode` | Effect |
|-------|---------------|--------|
| ALBUM (default) | `album` | Side albums hidden |
| PREV/NEXT | empty / reset | Side albums shown |

Select / Left / Right toggle. Shared Skin.String across 1120 and viz.

## Dialogue FS (1120)
Visible always while dialog open. Down / Up → `6400`. Back → close 1120 (fsret latch).

## Full screen album viz (MusicVisualisation)
Visible while album viz active (`bz_pnoff` cleared) + audio playing. Fan art pill `6391` is **hidden** in album viz (fanart view only). Down / Up / Back → `6390`. Sides via `BezelFSPlayNext` param `sides=!album` (match 1120). Touch side hits `6407`/`6408` also require PREV/NEXT mode.

## Related
dialogue-fs.md · play-next.md · fanart-fs.md (fan art pill `6391`)
