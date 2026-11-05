# Music Fanart FS (Bezel fullscreen music)

**Object:** fullscreen music screen over any section · Kodi: dialog `1121` (`Custom_1121_MusicFanartFS.xml`) · main `6420` · cycle pill `6421` · Back router `6422` · touch `6426`–`6430` · big album pill `6401` (shared)
**Where:** over Music, Home, Movies / TV, Pictures, Programs, Add-ons while music plays
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none. **Rob rule:** any change to Kodi Fanart FS ([fanart-fs](fanart-fs.md)) is made here in the same build, and the reverse; alert Rob that it applies to both.

## Simple
With music playing, FULLSCREEN (the strip pill, the MM FULL pill, Tab or the remote's Display key) fills the screen with the playing artist's fanart, the big album swaying on the right, the song's artist / album / title at the top left and a progress bar that grows out of the year pill. Nothing restarts: the fanart and the album keep moving exactly as they were. Double-Select slides the big album to the centre with the previous and next albums beside it (album view). Back from album view returns to the fanart; Back from the fanart closes fullscreen and returns you where you were. If the music stops, fullscreen closes by itself.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Fanart stage | open fullscreen | double-Select → Album view; Back → closed | artist fanart full screen, big album home (right), meta + progress top left, cycle pill top left, transport bar |
| Album view | double-Select (or double-tap the album) | Back → Fanart stage | big album slides to centre; side albums fade in; NP bar under the centred album |
| Cycle mode | Up to the cycle pill, Left / Right / Select | Down | one of six panels: Visualizer, Bio, Fanart, Lyrics, Up Next, Controls; mode name flashes 2 s |
| Up Next list | cycle mode Up Next, Down | Back / Up from first row / Left | queue list; Select plays that song |
| Controls | cycle mode Controls, Down; or Menu / Red | close it | music controls dialog on top |
| Closed | Back from Fanart stage; Tab / Display; music stops | — | the screen you came from, same row focused |

### Timeline
**Open (from any section)**
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | fullscreen layer fades in over the section; behind it a black cover and the fanart stage fade in (non-Music sections) | 300 | sine |
| 0 | big album already swaying; it is not restarted | — | — |
| 150 | progress bar grows right out of the year pill (from the pill's left edge) | 2000 | sine in-out |
| 0 → 1000 | genre pill fades away (hard-hidden at 1150) | 1000 | sine |
| 2100 | elapsed / duration labels fade in | 300 | sine |

**Fanart stage → Album view**
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | big album slides left 480 px to centre (1140 → 660) | 280 (Tuner: 480 / 380 / 280 / 180) | sine in-out |
| 0 | side albums fade in (no wait) | 2000 | sine |
| 480 | NP bar fades in under the centred album | 600 | sine |
| Back | NP bar fades out 300 ms; album slides home (reverse of the slide); sides fade out | 280 / 300 | sine |

**Close**: fade-out (300 ms chrome, 600 ms whole screen, sine in-out); the section underneath is already drawn, focus returns to its list (or the MM reopens if fullscreen was opened from the MM). Exception: closing onto the Music song list of an artist's album (Level 3) is instant, no fade (5.33.306).

### Interruptions
- Back during the slide to centre: the slide reverses from where it is (no jump).
- Track change in either state: art crossfades in place; no slide, no restart; side albums update.
- Music stops: closes at once (any state).
- Video starts: fullscreen music closes and video fullscreen opens.
- Second Select within 1 s on the fanart stage = album view; a single Select = play / pause, applied after the 1 s window.

### Continuity
- The fanart stage and the big album's sway, glare, lit dust and cast never restart when fullscreen opens or closes, or on Fanart ↔ Album view.
- The fanart image under fullscreen is the same image the section showed (or the preloaded artist fanart outside Music): no reload flash.
- Leaving returns focus to the same list row.

### Layering
Section window (+ black cover + fanart stage when not in Music) < big album layer (album, side albums, sway, glare, dust, NP bar under centred album) < fullscreen chrome (meta, progress, cycle pill, transport bar, Up Next list) < music controls < system dialogs.

### Geometry
| Element | Position (1920×1080) |
|---|---|
| Fanart stage | full screen |
| Big album home / centre | x 1140–1740 / x 660–1260, y 220–820 (600 × 600) |
| Side albums | 90, 250 and 1290, 250, 540 × 540 (title / artist panel on their lower 162 px) |
| Meta: small ARTIST · ALBUM | 150, 196, 780 × 30 |
| Meta: big SONG TITLE | 150, 226, 780 × 60 |
| Year pill → progress bar | 150, 296; bar 780 × 32 |
| Cycle pill | 140, 136, left-aligned; "press down to open" hint 140, 172 |
| Prev / next song pills | 226 × 32 at x 128 / 726, y 981 |
| NP bar under centred album | album x range, y 892–1004 |
| Touch: prev / next album | 90, 250 / 1290, 250 (540 × 540); album 1100, 220 (680 × 680); right half 960, 0 (960 × 1080); logo 0, 0 (120 × 116) |

### Art
- Fanart: playing artist's fanart, fills the screen (scale to cover).
- Big album / side albums: the playing / previous / next covers; no cover → nothing drawn (no placeholder, no stub shadow).
- Progress bar 25 % white ring and fill over 25 % black; time labels 100 %.
- Pills: rounded 32 px pill, 16 px caps, tinted fill.

### Input
| Action | Fanart stage | Album view |
|---|---|---|
| Select | 1st: play / pause after 1 s; 2nd within 1 s: Album view | play / pause (pause logo on the album) |
| Left / Right | previous / next song | previous / next song |
| Up | cycle pill | big album pill |
| Down | — | — |
| Back | close fullscreen | Fanart stage |
| Long Select | play / pause | play / pause |
| Menu / Red | music controls | music controls |
| Tab / Display | close fullscreen | close fullscreen |
| Cycle pill Left / Right / Select | previous / next mode (wraps); Down: Controls → music controls, Up Next → list, else back to the stage | |
| Touch | album double-tap → Album view, tap → play / pause; right half tap → Up Next; logo → close; side albums → previous / next | |

### Speed targets
- Fullscreen visible ≤ 300 ms after the key; the fanart is already cached (preloaded while music plays).
- Album view slide feels immediate (≤ 280 ms default).

### Never
- No sway / glare / dust restart on open (5.33.210 copy design; 452, 453).
- No old Now Playing panel or old upper-right cycle pill around open / close (465 OLDPILL / OLDNP).
- No NP bar on the fanart stage under the home album (470 reverted 463).
- No idle auto-open (5.33.311).
- No wait before side albums (317 "remove the wait").
- No small cover in the stage's corner on open (472 ALBUMHALF).

### Acceptance checks
1. Music list, song playing → FULLSCREEN: one fade, album still mid-sway, meta + progress grow in.
2. Same from Home, Movies, TV, Pictures, Add-ons → identical screen; Back → same section, same row.
3. Double-Select → album to centre with sides and NP bar; Back → album home, bar fades, sides fade.
4. Stop music while fullscreen → closes to the section.
5. Play a video, press Tab → video fullscreen, not music.

## Kodi implementation (sandbox)

### How it works
- **Why a dialog (Intent: one fullscreen over everything).** Kodi's real visualisation window replaces the section window, which would restart the stage and the album. 1121 is a dialog over the current window, so the window and the always-open big album dialog 1122 keep running. Since 5.33.309 the album, sway, glare, dust and NP bar live in 1122, so 1121 only needs the window for the fanart stage.
- **Openers.** When `$EXP[bz_m1121ok]` (audio, no video, kill switch off, window in `bz_fs1121win` = Music / Home / Videos / Pictures / Programs / Add-ons, not viz): FULLSCREEN pill 6886, MM FULL pills 6960 / 6910, big album routes, Tab / Display keymap in those windows, `bz_cmd.py` `tab` / `np` / `nptoggle` / `vistoggle` / Info-with-no-album / auto-NP / bz_flip `bz_tabq`, Tuner Back with `bz_tunesrc=fsctrl`. Otherwise the same controls open Kodi FS (`ActivateWindow(visualisation)`).
- **Fanart stage outside Music.** `BezelFSUnderlay` (black 1920×1080 + `BezelNPInPlace`, npfade 300) at the end of Home, MyVideoNav, MyPics, AddonBrowser; `BezelFSUnderlayBlack` in MyPrograms (it already has the stage). Visible `Window.IsVisible(1121) + !Window.IsActive(music) + Player.HasAudio`, 300 ms fades. In Music the list view's own `BezelNPInPlace` is the stage.
- **Fanart preload.** 1122 draws `Player.Art(artist.fanart)` at 3 % while audio plays and neither 1121 nor viz is up, so the texture is cached.
- **onload** (in order): close if kill switch / no audio / video / window not allowed; video → `ActivateWindow(fullscreenvideo)`; not allowed + audio → `ActivateWindow(visualisation)`; keymap refresh; `bz_pnoff=1` (fanart stage); `bz_dfs_mode` defaults to `album`; `bz_fsnp`, `bz_np`; start bz_flip if not running. **No `bz_sway_restart`.**
- **Album view.** 6420 double-Select clears `bz_pnoff`; 1122 reads `bz_rail` / `bz_pnoff` and slides the album −480 on the `bz_at_fsslide` rail (1 / 2 / 3 / 4 = 480 / 380 / 280 / 180 ms, default 3). Sides: `BezelFSPlayNext` (sdelay 0, sfade 2000). NP bar: 1122 VIZNPBAR group, gate `[viz | Window.IsVisible(1121)] + bz_fsnp + bz_railc + Player.HasAudio` (600 ms in after 480, 300 out).
- **Back.** Keymap Back / Backspace / B → `SetFocus(6422)`; 6422 onfocus: album view → `bz_pnoff=1` + focus 6420; fanart → `Dialog.Close(1121)`.
- **Open / close fades.** WindowOpen fade 300 ms; WindowClose 300 + 600 ms fades, both gated `!$EXP[bz_m13]` (no fade onto Music Level 3).
- **onunload.** Clears `bz_np`, `bz_fsnp`, `bz_pnoff`, `bz_pnfoc`, `bz_vdtap`; sets `bz_gridret` for 3 s; if MM closed and not opened from the MM (`bz_fsmm` empty): `AlarmClock(bz_m1121ret,SetFocus(60))`. Opened from the MM (`bz_fsmm` latched by bz_cmd / bz_flip): bz_flip reopens the MM on exit.
- **Auto-close.** Timer `bz_m1121stop`: `!Player.HasAudio` → `Dialog.Close(1121)`.
- **Meta / progress.** Shared include `BezelFSMeta` (same as Kodi FS). Tuner `bz_fs_ttl_off` (meta), `bz_fs_prog_off` (progress), `bz_fs_pill_off`, `bz_fschrome_fan` (Fanart cycle mode keeps chrome; default hides meta + progress, 300 ms).
- **Cycle pill 6421.** `Skin.String(bz_npmode)` = vis / bio / fanart / lyrics / upnext / controls (empty = vis); label flash via `bz_npmlabel` (2 s alarm `bznpml`). Down: controls → `ActivateWindow(1115)`, upnext → 6396 (list 6395, `BezelFSUpNext`, Select `bz_cmd.py upnext_goto`), else 6420.
- **Pill idle.** bz_flip `_pill_idle`: 6421 idle 5 s → focus back to where it came from (else 6420).

### Wiring
| Control / key | Action |
|---|---|
| 6420 Select, fanart | 1st `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01)` + `bz_vdtap=1`; 2nd within 1 s: `CancelAlarm(bz_vdtapgo)`, `ClearProperty(bz_pnoff)`, `bz_vdtap=2`; always `AlarmClock(bz_vdtapclr,…,00:01)` |
| 6420 Select, album view | `bz_pnfoc=6403` (pause logo) / clear if paused; `PlayerControl(Play)` |
| 6420 Left / Right | `PlayerControl(Previous / Next)` |
| 6420 Up | album view → 6401; fanart → 6421 |
| 6422 | Back router (above) |
| 6426 logo (touch) | `Dialog.Close(1121)` |
| 6427 / 6428 | `Playlist.PlayOffset(music,-1 / 1)` (album view only) |
| 6429 album (touch) | click `PlayerControl(Play)`, doubleclick clear `bz_pnoff` (fanart only) |
| 6430 right half (touch) | `Skin.SetString(bz_npmode,upnext)` (fanart only) |
| Keymap `<window1121>` | m / red → 1115; tab / display → `Dialog.Close(1121)`; escape → Back; back / backspace / browser_back / b → `SetFocus(6422)`; long return / enter → PlayPause |
| Includes | `BezelFSMeta`, `BezelLogo`, `BezelBigAlbumPill`, `BezelFSPlayNext`, `BezelFSUpNext`, `BezelNPControls` |
| Expressions | `bz_m1121ok`, `bz_fs1121win`, `bz_railc`, `bz_npm_fan` |
| Home props | `bz_pnoff`, `bz_fsnp`, `bz_np`, `bz_pnfoc`, `bz_vdtap`, `bz_rail`, `bz_fsmm`, `bz_npmlabel`, `bz_gridret` |
| Skin | `bz_m1121_off` (kill switch), `bz_dfs_mode`, `bz_npmode`, `bz_at_fsslide` |

### Kodi workarounds (do not port)
- Opening a dialog instead of a window, and the per-window underlays, exist only because a Kodi window switch would restart the stage. A native port draws one fullscreen layer over the app.
- The 1 s `AlarmClock` double-tap and the 6422 focus trick for Back: Kodi has no double-press event and no per-state Back handler.
- The onload close / redirect chain: Kodi can't refuse to open a dialog, so it opens and closes itself.
- `Dialog.Close(1112)` in onload: no-op since 465.
- `bz_gridret` 3 s: legacy grid return flag (grid removed in 455).

## Related
[fanart-fs](fanart-fs.md) · [big-album](big-album.md) · [big-album-pill](big-album-pill.md) · [play-next](play-next.md) · [np-bar](np-bar.md) · [fullscreen-pill](fullscreen-pill.md) · [music-controls](music-controls.md) · [keymaps](keymaps.md) · [sway-animations](sway-animations.md)
