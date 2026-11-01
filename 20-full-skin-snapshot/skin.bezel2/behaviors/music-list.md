# Music section list

**Object:** `MyMusicNav.xml` · list `60` · grouplist (Includes_Bezel ~L1492) · ALL `6097` · A–Z `6100`/`6500` · album rails `6367`/`6377`/`6397`/`6382` · NP proxy `6385`
**Where:** Main menu MUSIC (and the music pills) → music window
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Edge-to-ALL with no wrap. Left opens the MM when the A–Z bar is hidden, and Back at the armed root opens the MM (clearing NP first). The big album and compact NP share album grouplist 6397, and the speed rail follows `bz_at_fsslide`. Tap big album → Dialogue FS 1120. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

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
| Right | `bz_vback` → 6291 · grid → `gridenter` · 6160 → 1115 · else 6192 |
| Back | … `bz_np` → clear + 6299 · `bz_atroot` → MM · else parent |
| M / Red | Music controls 1115 |
| Tab / Display | Now Playing 1112 |

## Touch
Big album tap → Dialogue FS 1120 (dialogue-fs.md).

## Related
mm-list.md · mm-warm.md · now-playing.md · np-bar.md · dialogue-fs.md · music-controls.md · section-transitions.md
