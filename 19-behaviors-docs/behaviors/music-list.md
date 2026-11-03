# Music section list

**Object:** `MyMusicNav.xml` · list `60` · grouplist (Includes_Bezel ~L1492) · ALL `6097` · A–Z `6100`/`6500` · album rails `6367`/`6377`/`6397`/`6382` · NP proxy `6385`
**Where:** Main menu MUSIC (and the music pills) → music window
**Last updated:** 2026-11-02 · 5.33.384
**Status:** Live in 5.33.275. Edge-to-ALL with no wrap. Left opens the MM when the A–Z bar is hidden, and Back at the armed root opens the MM (clearing NP first). The big album and compact NP share album grouplist 6397, and the speed rail follows `bz_at_fsslide`. Tap big album → Dialogue FS 1120. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

## 3-level Music (5.33.274 MOCK on live tree — not Rob-approved yet)

### Simple
Artists → Albums → Songs, three separate native lists. The old merged "all songs with album headers" list is gone. Music has one view only: no Album View (A/D) and no View Type (grid / album-list / cover-column) choices in options.

### How it works
- **L1 Artists** `musicdb://artists/`: full-height list 60, 3B artist strip, big album 600×600 at 1140,220 (`bz_nojumbo` — never jumbo; no white panel frame).
- **L2 Albums** `musicdb://artists/ID/`: Select an artist → native Kodi artist albums. Regular 60px list (no cover column: `bz_covercol` excludes `bz_artistalbums`). Parent `..` and stock *All are blanked and pulled away (`bz_allpull120`); **ALL ALBUMS** (6097) sits directly under the last album row (`bz_allpick` = multi-disc picker only, so no cover-column slides). 3B album strip + big album 600×600.
- **L3 Songs** `musicdb://artists/ID/ALBUMID/-2/` (or ALL ALBUMS `…/-1/-2/`): regular 60px song list, no title / album header bar above (`bz_m13` 75px layouts parked with condition `false`; `bz_discbar` excludes `bz_m13`). `..` is the top row. 3B = focused song (small art kept) + big album.
- Back steps L3 → L2 → L1 natively. No Python path hop (5.33.270 `artists/ID/ → /-1/` hop removed in bz_flip.py).
- Old view bools `bz_albview_a` and `bz_grid_music` are reset once at bz_flip start; their option buttons (DialogMusicInfo 9978 Album View, 9979 View Type) and the dead 6880 view-pill music cycle are removed. Section options now opens on Sort By (9971).
- Shared fold / sway / NP / MM warm / strip unchanged. Leaf-fold changes (while-play, FS stubs, warm 5s, random 10s) are separate later work.

### Known (mock)
- (none for L2/L3 layout as of 5.33.275)

---

## Open

### Simple
MUSIC on the main menu (or one of its pills) opens the music library behind the menu, then fades it in.

### How it works
1. The MM row sets `bz_navroot` to `musicdb://albums/` and runs `bz_cmd.py tomusic`.
2. If Now Playing 1112 is open, it's closed first.
3. The music window loads hidden (`bz_secload`, 3 s cap), then the MM closes and the section fades in (`bz_secfade`, 400 ms).
4. While the MM is open, the list chrome hides, the strip 6996 owns focus, and the warm underlay is `musicdb://artists/`.

See mm-warm.md → Section enter / exit. Pills: ARTISTS → ALBUMS → GENRES → RECENT SONGS → RECENT ALBUMS.

### Wiring
| Item | Value |
|---|---|
| GO | `SetProperty(bz_navroot,musicdb://albums/,home)` · `RunScript(bz_cmd.py,tomusic,musicdb://albums/)` |
| SUBS | `musicdb://artists/`, `albums/`, `genres/`, `recentlyaddedsongs/`, `recentlyaddedalbums/` |
| onload | `bz_np_focus` → `SetFocus(6390)` · onunload saves `bz_np_was` |

---

## List 60 navigation

### Simple
- **Up / Down** move through the list. At the top or bottom edge, focus jumps to the **ALL** row if it's showing. Otherwise it stays put and doesn't wrap around to the far end.
- **Left** opens the main menu whenever the A–Z bar isn't on screen.
- **Back** steps out of folders, and at the section's home level it opens the main menu.

### How it works
- **Edges and wrap:**
  - List 60 sits inside a vertical grouplist that's 450×900 with a true clip. The grouplist owns onup/ondown, because Kodi overwrites a single child's nav.
  - At an edge, the grouplist sends focus to ALL `6097` when that row is visible. Otherwise it only writes the marker props `bz_topedge` / `bz_bottomedge`; no script reads them.
  - Kodi's native wrap is caught by `bz_flip.py`. When a poll sees the list jump from the top row to the bottom, it focuses ALL if that's shown, or snaps back to the top row (`SetFocus(60,0,absolute)`).
  - A folder change (open/Back) is never counted as a wrap.
- **Left:**
  1. `bz_vback` set (video back-face) → `bz_vback_close`.
  2. Otherwise, if `!Control.IsVisible(6500)` + `!Control.IsVisible(6100)` and `$EXP[bz_navok]` → `bz_nav=true` (MM).
- **Right:** `bz_vback` → 6291. If the grid entry 6600 is visible → `bz_cmd gridenter`.
- **Back, first match wins:**
  1. `bz_vback` → close the back-face.
  2. `bz_msret=1` on `sources://` → `ActivateWindow(1117)`.
  3. `bz_np` → clear `bz_np` + 6299
  4. MM open → clear `bz_nav`/`bz_navtune`/`bz_navbez`.
  5. `bz_atroot` + navok → `bz_nav=true`.
  - Otherwise → 6299, which is Kodi's normal parent-folder Back.
- **Root arm:**
  - `bz_atroot` needs `bz_rootarm`. `bz_flip` sets that once the folder has shown for 0.6 s and is one of the section ROOTS, or equals `bz_navroot` (which also sets `bz_atnavroot`).
  - So a fast Back-Back from a subfolder doesn't overshoot into the MM.
  - `$EXP[bz_navok]` = `bz_navlock` empty + `bz_navgrace` empty + `bz_nav`≠true.

### Wiring
| Handler | Value (MyMusicNav.xml, Includes_Bezel ~L1492–1505) |
|---|---|
| grouplist onup | `Control.IsVisible(6097)` → 6097 · else `SetProperty(bz_topedge,1,home)` |
| grouplist ondown | `Control.IsVisible(6097)` → 6097 · else `SetProperty(bz_bottomedge,1,home)` |
| onleft | `bz_vback` → `bz_vback_close` · `!Control.IsVisible(6500)` + `!Control.IsVisible(6100)` + `$EXP[bz_navok]` → `SetProperty(bz_nav,true,home)` |
| onright | `bz_vback` → 6291 · 6600 visible → `RunScript(bz_cmd.py,gridenter)` |
| onright (music) | after the above: 6160 visible → `ActivateWindow(1115)` · else 6192 if visible and `!$EXP[bz_artbtn]` |
| onback | order above; fallback 6299 |
| Wrap catch | `bz_flip.py` ~L333–345 (`sw_top` / `sw_prev`; 0.8 s after a folder change) |
| Root arm | `bz_flip.py` ~L711 `bz_rootarm` · `bz_atroot` Includes_Bezel ~L2323 |

---

## ALL row (6097)

### Simple
At the bottom of an album, season, or disc list there's an **ALL** row that opens everything at once. Up from it goes back to where you were.

### How it works
- `6097` is shown by `$EXP[bz_allrow]` when the MM is closed (and not in cover-column mode). It slides down by NumItems×60 so it sits under the last row.
- Select runs `bz_cmd allrow`. That opens the stock "All" node (`<path>-1/`), keeps the query, and stores `bz_allret` so Back from All lands on the ALL row.
- When `bz_flip` sends focus here after a wrap, it stores `bz_allup`, the row count. ALL's onup then restores that row with `SetFocus(60,n,absolute)`.
- Artist-album lists hide the parent `..`, so Up off the first album goes to ALL ALBUMS.

### Wiring
| Handler | Value |
|---|---|
| visible | `$EXP[bz_allrow] + !$EXP[bz_navmenu]` + covercol condition |
| onup | `bz_allup` set → `SetFocus(60,$INFO[Window(Home).Property(bz_allup)],absolute)` · else 60 |
| ondown | noop |
| onleft | `$EXP[bz_navok]` → `bz_nav=true` · else 6996 |
| onclick | `RunScript(bz_cmd.py,allrow)` |
| onback | 60 |

---

## A–Z jump bar

### Simple
For long lists, a strip of letters on the left lets you jump by letter. It's letters only, with no dark band behind it. While it's showing, Left uses the bar instead of opening the menu.

### How it works
- Grouplists `6100` (Music artists/songs, only when NumItems > 38) and `6500` (Movies/TV) sit at left 78, top 151. They're hidden while the MM is open.
- `BezelAZFade` is empty (the old `fade_top`/`fade_bottom` were removed Oct 31 2026).

### Wiring
- `6100` visible `!$EXP[bz_navmenu]` + NumItems > 38 · `6500` visible `!$EXP[bz_navmenu]` · left 78 / top 151.
- `BezelAZFade`: empty include.

---

## Big album and speed rails

### Simple
While music plays, the big album art sits on the right. The compact now-playing view moves with it as one piece. Tapping the album opens the full-screen Dialogue view (1120). How fast it slides is a tuner setting.

### How it works
- There are four album grouplists, one per slide-speed setting. `bz_at_fsslide` picks which one is used, and its scrolltime sets the speed.
- Each has a "home" slot and an "FS" slot:
  - **Home slots** bounce focus straight to 6996 (MM open) or 60.
  - **FS slots:** every direction and Back go to their home slot, then 6390.
- The compact NP rides 6397 with the album (5.33.121). There's no 1120 fade, and the FS copy is hidden over Music (5.33.125).

### Wiring
| fsslide | Grouplist | scrolltime | Home slot | FS slot |
|---|---|---|---|---|
| 1 | 6367 | 480 | 6368 | 6369 |
| 2 | 6377 | 380 | 6378 | 6379 |
| empty / 3 (default) | 6397 | 280 | 6398 | 6399 |
| 4 | 6382 | 180 | 6383 | 6384 |

- Rails start at Includes_Bezel ~L2207. Home slot onfocus → `$EXP[bz_navmenu]` ? 6996 : 60. FS slot up/down/left/right/back → its home slot, then 6390.

---

## Side menu

### Simple
The side menu has Update library, Playlist, node editor and More add-ons.

### How it works / Wiring
These are Kodi music-window side buttons in `9000`. Playlist `612` opens the queue (playlists.md).

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move; at an edge → ALL `6097` if visible, else stay (no wrap, never to `..`) |
| Select | Open / play |
| Left | `bz_vback` close · A–Z hidden + navok → MM |
| Right | `bz_vback` → 6291 · grid → `gridenter` · 6160 → 1115 · idle → artist meta 3B (albums 6096 / songs·disc 6095 only; Artists list Right does nothing) |
| Back | … `bz_np` → clear + 6299 · `bz_atroot` → MM · else parent |
| M / Red | Music controls 1115 |
| Tab / Display | Now Playing 1112 |

## Touch
Big album tap → Dialogue FS 1120 (dialogue-fs.md).

## Related
mm-list.md · mm-warm.md · now-playing.md · np-bar.md · dialogue-fs.md · music-controls.md · section-transitions.md

## Touch: big album tap (5.33.221)
- Button `6180` (Includes_Bezel `BezelMusicPlayingArt`, left 1140 top 220, 600×600; visible while `bz_audio_latch` and no back/flip anim) now has the same Dialogue FS onclicks as remote 6390 when `$EXP[bz_pndlg_ok]`: SetFocus fsslide slot (`bz_at_fsslide` 1→6369, 2→6379, empty/3→6399, 4→6384) then `ActivateWindow(1120)`. When `bz_pndlg_ok` is false the tap does nothing.

## Artist meta — option 3B (5.33.224)

### Simple
With no music playing, **Right** from the list opens the artist's meta in the colour strip: big artist art, the name split over two lines (first word bold, the rest lighter), album/song counts in plain type, and the genres as white pills. **Left** or **Back** closes it and returns to the list. **Select** opens that artist (artists list: opens the row; album/song lists: the artist's albums). With music playing, Right still goes to the player controls (1115).

### How it works
- Album and disc/song levels only (Rob 5.33.225). Panel shows when `6095` (songs/disc) or `6096` (albums) is focused → `$EXP[bz_ameta]`. Not on the Artists list: there the big cover is already the artist thumb, so 3B would draw the same artist image twice. Only one artist image draws: 3B thumb; the right cover shows the album.
- On focus the button runs `bz_artist.py meta,<kind>,<dbid>,<name>`; it resolves the artist id and sets Home props `bz_am_n1` (first word), `bz_am_n2` (rest), `bz_am_counts`, `bz_am_thumb` (artist thumb, else fanart), `bz_am_g1..g6` (genres).
- While the panel is up, the strip's normal info grouplists hide (`!$EXP[bz_ameta]` added next to `!$EXP[bz_infoup]`). The tag button's white focus bar is now transparent — the panel is the focus cue.
- One-word names: counts + pills slide up 58 px.

### Wiring
| Item | Value |
|---|---|
| Include | `BezelArtistMeta3B` (strip-local 570,120): art 330² @30,40 · n1 `bz_b46` @400 · n2 `bz_m44` @458 · counts `bz_m26` @530 · pills two horizontal grouplists @582/@626 (`BezelAMPill`: `np_pill32` white, black `bz_mm18s` text, auto width, disabled) |
| List 60 onright | songs/albums → 6095/6096; no Artists-list route (6094 removed .225) |
| `bz_artmeta_ok` | music + `Container.Content(artists)` + not `..` + grid 6600 hidden + DBID set |
| Button 6094 | Present but `vis=false`, never focused (.225) |

## Random start (RANDSTART, current 5.33.226)
First visit to Music (no session row) picks a random row in list 60 (skips `..` and *All). If list 60 is hidden under MM, `bz_flip.py` `_defer` re-applies `SetFocus(60,row,absolute)` the moment 60 is visible (20 ms poll). While that deferred apply is pending, Home property `bz_randpend` holds list 60 at alpha 0 (Conditional fade 0→0, control stays IsVisible) so row 1 never flashes; it is cleared when the row lands, the folder changes, MM pick, or the 120 s timeout.

## RANDSTART flash guard (current, 5.33.230)
- `bz_randpend` (Home) is set at **warm-start for Music** whenever there is no session row yet — *before* the Container.Update / window load — so row 1 never paints.
- While set: list 60 is alpha 0 (still IsVisible), and the big album / flip art (`BezelPoster60`, `BezelPoster60M`, `BezelFlipA/B`) resolves empty in Music.
- Cleared when the random row lands (`_defer`, 10 ms poll, 30 ms re-apply), or immediately in `_restore` when there is nothing to land. Always cleared in `_defer` finally.
- No K40 bz_mmwarm open-anim gates are used.

## Idle Big Album fold
Moved to **`behaviors/idle-big-album-fold.md`** (APPROVED / locked, Rob Nov 1 2026). Book-page L|R leaf, 1400 ms × 2, 10 s hold, `bz_hf_a/b/ph` — see that file. Leaf flip family / boundary: [leaf-flip.md](leaf-flip.md) (not rock/sway, not `bz_cov_side`).

## 3B album / disc meta (5.33.236, current — Rob t1841)
- Same `BezelArtistMeta3B` panel, same layout (large art 330², split name bold/regular, plain counts line, white genre pills). Only the content changed.
- **Album level** (albums list, focus 6096): `bz_artist.py meta,album,<dbid>` → `ameta()` fills `bz_am_*` with the **album**: thumb = album art (else fanart), n1/n2 = album title split at first space, counts = `ARTIST · YEAR · [N discs ·] N tracks`, pills = album genres.
- **Disc / song level** (focus 6095): resolves the song's albumid + disc → same album art/title; counts = `ARTIST · YEAR · Disc d of n · N tracks` on multi-disc albums, else `· N tracks`.
- Fallback: no album id → old artist meta (`meta()`).
- Artists list: still no 3B. No K40 gates. .py → FULL restart.

## Merged song list — Artists → one list (MERGED13, current 5.33.272)
- **Flow:** Artists (L1) → Select → ONE song list for that artist (all albums). The Albums level (L2) is skipped. Back → Artists, with the artist row restored.
- **How:** Kodi lands on `musicdb://artists/ID/` as usual; `bz_flip.py` (main loop, path-change block) sees the hop came from the Artists root and does `Container.Update(musicdb://artists/ID/-1/)` (Kodi resolves to `…/ID/-1/-2/?artistid=ID` = all songs). Once loaded it sets sort **Album** (`Container.SetSortMethod(12)`, ascending) so each album's tracks sit together, track order inside. Back from the merged list lands on `artists/ID/` → `bz_flip` fires `Action(Back)` once → Artists. Never fires under MM / warm (`bz_nav` / `bz_mmwarm`), only on a real path change.
- **Album header bars:** Kodi can't insert header rows into list 60, so the header is the existing View D **disc bar** (fix-in-place): `$EXP[bz_discbar]` now also fires when `$EXP[bz_m13]` (music, songs, `musicdb://artists/…/-1/…`) on each album's track 1 (disc 1, or every disc when the album has several). Label `$VAR[BzDiscBarLabel]`: `ALBUM · YEAR` (or `ALBUM · DISC n · YEAR`). Normal album lists still show `DISC n · title` only for multi-disc albums.
- **Full-height list (5.33.272 rebuild):** on `$EXP[bz_m13]` the list is NOT View D. `bz_covercol` excludes bz_m13 (`[$EXP[bz_inalbum] + !$EXP[bz_m13]] | …`), so no 50% zoom, no 900 top slide, no 450 cover slot, no cover groups. Dedicated `itemlayout`/`focusedlayout condition="$EXP[bz_m13]" height="75"` (placed before the covercol layouts) draw 12 full rows from the panel top (y128) to the bottom, focus pill, album header bar on track 1. The parent `..` row stays as a blank top slot (the `bz_allpull_inall` -60 pull is gated `!bz_m13` so no row leaks above the panel).
- **Big album, never jumbo:** `$EXP[bz_nojumbo]` = bz_m13 | Artists root. The idle big-album 100→150 jumbo zooms (shadow / flat / sway copies, ~L1072/1076/1091) carry `+ !$EXP[bz_nojumbo]`, so the album stays BIG 1140,220 600² here. The locked fold groups (~L1097/1117/1121) were not touched.
- **Art follows focus:** big album, strip small album and 3B meta read the focused song's album art, so moving into the next album swaps everything natively (no script).
- **Unchanged:** big album slot, idle fold (locked 266/267), sway while playing, compact NP, MM warm/never-break, colour strip chrome, ALLHIDE.
- **Limits (first cut):** an album with no track 1 gets no header. The header sits on the first row (not a separate focusable row). Sort is Kodi's album sort (alphabetical, not by year). A–Z on this list jumps by song title.
- **Parked:** the 5.33.268/269 L3 strip (`bz_l3`, `BzL3FocusText`, 60px pill rows, header group, `l3_pill.png`) was reverted to 5.33.267 XML. The copy is at `/workspace/b401/parked_l3_268_269/`.

## Album / disc view types (current 5.33.246)
Options › Section options › **Album View** (9978, DialogMusicInfo) toggles skin bool `bz_albview_a`. Default = D.
- **D (default, bool off)** — `$EXP[bz_albd]` = !bz_albview_a + bz_inalbum:
  - Cover column slot (450 above the rows; **not drawn in the MERGED13 artist song list** since 5.33.271): the small in-list album art (`BezelInAlbumArt`) is hidden; the dark FF141414 mask stays and an album header (Album title bold 26 + album artist 18, bottom of the slot, just above the rows) draws instead.
  - Rows: covercol item/focused layouts only (no row thumbs). On multi-disc albums the first track of each disc (`$EXP[bz_discbar]`: TotalDiscs>1, track 1/01, !MM) draws a full-width (450×26) light bar with left-aligned black **DISC n · disc title**; every row label on that row slides down 13 px so the track text sits under the bar. Old 5.33.237 right-side overlay header in the 60 layouts removed.
  - Right 3B = focused SONG: `bz_flip.albview_a()` polls (0.1 s while D in album) and sets Home `bz_albvd=1` + `bz_sd_thumb` (song Art(thumb)/Icon), `bz_sd_n1`/`bz_sd_n2` (title split at first space), `bz_sd_meta` (Disc n · Track n · duration), `bz_sd_alb` (artist — album). `bz_ameta` includes bz_albvd so the strip content hides; the song panel lives in `BezelArtistMeta3B` (570,120). Focusing the artist tag 6095/6096 swaps back to the artist/album 3B panel. Cleared on leaving.
- **A (bool on):** `bz_flip.albview_a()` (0.25 s) sets Home `bz_albva` at musicdb album/disc song level and calls `bz_artist.py meta song <dbid>` on folder/disc change → `bz_ameta` holds the 3B album panel (art, split title, artist·year·disc/tracks, genres) in the colour strip. In-list cover art still shows. Cleared when leaving.

## 5.33.244 current state
The RANDSTART pending gate (`bz_randpend`) no longer hides anything. List 60, the big album, and the flip/poster art always paint. Python still sets and clears the property, but no XML reads it. Row-1 may flash briefly on the first Music start.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/music-list.md) · [state](../state/music-list.md) · [motion](../motion/music-list.md) · [art](../art/music-list.md) · [input](../input/music-list.md) · [theme](../theme/tokens.md) · [screens](../port-refs/music-list/) · [PORT_INDEX](../PORT_INDEX.md)

- **5.33.273 NOFRAME (Rob t2065u, Nov 1 2026):** big white "panel frame" on Music right art was NOT a panel control — it was the hinge-fold stack group (Includes_Bezel.xml ~L1097: static half-frames bz_frame_half_l/r + shades) and the two glare groups (~L1117, ~L1121) still running the idle jumbo zoom 100→150 around 1440,420 (→990,120 900²) because 272 gated only the art layers with `!$EXP[bz_nojumbo]`. Gate added to those 3 zoom-ins. On Artists L1 + merged songs the fold half-frames/glare now stay locked to the 600² art at 1140,220 (thin edge only). Fold, sway, glare, 6180 touch untouched. ReloadSkin (XML). Smoke /workspace/b401/smoke_273_noframe/. Not zipped.


## No-art (5.33.276)

**Simple:** An album/artist with no cover shows an empty slot — no stand-in, no grey default cover, and the big album no longer fades away.

**How it works / Wiring:** idle big album `$EXP[bz_noart60]` fade removed; genres/years poster-window `bz_vnoart` fade removed; both expressions deleted. Warm chain ends at `Player.Icon`. See mm-warm.md → No-art.

## Current state (5.33.278)
Music artists/albums/songs: list 60 sits in the colour strip (570..960, uniform 86.67% scale, same nav/focus). Meta (small/big/year+genre pills) on the fanart block 150,196–296. FULLSCREEN pill 6886 at fanart UL 140,136 (music, audio playing; same actions).

## 5.33.280 (Nov 1 2026)
- Music L2/L3 half list (bz_mhalf → bz_covercol): small album at top of strip, list under it, no big strip title (BezelArtistMeta3B hidden). Strip slide 450→510.
- Meta = FS fanart format: small artist bz_mm18s, big title bz_mm34 uppercase, outlined pills np_pill32_ol.png (also in Custom_1121 year/genre).
- FULLSCREEN pill 6886: Left from list 60 (music strip, pill visible) → 6886; Left on 6886 → list 60 + open MM; Select unchanged (1121 when bz_m1121ok, else visualisation).
- Open: L2 ALL ALBUMS row 6097/6098 not shown in half-list mode.

**5.33.281 warm rail:** the big-album rail (6367/6377/6397/6382; big album + compact NP) is the one group shown in Music section AND under MM warm — same controls, no MM twin swap (see mm-warm.md). Open: L2 ALL ALBUMS row 6097 still hidden in half-list (`bz_mhalf` makes `bz_covercol` true; 6097 visible = `!bz_covercol | bz_allpick`).

**5.33.282 ALL ALBUMS in half-list:** L2 artist albums (half-list, `bz_mhalf`) shows ALL ALBUMS row 6097 flush under the last album row. Gate `bz_allhalf` (= bz_mhalf + bz_artistalbums) lets 6097 show despite `bz_covercol`; offset = covercol 75px rows from y450 (+15/item, −135 with `..`). Long lists (>6 rows) keep the y1020 rule: row shows only when focused or list fits. L1 full list and L3 unchanged.

## 5.33.289
The big album rail + compact NP block is now the shared include `BezelMusicRail`; Music still mounts it in View_60 with the same visibility. See mm-warm.md for non-Music MM mounts.

**5.33.296 HALFALB (Rob t2233u, Nov 1 2026):** L2→L3 small strip album jumped. Cause: at L2 (artistalbums, bz_covercol true, not m13) the list-group cover mask + art (Includes_Bezel ~L2519/L2520, 0,0 450x450 inside the 86.67%-zoomed/510-slid list group, texture BezelInAlbumArt) drew over the strip small album; at L3 (bz_m13) those groups are hidden, leaving only the strip album control (570,120 390x390, ListItem.Art(thumb)). Fix: both list-group cover groups gated `!$EXP[bz_mhalf]`, so L2 and L3 use the one shared strip album at 570,120 390x390. L1 / album-folder cover column unchanged. ReloadSkin (XML). Not zipped.

## 5.33.297 — Left from list
Music strip (L1/L2/L3) with FULLSCREEN pill 6886 visible: Left from 60 → 6886, priority over A-Z bar 6100/6500 (L1 Artists used to jump to the A-Z bar, skipping the pill). No pill → A-Z bar if shown, else MM.

## Strip-only list (5.33.298)
List 60 is always the colour-strip list — the old full-size off-strip list is parked at `/workspace/b401/parked_old_list/` (RESTORE.md). Every list view (Music L1–L3, Movies/TV, Music root, sources, files, non-library) draws in the strip: the list group is laid out 450×1038 at x120/y120 and always shrunk 86.67% (center 120,120) + slid 510 → on screen x570–960, y120–1020 (390×900, fills the strip, ~13.8 rows of 75). Grouplist clip (t4533) is 450×1038 so nothing paints past y1020. ALL row 6098 always rides the same shrink/slide. Left still goes to FULLSCREEN 6886 first on Music (5.33.297); Up/Down wrap to 6097/6098 unchanged; A–Z bars 6100/6500 stay at x78.

## 5.33.304 — fit in the colour strip (Rob)
- The list sits flush in the colour strip on Levels 1–3: it's nudged right 7 so the highlight lines up with the strip edge.
- The list stops above the double-tap tag: its height went from 1038 to 981, so long Level 1 lists no longer run over the tag.
- Level 2 half list: ALL ALBUMS now sits right under the last album. The old 135 pull put it on top of the first album, so it was removed.


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## Meta text per level (current, 5.33.311 — Rob pt2364u)
Fanart-block meta (`BzMMetaSmall` / `BzMMetaBig`, Includes_Bezel ~L124–125, labels ~L1480–1481):
- **L1 Artists:** small `ARTIST`, big = list label.
- **L2 Albums:** small = artist, big = album title (list label).
- **L3 Songs:** small = **artist only**, big = **album title** (`ListItem.Album`, falls back to label).
- Year + genre pills unchanged on all levels.
- Fanart FS (1121) is deliberately different — song-focused; see music-fanart-fs.md.

## Big album art after stop (5.33.320, Rob t2402/t2403 — current)
- Playing: `BezelBigArt` = `Player.Art(thumb)`. Stopped: Music list focus art via `BezelPoster60` (Container(60) thumb / next-item thumb / icon).
- When music stops (latch drop + no media) `bz_flip.py` saves the last shown cover to Home `bz_cov_last` before clearing `bz_cov_a/b`. It persists (never cleared).
- `BezelBigArt` falls back to `bz_cov_last` when stopped and either not in the Music window or no Container(60) art resolves (e.g. returning from FS/viz to Home/MM/other section, or 1122 resolving no list art). Music list focus art still wins when it exists.

## Now Playing over Level 2 / Level 3 (5.33.324)
When Now Playing (1112) opens over the Level 2 album list or Level 3 song list, the small strip album (570,120 390×390) fades out over 1 s with the list, meta and info, and fades back when Now Playing closes — the same as every other strip piece. (Lost in 5.33.296 when the list-group cover, which carried the fade, was hidden at L2/L3.)

## Art fade-in (5.33.329)
Music section art fades in (no pop), ~400 ms: big album 1122 rail image fadetime 400; Music poster twin (`BezelPoster60M`, MM closed) fadetime 400 + one-shot 400 ms sine-out Visible fade-in; list/cover-column album (`BezelInAlbumArt`, 3 images) fadetime 400. MM A/B lanes / Warm mirror-enter unchanged (locked).

## List bottom (5.33.347, t2491)
Double-tap hint (BezelDtapHint) is fixed at y978 h30 in the colour strip. List 60 clip grouplist + list are 858 tall from bz_top 120, so the list ends at y978, right above the hint. PVR lists (50) use the same 858. Any new section list must end at y978 or higher.


## Global artwork group (5.33.366)
See `artwork-group.md`. Big album + Compact NP now sit in 1122 group 6400 / album layer 6402, opacity-gated by `bz_railvis` (no Visible remount, sway clock unbroken). Poster layer 6401 pre-warms Videos poster and crossfades in during Music↔Movies/TV handoff. MM Warm underlay unchanged.

## 5.33.367 — poster stage
The swaying Movies/TV poster (BezelVPLPoster) now draws only in dialog 1122 layer 6401, fed by the bz_flip list-60 Home mirror (bz_v60_*, bz_vpl_on). Screens keep only the tap target. See `artwork-group.md`.

- 5.33.382 POSTERWARM: Music→Movies/TV — the 1122 poster layer never draws Music art (twins read held `bz_v60_art`); see artwork-group.md.

## Idle album A/B (current, 5.33.384)
Idle Music big album in the 1122 album layer draws two always-loaded images: `bz_m_idle_a` / `bz_m_idle_b`; `bz_m_idle_side` (a|b, empty=a) picks the shown one. Each has a Conditional 400 ms sine fade-out when `Player.HasAudio` or it is not the shown side; the NP layer (`bz_m_np_art`) is unchanged. `bz_flip.py` `_m_idle_stage()` (called from `m_mirror`): first cover goes straight into the shown slot; later covers go to the hidden slot, wait 0.6 s to decode, then flip side and set `bz_m_idle_art` (= cover on screen, used by MMHOLD/IDLERESET locks). Hidden slot is not written until 0.45 s after a flip. Random steps (UADVRAND, MM + startup only) therefore crossfade, never pop; after MM wake the 383 hold applies, then the next random step crossfades.
