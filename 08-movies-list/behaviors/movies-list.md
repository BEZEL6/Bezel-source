# Movies list

**Object:** the Movies section · Kodi: `MyVideoNav.xml`, list `60` (strip list), A–Z bar `6500`, VSTRIP META group (Includes_Bezel), poster layer in 1122 (see [artwork-group](artwork-group.md))
**Where:** Movies: fanart stage left with meta and plot, list in the colour strip, swaying poster on the right
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Movies opens on Titles (or Recently added / Years from the MM pill). The list sits in the colour strip; the focused movie's fanart fills the stage with its title (or its clear logo if you turn Movies clear art on), the info pills (year, MPAA, runtime; genre on its own row) and the plot; its poster sways on the right. Folder lists (years, genres, sets, actors) show the folder name as the title. Long lists have an A–Z bar. Double-Select opens Info / Options, where Section options holds the Movies Clearart switch (off by default).

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Titles / Recently added | MM MOVIES (pills) | Select → plays / info; Back → MM | strip list, stage fanart + meta + plot, poster |
| Folder list (Years, Sets, Genres, Actors) | pill / Select | Select → titles; Back | folder name as title; no pills unless present |
| Clear art on | Section options › Clearart ON | OFF | movie clear logo (else clear art) instead of the title |
| Info | double Select | Back | info / options dialog over the list |

### Timeline
| What | Duration | Curve |
|---|---|---|
| section entry | 400 fade-in, rows after 350 | sine out |
| meta group appears | 300 fade | sine |
| clear logo / title change | 200 image fade | — |
| poster change | preload ≥ 600, then 1000 crossfade | sine |
| fanart change | 150 | — |
| row scroll / cascade | 271 cubic / 286 + 30 stagger | — |

### Interruptions
- Fast scrolling: poster and fanart only change once the focus settles and the new art is decoded.
- Opening Info and closing it: poster and art stay exactly as they were.

### Continuity
- Movies and TV each keep their last poster, so MM row switches between them are instant.
- Back returns to the same row; the MM shows the same art.

### Layering
Fanart stage < meta + plot < colour strip + list < A–Z bar < poster layer (1122) < MM / dialogs.

### Geometry
| Piece | Value |
|---|---|
| Title / clear logo box | 150, 120, 410 × 176, centred (stage top to the pills) |
| Pills row 1 | y 296, width 410: YEAR · MPAA · RUNTIME |
| Pills row 2 | y 336: GENRE (truncates at 410) |
| Plot | from y 386 |
| List | strip x 570–960 (see [music-list](music-list.md) for the scaled list rule) |
| A–Z bar | 78, 151 |
| Poster | big album column (x 1140), sway axis 1290 |

### Art
- Fanart: movie fanart. Poster: movie poster (set: set poster). Clear logo (preferred) or clear art only when Movies clear art is on.
- No art → title text; no placeholder.

### Input
| Action | Result |
|---|---|
| Up / Down | move, no wrap |
| Left | A–Z bar (if shown) → MM |
| Select | play / open folder |
| Double Select | Info / Options |
| Back | up a level / MM |
| Long-press on the poster (touch) | extended info |

### Speed targets
Rows ≤ 0.45 s after entry; poster ≤ 0.6 s after focus settles.

### Never
- No clear logo by default (473 MOVCLEAR: Rob "disable clear art for movies section by default").
- No director label above the title (418).
- No poster hold / stand-in posters (152).
- No poster gone after closing Info (473 VIEWTYPEDEL: the dead View Type option removed).
- No dip to black between Movies and Music / TV (392, 413, 430, 431).

### Acceptance checks
1. MM → MOVIES: strip list, title (not logo), pills, plot, poster swaying.
2. Info › Section options › Clearart → ON: logos show; OFF: titles.
3. Open Info, close: poster still there.
4. Years → a year → titles; Back → years list.

## Kodi implementation (sandbox)

### How it works
- **Open:** `SetProperty(bz_navroot,videodb://movies/titles/,home)` + `bz_cmd.py go` → section transition ([section-transitions](section-transitions.md)). Pills (`bz_mm.py SUBS`): `videodb://movies/titles/`, `recentlyaddedmovies/`, `movies/years/` (stored pills 4–6 fall back to Titles).
- **Strip list (`bz_vstrip`)** for `Container.Content(movies)` lists on every pill path; folder names via `bz_vfold` ⊂ `bz_vstrip`. Old strip info pairs / plot faded off while `bz_vstrip`.
- **VSTRIP META** (Includes_Bezel): visible `$EXP[bz_vstrip] + !$EXP[bz_infoup] + !$EXP[bz_navmenu] + !ListItem.IsParentFolder`, 300 ms fade. Movies clear logo image (`$VAR[BzVStripLogo]`: clearlogo else clearart) needs `Container.Content(movies) + Skin.HasSetting(bz_movclear_on)`; the centred title label shows otherwise (folders keep their old rule).
- **Section options toggle:** DialogVideoInfo 9967 Clearart (`ListItem.DBType` movie / set) → `Skin.ToggleSetting(bz_movclear_on)`, label2 `$VAR[BzMovClearOnOff]`.
- **Poster:** 1122 layer 6401 from `v60_mirror` (`bz_v60_art`, `bz_vpl_on`, holds `bz_v60_mov` / `bz_v60_tv`). The mirror holds while Info is visible.
- **Navigation / ALL / A–Z / Back rules:** as Music ([music-list](music-list.md)); no ALL row for movies.

### Wiring
| Item | Value |
|---|---|
| Expressions | `bz_vstrip`, `bz_vfold`, `bz_infoup`, `bz_navmenu`, `bz_navok`, `bz_atroot` |
| Skin | `bz_movclear_on` (default unset = off) |
| Variables | `BzVStripLogo`, `BzMovClearOnOff` |
| Home | `bz_navroot`, `bz_v60_*`, `bz_vpl_on` |

### Kodi workarounds (do not port)
Same as the Music list (scaled list group, wrap watcher, root arm, art mirror).

## Related
[tv-list](tv-list.md) · [artwork-group](artwork-group.md) · [info-options](info-options.md) · [section-transitions](section-transitions.md) · [mm-warm](mm-warm.md)
