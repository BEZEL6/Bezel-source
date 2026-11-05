# Music list

**Object:** the Music section · Kodi: `MyMusicNav.xml`, list `60` in `View_60_BezelInfoList` (Includes_Bezel), ALL row `6097` / long-list pill `6088`, A–Z bar `6100`, FULLSCREEN pill `6886`, NP block `6390`, meta `BzMMetaSmall` / `BzMMetaBig`
**Where:** Music: fanart stage on the left, list in the colour strip, big album on the right
**Last updated:** 2026-11-04 · 5.33.474 · **Status:** live · **Lock:** none

## Simple
Music has three levels: **Artists → Albums → Songs**, each a plain list in the colour strip. On the left the artist's fanart fills the stage with the meta on top (small ARTIST / artist name, big name / album title, year and genre pills); on the right the big album sways. On Albums (an artist's albums, the Albums list, Recently played / added) a small album cover sits at the top of the strip above the rows. An **ALL ALBUMS** (or **ALL DISCS**) row opens everything at once when there is more than one. Long lists get an A–Z jump bar on the left. Select on a song plays it in place. Back steps up a level, and at the top opens the main menu.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| L1 Artists | MM MUSIC (pill Artists) | Select → L2; Back → MM | artist rows; stage = artist fanart; meta ARTIST / name; A–Z bar if > 38 rows |
| L2 Albums | Select an artist; MM pill Albums; Recently played / added | Select → L3; Back → L1 / MM | small album at the top of the strip (half list), album rows; ALL ALBUMS under the last row (2+ albums) |
| L3 Songs | Select an album / ALL ALBUMS | Back → L2 | song rows, `..` on top; meta artist / album title |
| ALL ALBUMS | ALL row | Back → the ALL row | every song, grouped with an album header bar on each album's first track |
| Folder lists (Genres, Years, Sources …) | MM pill / Select | Back | rows only, no info card behind them |
| Playing | Select a song | stop | big album = playing cover; FULLSCREEN pill top left; compact NP under the album |

### Timeline
| What | Duration | Curve |
|---|---|---|
| section entry (see [section-transitions](section-transitions.md)) | 400 fade-in, rows after 350 hold | sine out |
| row cascade | 286 per row, 30 stagger | Tuner |
| row scroll | 271 | cubic |
| big album / poster art change | 400 crossfade | sine |
| idle album dissolve (A/B) | 400 | sine |
| list fades under Now Playing / fullscreen | 1000 | sine |

### Interruptions
- No wrap: Up on the first row / Down on the last stays put (or goes to the ALL row).
- Fast Back-Back from a subfolder never overshoots into the MM (root must show for 0.6 s first).
- A folder change is never treated as a wrap.

### Continuity
- Back returns to the row you came from on every level.
- The big album keeps swaying through every level change; leaving fullscreen returns to the same row.
- After music stops, the last cover stays as the big album until list art takes over.

### Layering
Fanart stage < meta (stage top) < colour strip < list rows / small album < pills (FULLSCREEN, A–Z) < big album layer < MM.

### Geometry
| Piece | Value |
|---|---|
| List | in the strip: layout 450 × 984 at 120, 120, scaled 86.67 % into x 570…960 (+7 nudge to the strip edge); bottom ≈ y 973 (5 px above the double-tap hint at y 978) |
| Small album (L2) | 570, 120, 390 × 390 at the top of the strip |
| Meta | small 150, 196; big 150, 226; pills 150, 296; all 480 wide (x 150–630, 474) |
| FULLSCREEN pill | 140, 136 |
| A–Z bar | left 78, top 151 |
| ALL row | flush under the last row (≤ 14 rows); long lists: bottom pill 576, 972, 378 × 46 |
| Big album | 1140, 220, 600 × 600 |

### Art
- Stage: artist fanart. Small album: the focused album's cover. Big album: playing cover, else the focused item's thumb (next item's for `..`), else the last cover.
- No art → nothing (no default cover, no placeholder).
- Meta pills: outlined pill, uppercase titles.

### Input
| Action | Result |
|---|---|
| Up / Down | move; edges → ALL row if shown, else stay |
| Left | FULLSCREEN pill (if playing) → A–Z bar (if shown) → MM |
| Right | music controls (if playing) |
| Select | open / play in place (no jump to the visualiser) |
| Double Select | Options / Info |
| Back | up a level; at the section root → MM |
| Tab / Display | fullscreen music |

### Speed targets
Rows visible ≤ 0.45 s after entry; Select on a song starts playback at once.

### Never
- No old list-group cover in the stage corner on Albums / Recently played (472 ALBUMHALF; 466 ALBUMCOVER).
- No meta text behind Genres / Years / folder lists (466 GENREMETA).
- No merged single song list for Artists; no view-type options (274).
- No placeholder art (276).
- No list wrap from top to bottom (451 NOWRAPGUARD).
- No ALL row for a single album / disc (443, 444, 451).
- No auto-switch to the visualiser on Select (409).

### Acceptance checks
1. MM → MUSIC → Artists: fanart + meta, rows in the strip, A–Z bar for a long list.
2. Select an artist with 2 albums: small cover on top, two rows, ALL ALBUMS under them.
3. Albums / Recently played: small cover on top, no cover in the stage corner.
4. Genres: rows only.
5. Up on the first artist: stays; Back at Artists: MM.

## Kodi implementation (sandbox)

### How it works
- **Levels:** L1 `musicdb://artists/`; L2 `musicdb://artists/ID/` (native artist albums; `..` and stock *All hidden and pulled up when `musiclibrary.showallitems` is on); L3 `…/ALBUMID/-2/` (or ALL `…/-1/-2/`). Back is native Kodi parent-folder.
- **Half list (`bz_mhalf`)** = `$EXP[bz_mstrip] + [Container.Content(albums) | $EXP[bz_m13]]` (472): 390 strip album above the rows (HALFLIST 280 / HALFALB 296). `bz_covercol` (cover-list mode) for `Window.IsActive(music) + Container.Content(albums) + !bz_artistalbums` (466). `bz_allhalf` (ALL row in half list) still needs `bz_artistalbums`.
- **Strip info card** (`View_60_BezelInfoList`, 9 parts) is alpha 0 for `$EXP[bz_mstrip] | Control.IsVisible(60)` (466).
- **ALL row:** `$EXP[bz_allrow]` + View All Albums (`bz_allalbums`); needs `bz_all2` (`NumItems > 2 | [NumItems == 2 + !bz_allhas]`, Kodi doesn't count `..`). Short lists: 6097 slid under the last row; long lists: pill 6088 (`$EXP[bz_alllong]` focusable, drawn on `$EXP[bz_alllongshow]`). Select `bz_cmd allrow` (opens `-1/`, sort by album, stores `bz_allret`); onup restores `bz_allup`. Label `BzAllRowLabel` + `bz_allcnt` (bz_flip `allcnt` JSON-RPC). ALL list = `$EXP[bz_allgrp]` with album header bars.
- **Navigation:** list 60 in a 450 × 900 clip grouplist that owns onup / ondown (→ 6097 if visible, else edge markers). bz_flip watcher catches Kodi's native wrap only when it really happened (451). onleft: `bz_vback` → close; 6886 visible → 6886; 6100 visible → 6100; else (`bz_navok`) `bz_nav=true`. onright (music): 6160 visible → `ActivateWindow(1115)`, else 6192. onback (first match): `bz_vback` → close; `bz_msret` on `sources://` → 1117; `bz_np` → clear + 6299; MM open → clear nav; `bz_atroot` + navok → MM; else 6299. Root arm: `bz_rootarm` after 0.6 s on a root / `bz_navroot`.
- **Meta:** L1 small "ARTIST", big label; L2 small artist, big album; L3 small artist, big `ListItem.Album`. Pills year + genre.
- **Big album art:** playing `Player.Art(thumb)`; stopped: list 60 thumb (via the 1122 mirror), fallback `bz_cov_last`. Idle A/B `bz_m_idle_a` / `_b` / `_side`, fade `bz_at_midlefade` (400 ms).
- **Select = play in place:** `musicfiles.selectaction` forced off at startup (`bz_dustviz.py`).
- **Random start row** (RANDSTART) on the first MM visit; the session row is kept by mm_warm.
- **LISTTIME:** `BEZEL list …` kodi.log line per folder change (470).

### Wiring
| Item | Value |
|---|---|
| GO | `SetProperty(bz_navroot,musicdb://albums/,home)` + `bz_cmd.py tomusic` |
| Pills | `musicdb://artists/`, `albums/`, `genres/`, `recentlyaddedsongs/`, `recentlyaddedalbums/` |
| Expressions | `bz_mstrip`, `bz_mhalf`, `bz_m13`, `bz_covercol`, `bz_artistalbums`, `bz_allrow`, `bz_all2`, `bz_allhas`, `bz_alllong`, `bz_alllongshow`, `bz_allgrp`, `bz_allhalf`, `bz_atroot`, `bz_navok`, `bz_discbar` |
| Home | `bz_navroot`, `bz_rootarm`, `bz_allup`, `bz_allret`, `bz_allcnt`, `bz_cov_last`, `bz_m_idle_*`, `bz_np_focus`, `bz_np_was` |
| Pill text | `BezelViewName` / `BezelViewPillText` show ALBUM LIST / ALBUMS on `Container.Content(albums)` |

### Kodi workarounds (do not port)
- Pull-up slides for the hidden `..` / *All rows and the 6097 offset tables: Kodi always inserts them.
- 86.67 % scaled list group: the list was moved into the strip without re-laying every row.
- Wrap watcher, root arm, `bz_allup`: Kodi list navigation quirks.
- `bz_all2` count rule: Kodi's `NumItems` excludes `..`.

## Related
[music-fanart-fs](music-fanart-fs.md) · [big-album](big-album.md) · [fullscreen-pill](fullscreen-pill.md) · [dialogue-fs](dialogue-fs.md) · [recently-played](recently-played.md) · [section-transitions](section-transitions.md) · [idle-big-album-fold](idle-big-album-fold.md)
