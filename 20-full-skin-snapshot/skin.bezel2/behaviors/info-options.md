# Options + Info

**Object:** the Info / Options menu for library items · Kodi: `DialogVideoInfo.xml`, `DialogMusicInfo.xml` (grouplist `9000` at 582,166, 360 wide; video cast list `50`), legacy `Custom_1111_XInfo.xml` (closes itself)
**Where:** Movies, TV, Music (and Pictures) items; menu in the strip column, fanart on the left, the poster / big album stays on the right
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
One Bezel menu replaces both Info and the context menu for Movies, TV and Music: Info, Menu / C or a double-Select opens it. It has three pages. **Main**: Play, Play next, Queue, Browse seasons / set, Trailer, More options, Section options. **More**: choose art, refresh, set rating, director, watched, favourites, remove from library. **Section options**: Clearart (Movies: off by default; TV: on by default), Sort by, Watched filter, Update library, Order, Filter, and the extras that apply (party mode, playlist, get more…). Back on a sub-page returns to Main; Back on Main closes. Closing leaves the section exactly as it was.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Main | open | Back → closed; More / Section → page | left fanart crop, title, rows; poster / album on the right |
| More | More options | Back → Main | more rows |
| Section | Section options | Back → Main | section rows (first row focused: Clearart, else Sort by) |
| Cast (video) | Down from the last row | Up | cast list |

### Timeline
| What | Duration |
|---|---|
| open | dialog appears over the section (no pop-in) |
| strip chrome under it | logo / list chrome fade 150 ms |
| close | instant; section fanart was never faded, poster / album never moved |

### Interruptions
Page change moves focus on the next frame (no flash of the old page's focus).

### Continuity
- Every open starts on Main.
- The right-side poster / big album stays during and after (the art mirror holds while Info is up).
- Closing never hides posters (the old View Type row that switched them off is gone).

### Layering
Section < fanart crop (opaque, 120…960) + title < menu rows (strip column) < confirm dialogs. The 1122 art layer stays visible on the right.

### Geometry
| Piece | Value |
|---|---|
| Fanart crop | x 120–960 |
| Title | 150, 150 |
| Rows | 582, 166, 360 wide |
| Cast list | 593, 476, 352 × 108 |

### Art
Left fanart crop of the item; no art of its own on the right.

### Input
| Action | Result |
|---|---|
| Up / Down | move (no wrap; video Down from the last row → cast) |
| Left / Right | close |
| Select | run the row |
| Back | sub-page → Main; Main → close |
| Cast Select | Movies filtered by that actor |

### Speed targets
Opens on the double-Select without delay beyond the tap window.

### Never
- No left black mask over the fanart (205).
- No art flash on exit (395).
- No poster loss after exit (473 VIEWTYPEDEL: View Type removed from video Section options; music lost it in 274).
- No movie clear art unless switched on (473 MOVCLEAR).

### Acceptance checks
1. Movie → double-Select → Main; Section options → Clearart (OFF) focused; Back → Main; Back → closed, poster in place.
2. TV show → Section options → Clearart ON → OFF → logo becomes the title.
3. Remove from library → confirm → removed.

## Kodi implementation (sandbox)

### How it works
- Routing: `bz_dtap.info()` → `Action(Info)` for library windows ([context-menu](context-menu.md)).
- `onload ClearProperty(bz_ci_more)`; defaultcontrol `always` 8 (Play). Pages by Window prop `bz_ci_more`: empty = Main, `1` = More, `sec` = Section. 9980 "Section options ›" (video: on Main; music: inside More): `SetProperty(bz_ci_more,sec)` + focus by 0 s alarm — video: 9969 (TV), 9967 (movie / set), else 9971; music: 9971.
- Section rows (video): 9969 Clearart TV (`bz_tvclear_off`), 9967 Clearart Movies (`bz_movclear_on`), 9971 Sort, 9972 Watched filter, 9973 Update library, 9989 Order, 9981 Filter, 9982 Party mode (music videos), 9983 Master mode (locks), 9984 Go to playlist, 9985 Get more (add-ons) …; music adds Visualizer 9974.
- Every sub-page row onback: `ClearProperty(bz_ci_more)` + `AlarmClock(bzci_back,SetFocus(9980))`.
- Art: `bz_flip.v60_mirror` returns early while `movieinformation | musicinformation | songinformation` is visible; `bz_railvis` keeps the album in Music. Section fanart has no `bz_infoup` fade (395); logo / list chrome fade 150 ms on `bz_infoup`.
- Remove from library → `bz_ctx.py remove` → confirm.
- 1111: `onload Dialog.Close(1111,true)`, `onunload` clears `bz_xinfo`.

### Wiring
| Item | Value |
|---|---|
| Window prop | `bz_ci_more` |
| Expression | `bz_infoup` |
| Skin | `bz_tvclear_off`, `bz_movclear_on` |
| Variables | `BzTVClearOnOff`, `BzMovClearOnOff` |
| Row include | `BzCIBtn` |

### Kodi workarounds (do not port)
- Kodi's info dialog reused as a menu (pages by property, focus by 0 s alarm).
- The art mirror freeze: list 60 can't be read from a dialog.
- Rows that `SendClick` Kodi's hidden window buttons (filter, party mode…).

## Related
[context-menu](context-menu.md) · [movies-list](movies-list.md) · [tv-list](tv-list.md) · [music-list](music-list.md) · [dialog-confirm](dialog-confirm.md) · [favourites](favourites.md)
