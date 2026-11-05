# Main menu (MM) strip

**Object:** the main menu · Kodi: list `6996` (Includes_Bezel, `BezelNavMenu`), chrome `BezelMMStripChrome`, `scripts/bz_mm.py`, Home `bz_nav`
**Where:** in the colour strip (x 660, 390 wide), over the current section
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live (approved) · **Lock:** the art behind the MM is LOCKED ([mm-warm](mm-warm.md))

## Simple
Left or Back at the top of a section list (or M) opens the main menu inside the colour strip: MUSIC, MOVIES, TV SHOWS, RECENTLY PLAYED, FAVOURITES, SEARCH, PICTURES, ADD-ONS, SETTINGS, MEDIA SOURCES, POWER. Behind it the screen shows the art of the row you're on, so moving between rows previews each section. Left / Right on MUSIC, MOVIES and TV choose which list opens (the "pill": Artists, Albums …), remembered across sessions. Select opens it; Back closes the menu. A second press within 0.4 s is ignored, so a fast double tap never opens two things.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Closed | — | Left / Back at a list top, M | section |
| Open | as above | Back; Select a row | strip chrome + rows; art of the focused row behind |
| Pill changed | Left / Right on MUSIC / MOVIES / TV | — | the row's chip shows the new list name + dots |
| Picking | Select | destination opens | MM stays until the destination fades in |
| Mini player | Up from MUSIC while playing | Down | focus on the mini player above the rows |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| open | strip chrome fades in (no slide); art lanes already at 100 % | 286 | sine out |
| close | chrome fades out | 250 | sine in |
| row change | the art behind crossfades (warm system) | 500 / 1500 (see mm-warm) | sine in-out |
| row scroll | focus bar moves | 150 | — |
| mini player shown | rows shift down 120 px | 0 (instant) | — |

### Interruptions
- A second Select / Back / Left / Right within 400 ms: ignored. Up / Down are never blocked.
- Select during a running warm swap: opens the destination; the art keeps fading as is.
- A destination that needs loading keeps the MM drawn until it fades in ([section-transitions](section-transitions.md)).

### Continuity
- The menu reopens on the row of the section you are in (Recently played → row RECENTLY PLAYED; Media sources → row MEDIA SOURCES).
- The pill choice per section is remembered; cold start resets the pills to the first list.
- Fullscreen music opened from the MM returns to the MM.

### Layering
Section (+ art lanes) < MM dim < strip chrome < rows / focus bar < mini player < dialogs.

### Geometry
| Piece | Value |
|---|---|
| Strip | x 660, 390 wide; list top 40 (in the strip), 728 tall |
| Mini player shift | rows +120 px down while media plays |

### Art
Rows: label in caps; focused row = bar with "›" on MUSIC / MOVIES / TV and the pill label + dots; SETTINGS = flat bar. Divider line above ADD-ONS.

### Input
| Action | Result |
|---|---|
| Up / Down | move; Down on the last row wraps to MUSIC; Up on MUSIC → mini player (video / audio) or POWER |
| Left / Right on MUSIC / MOVIES / TV | previous / next pill (chip only) |
| Select | open the row |
| Back | close → section list |
| 5 s idle on a header pill | focus back to where it came from |

### Speed targets
Open / close ≤ 300 ms; destination fade within ≤ 0.6 s.

### Never
- No MM slide (469 "disable the mm menu slide").
- No MM auto-hide / idle fade (398 "old system was glitchy and broken").
- No dip to black or 1.5 s wait on open (430, 431, 458 → 460).
- No hitch or flash while moving rows (426).
- No sway restart when moving between Music and Movies / TV (314).

### Acceptance checks
1. Movies list top → Left → menu fades in, poster unchanged behind.
2. Down through every row: background previews each section, no flash; last row wraps to MUSIC.
3. MUSIC Right × 2 → ALBUMS chip; Select → Albums list.
4. Double-tap Select fast: opens once.
5. Restart the app: pills back to the first list.

## Kodi implementation (sandbox)

### How it works
- **Open** = Home `bz_nav=true`; strip, dim and underlay follow `$EXP[bz_navmenu]`. Sections check `$EXP[bz_navok]` (`bz_navlock` / `bz_navgrace` empty, `bz_nav` not true) first. While open, focus landing on list 60 bounces to 6996 unless `bz_mmpick`.
- **Visible:** `$EXP[bz_navmenu] + !Window.IsVisible(1118) + bz_navtune ≠ true + bz_navbez ≠ true`. Chrome fades: `BezelATMenuAnim` (Tuner menu open / close, baked).
- **Select.** `bz_mm.py <sec>` (`MMLOCK_S = 0.30` repeat guard): `store()` (`Skin.String(bz_lastart_<sec>)`), `bz_mmpick=true`, then `subgo()` with the 1-based pill index (music without a pill uses `bz_lastmusic`, clears `bz_music_underlay`) → `bz_cmd.py tomusic` / `go`. Other rows: clear `bz_nav` then `ActivateWindow(Favourites / 1107 / pictures / addonbrowser / Settings / 1117 / 1118)`; Settings kids set `bz_setopen` first.
- **Quick-tap latch.** Every 6996 Select / Back / Left / Right is conditioned on empty `bz_mmtap` and sets it; `bz_flip.py mm_tap()` clears it after 400 ms.
- **Pills.** Left / Right write Home `bz_mmsub_<key>` and `Skin.String(bz_last_mmsub_<key>)`; `$VAR[BzMMPrev_*]` / `$VAR[BzMMNext_*]`; `restore()` / `bz_cmd.py start` rebuild after a reload. Lists: MUSIC Artists · Albums · Genres · Recent songs · Recent albums; MOVIES Titles · Recently added · Years; TV Shows · Watching · Years · Actors · Recent · Genres.
- **onback:** restore `bz_mmsub_*` from Skin.String, clear `bz_nav` / `bz_navtune` / `bz_navbez`, focus 60.
- **Reopen row map:** SetFocus map {6902:1, 6903:2, 6905:3, 6904:3, 6908:8, 6919:9, 6909:10, 6920:9}; Recently played path → row 3; media sources via the msret latch.
- **From fullscreen:** `bz_fsmm` latch → bz_flip reopens the MM when fullscreen closes.
- **Pill idle:** `_pill_idle` covers MM header pills 6958–6961 / 6910 only while `bz_nav` and no `bz_navsub`.

### Wiring
| Row | sec | Select |
|---|---|---|
| MUSIC / MOVIES / TV SHOWS | music / movies / tv | `bz_mm.py,<sec>` → pill list |
| RECENTLY PLAYED | recent | `bz_navroot` + `bz_cmd.py tomusic/go` |
| FAVOURITES | fav | `ActivateWindow(Favourites)` |
| SEARCH | search | 1107 |
| PICTURES | pictures | `pictures` |
| ADD-ONS | addons (`div=1`) | `addonbrowser` |
| SETTINGS | settings | `Settings` (via 1130) |
| MEDIA SOURCES | mediasources | clear nav props → `ActivateWindow(1117)` |
| POWER | power | `ActivateWindow(1118)` |
| Up (first row) | `Player.HasVideo` → 6966; `$EXP[bz_mpup]` → 6958; else `SetFocus(6996,12,absolute)` (clamps to POWER) |
| Down (last row) | `SetFocus(6996,0,absolute)` |
| Geometry | left 0 / top 40 in the strip, `bz_strip_w` × 728; slide 0,120 (time 0) on `$EXP[bz_mpup]` |
| Home | `bz_nav`, `bz_navlock`, `bz_navgrace`, `bz_mmpick`, `bz_mmtap`, `bz_mmsub_*`, `bz_fsmm`, `bz_setopen` |

### Kodi workarounds (do not port)
- Focus bounce from list 60 while the menu is open: Kodi keeps the section's list focusable underneath.
- The 400 ms `bz_mmtap` latch and the 300 ms script lock: Kodi queues repeated remote presses.
- `SetFocus(6996,12,absolute)`: relies on Kodi clamping.

## Related
[mm-warm](mm-warm.md) · [mm-mini-player](mm-mini-player.md) · [section-transitions](section-transitions.md) · [music-list](music-list.md) · [movies-list](movies-list.md) · [tv-list](tv-list.md) · [media-sources](media-sources.md) · [power-menu](power-menu.md)
