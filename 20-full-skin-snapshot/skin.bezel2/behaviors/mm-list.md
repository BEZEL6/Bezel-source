# MM list (Main Menu strip)

**Object:** Main Menu strip list `6996`  
**Where:** Colour strip under `$EXP[bz_navmenu]`  
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** approved — live tree matches (verified 5.33.194)  
**Skin:** skin.bezel2 (Estuary fork) · live 5.33.194

## Open / close
| Action | Behavior |
|--------|----------|
| Left or Back-at-root from a section list, or M | Open MM; focus strip `6996` |
| Back | Close MM → section list |
| Select on a row | Open that destination; close MM |
| Focus while open | Strip owns focus; underlay stays warm behind |

## Rows (top → bottom)
MUSIC · MOVIES · TV SHOWS · RECENTLY PLAYED · FAVOURITES · SEARCH · PICTURES · ADD-ONS · SETTINGS · MEDIA SOURCES · POWER

## Keys
| Key | Behavior |
|-----|----------|
| Up / Down | Move rows; Down from last wraps to MUSIC (row 0). Up from MUSIC: video playing → `6966`; audio playing → mini-player `6958`; nothing playing → wraps to last row (POWER, index 12) |
| Select | Open that section; Music / Movies / TV open the **primed pill** sub |
| Back | Close MM → section list |
| Right on MUSIC / MOVIES / TV | Cycle primed pill **forward** (chip only; does **not** enter list) |
| Left on MUSIC / MOVIES / TV | Cycle primed pill **backward** |
| Left / Right on SETTINGS | *None* (Select only) |

## Primed pills (wrap)
| Section | Order |
|---------|--------|
| MUSIC | ARTISTS → ALBUMS → GENRES → RECENT SONGS → RECENT ALBUMS |
| MOVIES | TITLES → RECENTLY ADDED → YEARS → ACTORS → SETS → GENRES |
| TV | SHOWS → WATCHING → YEARS → ACTORS → RECENT → GENRES |

## Pill UI
- Chip + ‹ › on the focused Music / Movies / TV row
- Last choice remembered across sessions

## Code notes (implement / keep in sync)
- List: `Includes_Bezel.xml` control `6996`
- Select open: `scripts/bz_mm.py` + `SUBS` paths
- Cycle props: `bz_mmsub_music` / `bz_mmsub_movies` / `bz_mmsub_tv` (+ Skin.String `bz_last_mmsub_*`)
- L/R live in `Includes_Bezel.xml` 6996 `onleft`/`onright` gated on `ListItem.Property(sec)` = music/movies/tv only (vars `BzMMPrev_*`/`BzMMNext_*`); SETTINGS has no L/R handler (Select-only).
- Pill paths live in `bz_mm.py` `SUBS` in the approved order; `restore()` rebuilds pills from `bz_last_mmsub_*` after ReloadSkin.
- Former "pending vs live" note removed: SETTINGS Select-only + new Movies/TV orders are shipped.

## Related
- `music-list.md` (separate — Music section list/grid, MM closed)
- `movies-list.md` · `tv-list.md`

## Strip soft shadow (current)
`BezelMMStripChrome` soft cast `bezel/mm_strip_shadow_c.png` is placed at **left=-47**, top=-36, width w2 (470). Dark contact sits on the colour-strip left edge (was left=-37, ~10px inside).

