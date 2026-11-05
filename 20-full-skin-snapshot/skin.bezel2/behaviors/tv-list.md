# TV list

**Object:** the TV section · Kodi: `MyVideoNav.xml`, list `60` (strip list), ALL row `6098` / long-list pill `6089`, A–Z bar `6500`, VSTRIP META group, strip clear art (`BzTVClear`), poster layer in 1122
**Where:** TV: fanart stage left with logo, meta and plot; list in the colour strip; swaying poster on the right
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
TV has Shows → Seasons → Episodes, all in the strip-list look. The show's clear logo sits at the top of the stage on every level (the show title if there's no logo, or if you switch TV clear art off in Info › Section options; it's on by default), with pills underneath (S×E, year, studio, MPAA, runtime; genre on its own row), the season / episode name and the plot. Opening a show lands on its first season, never on `..`. An **ALL SEASONS** row opens every episode when a show has two or more seasons. The poster sways on the right.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| L1 Shows | MM TV (pills Shows · Watching · Years · Actors · Recent · Genres) | Select → L2; Back → MM | show rows; logo or title; pills; plot |
| L2 Seasons | Select a show | Select → L3; Back → L1 | season rows starting at Season 1; ALL SEASONS under the last (2+ seasons) |
| L3 Episodes | Select a season / ALL SEASONS | Back → L2 | episode rows; S×E pill; episode name; plot |
| Recent episodes | MM pill Recent | Back | episode strip list |
| Clear art off | Section options › Clearart OFF | ON | show title instead of the logo |

### Timeline
| What | Duration | Curve |
|---|---|---|
| section entry | 400 fade-in, rows after 350 | sine out |
| logo change (MM closed) | 300 image fade | — |
| logo change (MM open) | settle 250 → load ≤ 500 → 1500 crossfade | sine in-out |
| poster / fanart | as Movies | — |

### Interruptions
Up from Season 1 goes to ALL SEASONS (or stays); the hidden `..` is skipped.

### Continuity
The show's logo carries from L1 through L3 (show logo used for seasons and episodes).

### Layering
Fanart stage < logo / meta / plot < strip + list < poster layer < MM.

### Geometry
| Piece | Value |
|---|---|
| Logo / title box | 150, 120, 410 × 176, centred |
| Pills | row 1 y 296 (S×E · YEAR · STUDIO max 200 · MPAA · RUNTIME), row 2 y 336 (GENRE) |
| Season / episode name | 150, 382 |
| Plot | from y 386 (L1) / below the name (L2–L3) |
| ALL row | under the last row (≤ 14 rows); long lists: pill 576, 972, 378 × 46 |

### Art
Logo: item clear logo → show clear logo → clear art → show clear art. Poster: show / season poster. No art → title.

### Input
As Movies; Up from the first season → ALL SEASONS.

### Speed targets
As Movies.

### Never
- No `..` drawn above the strip on seasons (338).
- No watched badge drawn in the big album group (323).
- No ALL SEASONS for a single season (443).
- No old info pairs / plot over the episode list (343).

### Acceptance checks
1. TV → a show: lands on Season 1; logo stays; Up → ALL SEASONS.
2. Info › Section options › Clearart OFF → titles; ON → logos (default).
3. Recent episodes: S×E pill, episode name, plot.

## Kodi implementation (sandbox)

### How it works
- **Open:** `bz_navroot=videodb://tvshows/titles/` + `bz_cmd.py go`.
- **Strip list:** `bz_vstrip` covers tvshows / seasons / episodes under `videodb://tvshows/titles/`, recent episodes, and every pill path once the list holds titles; folder names via `bz_vfold`.
- **Logo (stage):** `$VAR[BzTVClear]` image, visible with any of the four art fields + `!Skin.HasSetting(bz_tvclear_off) + !Container.Content(movies)`; title `BzTVShowName` otherwise.
- **Logo (strip, MM open):** A/B lane `bz_clr_a/b`, `bz_clr_side`, `bz_clr_on`, `bz_clr_empty` from `bz_flip._ab_clear` (TV content in Videos only, not on virtual rows, off with `bz_tvclear_off`).
- **Toggle:** DialogVideoInfo Section options 9969 Clearart (DBType tvshow / season / episode) → `Skin.ToggleSetting(bz_tvclear_off)`, label2 `BzTVClearOnOff`.
- **Seasons:** bz_flip `Control.Move(60,1)` when a seasons folder opens on the parent item; layouts hide `..` on seasons when `videolibrary.showallitems` is on (342).
- **ALL SEASONS:** `bz_allseasons` + `$EXP[bz_allrow]` / `bz_all2`; long-list pill 6089; count `bz_allcnt` (VideoLibrary.GetEpisodes); opens the plain episode list.

### Wiring
| Item | Value |
|---|---|
| Skin | `bz_tvclear_off` (default unset = on), `bz_allseasons` |
| Variables | `BzTVClear`, `BzTVShowName`, `BzTVClearOnOff`, `BzAllRowLabel` |
| Home | `bz_clr_*`, `bz_allcnt`, `bz_v60_tv` |

### Kodi workarounds (do not port)
`Control.Move` past `..`, pull-up slides for hidden rows, the clear-art A/B lane under the MM.

## Related
[movies-list](movies-list.md) · [artwork-group](artwork-group.md) · [info-options](info-options.md) · [mm-warm](mm-warm.md)
