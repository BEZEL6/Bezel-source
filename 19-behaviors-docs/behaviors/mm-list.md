# MM list (Main Menu strip)

**Object:** Main Menu strip list `6996` (Includes_Bezel) · `scripts/bz_mm.py` · chrome `BezelMMStripChrome` (line ~2318)  
**Where:** Colour strip under `$EXP[bz_navmenu]` (`String.IsEqual(Window(Home).Property(bz_nav),true)`)  
**Last updated:** 2026-11-01 · 5.33.217  
**Status:** approved. The live tree matches (re-verified 5.33.207). Warm underlay behavior is LOCKED in mm-warm.md.  
**Skin:** skin.bezel2 (Estuary fork)

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.

**How it works.** Opening just sets Home `bz_nav=true`. The strip, the dim and the warm underlay all follow `$EXP[bz_navmenu]`. Section lists use `$EXP[bz_navok]` before opening, so the menu cannot reopen during a nav lock or grace window. While the menu is open, the focus bounces send any focus that lands on list 60 back to 6996, unless a pick is in progress (`bz_mmpick`). The underlay stays warm behind the strip (mm-warm.md, LOCKED).

**Wiring.**
- `bz_navok` = empty `bz_navlock` + empty `bz_navgrace` + `bz_nav` not true (Includes_Bezel line ~366).
- `BezelMMFocusBounce` / `BezelMMFocusBounceList` (the List variant also checks `bz_mmwarm`): `onfocus SetFocus(6996)` when navmenu is open and `bz_mmpick≠true`.
- Visible: `$EXP[bz_navmenu] + !Window.IsVisible(1118) + bz_navtune≠true + bz_navbez≠true`. No `allowhiddenfocus` (5.33.190).
- Anim: Visible slide -390→0 over 210 ms cubic out (when `bz_pwrswap` is empty). Hidden slide 0→390 over 180 ms cubic in (when not 1118 and `bz_pwrswap` is empty, "K48 no slide-out when POWER opens"). Slides 0,120 while `Player.HasMedia`, to make room for the mini-player.
- Geometry: left 0, top 40, 390×728, `scrolltime` 150.
- `onback`: restore `bz_mmsub_*` from Skin.String, clear `bz_nav` / `bz_navtune` / `bz_navbez`, focus 60.

## Rows (top → bottom)

**Simple.** MUSIC · MOVIES · TV SHOWS · RECENTLY PLAYED · FAVOURITES · SEARCH · PICTURES · ADD-ONS · SETTINGS · MEDIA SOURCES · POWER

**Wiring.** 11 items, index 0–10, each with `ListItem.Property(sec)`.
| Row | sec | Select |
|---|---|---|
| MUSIC / MOVIES / TV SHOWS | music / movies / tv | `bz_mm.py,<sec>` → primed pill sub |
| RECENTLY PLAYED | recent | `bz_mm.py` → `bz_navroot` + `bz_cmd.py tomusic/go` |
| FAVOURITES | fav | `ActivateWindow(Favourites)` |
| SEARCH | search | window 1107 |
| PICTURES | pictures | `pictures` |
| ADD-ONS | addons (`div=1` divider line) | `addonbrowser` |
| SETTINGS | settings | `Settings` |
| MEDIA SOURCES | mediasources | clear nav/navtune/navbez → `ActivateWindow(1117)` |
| POWER | power | `ActivateWindow(1118)` |

Every non-library GO entry first runs `ClearProperty(bz_nav)`. `bz_mm.py` drops a repeat Select within 300 ms (`MMLOCK_S=0.30`). Before GO it runs `store()` (`Skin.String(bz_lastart_<sec>)`), sets `bz_mmpick=true` and closes 1112 if open.

## Keys

**Simple.** Up and Down move through the rows. Down from the last row wraps to MUSIC. Up from MUSIC goes to the mini-player when something plays. Left and Right on MUSIC/MOVIES/TV change the primed pill.

**Wiring.**
| Key | Behavior |
|-----|----------|
| Down (last) | `SetFocus(6996,0,absolute)`, wraps to MUSIC |
| Up (first) | video → `6966`; audio → `6958`; nothing → `SetFocus(6996,12,absolute)` |
| Select | open (table above) |
| Back | close MM → list 60 |
| Right / Left on MUSIC / MOVIES / TV | pill forward / back (chip only, does **not** enter the list) |
| Left / Right on SETTINGS and other rows | *none* (Select only) |

**Unverified:** with nothing playing, Up targets absolute index **12**, but the list has only 11 items (0–10). It presumably clamps to POWER (index 10). I did not check this on device.

## Primed pills (wrap)

**Simple.**
| Section | Order |
|---------|--------|
| MUSIC | ARTISTS → ALBUMS → GENRES → RECENT SONGS → RECENT ALBUMS |
| MOVIES | TITLES → RECENTLY ADDED → YEARS (5.33.398: Actors/Sets/Genres deleted) |
| TV | SHOWS → WATCHING → YEARS → ACTORS → RECENT → GENRES |

The last choice is remembered across sessions. On a cold start the pills reset to index 1 (Artists / Titles / Shows, t5012).

**How it works.** Left/Right write the new index to both Home `bz_mmsub_<key>` (live chip) and `Skin.String(bz_last_mmsub_<key>)` (persisted). Select calls `subgo()`, which uses the explicit 1-based index. For music without an explicit pill it clears `bz_music_underlay` and uses `bz_lastmusic`. `restore()` and `bz_cmd.py start` rebuild the Home props from Skin.String after ReloadSkin.

**Wiring.**
- `onleft`/`onright` gated on `ListItem.Property(sec)` = music/movies/tv, using `$VAR[BzMMPrev_*]` / `$VAR[BzMMNext_*]` (Includes_Bezel ~465–470). Empty or 1: Prev → 5 (music) / 6 (movies, tv). Next → 2.
- `SUBS` paths: music `artists, albums, genres, recentlyaddedsongs, recentlyaddedalbums` · movies `titles, recentlyaddedmovies, years` (stored pill >3 clamps to Titles) · tv `titles, inprogresstvshows, years, actors, recentlyaddedepisodes, genres`.

## Pill UI and strip chrome

**Wiring.**
- Focused row: `BezelMMRowBar` with "›" on music/movies/tv. SETTINGS gets a flat bar with a plain label. Labels `$VAR[BzMMSubLbl]` / `$VAR[BzMMSubDots]`.
- `BezelMMStripChrome`: w 390, w2 470. Soft cast `bezel/mm_strip_shadow_c.png` at **left=-47**, top=-36, width w2 (470). The dark contact sits on the colour-strip left edge.

## Related
mm-warm.md (LOCKED) · mm-mini-player.md · music-list.md · movies-list.md · tv-list.md · media-sources.md

## Kodi FS from MM (5.33.378)
Leaving Fanart FS / 1121 / NP opened while MM was open returns to MM (`bz_fsmm` latch), not the section list. Video FS not covered (video playback starts from a section).

## Quick-tap ignore (current, 5.33.386)
- **Whole strip:** any Select / Back / Left / Right on 6996 runs once, then sets Home `bz_mmtap`. All 6996 actions are conditioned on `String.IsEmpty(bz_mmtap)`, so a second press within **400 ms** does nothing. `bz_flip.py mm_tap()` clears the latch 400 ms after it appears (50 ms poll). Up/Down are not latched (fast scrolling stays free).
- Scope: strip only. Once Back/Select hands focus to list 60 / another window, that target is not latched.

**No MM auto-hide (5.33.398 NOAUTOHIDE, Rob t2799u):** the strip 6996 / group 6894 stays visible and focusable the whole time MM is open. There is no idle fade, no park button 6897, no `bz_mmidle`, no idle label / clearart stage, no wake path (WAKEGRACE/IDLEPARK/IDLERESET), and no Tuner Auto-hide row. mmdim and the colour backdrop follow plain MM-open rules. MMHOLD on MM open is unchanged.
