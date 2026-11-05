# Now Playing bars and NP mode

**Object:** the compact NP bar under the big album, the NP bar under the centred album, the stage transport bar, and the "NP mode" flag · Kodi: include `BezelNPCompactBar`, 1122 VIZNPBAR group, `BezelNPInPlace` transport group, expression `bz_np` / Home `bz_np`, proxy `6385`
**Where:** under the big album (home or centre); bottom of the fanart stage in fullscreen
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
While music plays, a small now-playing bar sits under the big album: artist, song title, a thin progress line and the time. When the big album slides to the centre in fullscreen, the bar goes with it under the centred album; when you go back to the fanart, it fades away. On the fullscreen fanart stage a transport bar shows the previous and next song titles as pills.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Compact bar (home) | music playing, big album home, outside the Music NP mode | NP mode / fullscreen | bar under the album at the right |
| Centre bar | fullscreen album view | back to the fanart stage; music stops | bar under the centred album |
| Transport bar | fullscreen fanart stage | album view / close | prev / next song pills at the bottom |
| NP mode | Bezel fullscreen or the Music NP panel showing | close | the in-place NP chrome replaces the compact bar |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| album view entered | centre bar fades in after the album has moved | 600 after 480 | sine |
| back to fanart | centre bar fades out | 300 | sine |
| track change | labels / progress update in place | — | — |

### Interruptions
Back during the centre bar's delay: the bar never appears (its fade reverses from 0).

### Continuity
The compact bar is part of the album group: it slides with the album and never re-fades when the album moves.

### Layering
In the big album layer, just under the album art. Under fullscreen chrome.

### Geometry
| Piece | Value |
|---|---|
| Compact bar (album home) | x 1140–1740: artist 1140, 892 (600 × 24); title 1140, 922 (600 × 64); progress 1140, 1000 (450 × 4); time 1540, 988 (200 × 28) |
| Centre bar | the same bar shifted −480 (x 660–1260) |
| Transport pills | 226 × 32 at x 128 / 726, y 981 |

### Art
Text only + a thin progress line; transport pills use the cycle-pill chrome (32 px pill, tint 50 %); whole transport bar at 50 %.

### Input
None (display only).

### Speed targets
Bar text updates within a frame of a track change.

### Never
- No NP bar under the home album with Up Next on the fanart stage (463 → reverted in 470).
- The centre bar shows in both fullscreens (Bezel and Kodi FS) (470 CENTREBAR).

- No shadow copies of the transport pills (473 FSSHADOWDEL: they broke the bar texture).
### Acceptance checks
1. Movies with music playing and the MM open → compact bar under the album.
2. Fullscreen → double-Select → bar appears under the centred album after it lands; Back → fades.

## Kodi implementation (sandbox)

### How it works
- **NP mode.** `$EXP[bz_np]` = `bz_np=true` + [`Window.IsActive(music)` | `bz_fsnp=true`] + `bz_audio_latch=true` + `!Player.HasVideo`. Set by 1121 / Kodi FS onload and `bz_cmd.py` routes; cleared by close paths. MyMusicNav saves it on unload (`bz_np_was`) and refocuses 6390 on load if `bz_np_focus`.
- **Compact bar.** `BezelNPCompactBar` inside `BezelMusicPlayingArt` (1122), mounted with `!Window.IsActive(music) + !viz` and `!$EXP[bz_np] + !viz`.
- **Centre bar (VIZNPBAR).** 1122 group with the bar shifted −480, gate `[Window.IsActive(visualisation) | Window.IsVisible(1121)] + bz_fsnp + $EXP[bz_railc] + Player.HasAudio`, fade in 600 ms delay 480, out 300.
- **Transport bar.** In `BezelNPInPlace`, group `bz_fs_tbar_off` (Tuner).
- **NP proxy 6385** (off-screen x −400 in MyMusicNav and MusicVisualisation): with NP → focus 6390 + `bz_cmd.py npctl,toggle` (opens / closes 1115); without → side menu 9000.
- List 60 onback in Music: with `bz_np` → clear `bz_np` + 6299.

### Wiring
| Item | Value |
|---|---|
| Expression | `bz_np` |
| Home | `bz_np`, `bz_fsnp`, `bz_audio_latch`, `bz_np_was`, `bz_np_focus` |
| Includes | `BezelNPCompactBar`, `BezelMusicPlayingArt`, `BezelNPInPlace` |
| Tuner | `bz_fs_tbar_off` |

### Kodi workarounds (do not port)
- `bz_audio_latch` (debounced audio) exists because Kodi's `Player.HasAudio` drops briefly on track change.
- Proxy 6385: Kodi focus redirection trick.

## Related
[big-album](big-album.md) · [music-fanart-fs](music-fanart-fs.md) · [mm-mini-player](mm-mini-player.md) · [now-playing](now-playing.md)
