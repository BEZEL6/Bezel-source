# Dialogue FS

**Object:** album-centred view over the Music list · Kodi: dialog `1120` (`Custom_1120_PlayNext.xml`) · main `6400` (660,220 600×600) · big album pill `6401` (`BezelBigAlbumPill`) · touch sides `6405` / `6406` · side albums `BezelFSPlayNext`
**Where:** Music section only, over the Music list
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
In Music, tapping the big album (or Right / Select on the playing panel, or Right in Music controls) slides the big album to the centre of the screen while the list fades away; the previous and next albums appear beside it. Select pauses (a pause logo appears on the album), Left / Right change song, Up goes to the album pill (ALBUM ↔ PREV/NEXT). Back slides the album home and the list comes back.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Closed | — | open (above) | Music list, album home |
| Album centred | open | Back; music stops | album at centre, list faded, chrome fades in late |
| Sides on (PREV/NEXT) | album pill → PREV/NEXT | album pill → ALBUM | previous / next covers beside the album |
| Paused | Select | Select | pause logo (Bezel logo with bars) on the album |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | album slides home → centre (480 px left) | 280 default (480 / 380 / 280 / 180) | sine in-out |
| 0 | Music list / strip fades out (same time as the slide) | 280 | sine in-out |
| 0 | strip cast shadow fades out | 250 | sine out |
| 0 | side albums (if on) fade in | 2000 | sine |
| 1000 | Dialogue FS chrome (pill, controls) fades in | 600 | sine in-out |
| Back | chrome fades out 600; album slides home; list fades back; strip cast back after 1200 | 600 / 280 / 600 | sine |

### Interruptions
- Back mid-slide: the slide reverses from its position.
- Music stops: closes (same as Back).
- A second open while open: ignored.
- Opening Bezel fullscreen music: Dialogue FS can't open while it is up.

### Continuity
- The big album is the same object as on the Music list: it slides, it doesn't reappear; sway, glare and dust keep running.
- Back returns focus to the list row (or the MM if it was open).
- After Back the stage is held off for about 1 s so it doesn't flash in before the album is home.

### Layering
Music window (list fading out) < big album layer (album at centre, sides) < Dialogue FS chrome (pill, pause logo highlight).

### Geometry
| Piece | Value |
|---|---|
| Album centre | 660, 220, 600 × 600 |
| Side albums | 90, 250 and 1290, 250, 540 × 540; title / artist on a lower panel |
| Pause logo | 111 px (≈ 35 %), centred on the album (245, 245 inside it) |
| Album pill | upper right (see [big-album-pill](big-album-pill.md)) |

### Art
Album and sides: the playing / previous / next covers. Side cast shadow only when that side has a real cover. Pause logo: Bezel logo with centred pause bars.

### Input
| Action | Result |
|---|---|
| Select | pause / resume (logo on pause) |
| Left / Right | previous / next song |
| Up | album pill |
| Down | nothing |
| Back | close (slide home) |
| Touch side album | play that song |
| Touch logo | Back |

### Speed targets
Slide ≤ 280 ms by default; the album must start moving on the same frame as the key.

### Never
- No idle auto-open (411 NOIDLEFS: opens only on an explicit Select / tap).
- No wait before the sides (317).
- No viz layer behind the chrome (416).
- No stub cast shadow next to an empty side (127).

### Acceptance checks
1. Music list, song playing → tap the album → album slides to centre, list fades.
2. Select → pause logo; Select → gone.
3. Up → pill → PREV/NEXT → sides appear; ALBUM → they fade.
4. Back → album home, list back, same row focused.
5. Stop the music while open → closes.

## Kodi implementation (sandbox)

### How it works
- **Open.** `$EXP[bz_pndlg_ok]` = `!bz_pndlg_off + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !viz + !1120 + !Window.IsVisible(1121)`. Openers: 6390 Select / Right, touch 6180 on the album (1122), 1115 Right (13 actions in Custom_1115). Each sets `bz_rail=centre` then `ActivateWindow(1120)`.
- **onload:** `bz_dfs_mode` defaults to `album`; `bz_rail=centre` (1122 slides the album; see [big-album](big-album.md)).
- **Under it:** Includes_Bezel groups fade out at the slide speed (four `bz_at_fsslide` copies 480 / 380 / 280 / 180) on `Window.IsActive(1120) | [1121 + album view] | …`; strip cast fade 250 ms out, 600 ms back after 1200 ms.
- **Fades:** WindowOpen 600 ms delay 1000; WindowClose 600 ms.
- **Back.** 6400 onback: `bz_fsret=true` + `AlarmClock(bz_fsretclr,…,00:01)` + `Dialog.Close(1120)`. `bz_fsret` holds the stage off-frame ≈ 1 s.
- **onunload:** clear `bz_pnfoc`, `bz_pnsel`; `bz_rail=home`; focus 6996 (MM open) or 60 by alarm `bz_pvret`.
- **Auto-close.** Timer `bz_1120_autoclose`: audio stops → `bz_fsret` + close.
- **Sides.** `BezelFSPlayNext` `vis=Player.HasAudio`, `sdelay=0`, `sfade=2000`, `sides=!String.IsEqual(Skin.String(bz_dfs_mode),album)`.

### Wiring
| Key on 6400 | Action |
|---|---|
| Select | `!Player.Paused` → `bz_pnfoc=6403`; paused → clear; then `PlayerControl(Play)` |
| Left / Right | `PlayerControl(Previous / Next)` |
| Up | 6401 |
| Down | `bz_noop` |
| Back | fsret latch + close |
| onfocus | `ClearProperty(bz_pnfoc)` |
| 6405 / 6406 | onfocus → 6400; click `Playlist.PlayOffset(music,-1 / 1)` (touch only) |
| 6401 | `BezelBigAlbumPill` `main=6400`, `back_close=1` |
| Skin | `bz_pndlg_off` (kill switch), `bz_dfs_mode`, `bz_at_fsslide` |
| Pause logo | `bezel/logo_pause.png` |

### Kodi workarounds (do not port)
- `bz_fsret` 1 s latch: covers Kodi re-showing the stage before the album's reverse slide ends.
- Touch buttons that forward focus to 6400: keeps remote keys off the touch targets.
- The internal names "Play Next" / `bz_pn*` are historical; the object is Dialogue FS.

## Related
[big-album](big-album.md) · [big-album-pill](big-album-pill.md) · [play-next](play-next.md) · [music-controls](music-controls.md) · [music-list](music-list.md) · [music-fanart-fs](music-fanart-fs.md)
