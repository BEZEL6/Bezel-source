# Big album layer

**Object:** the always-present big album / poster layer · Kodi: dialog `1122` (`Custom_1122_BigAlbum.xml`, zorder 0, modeless) · group `6400` · includes `BezelAlbumCast`, 2 × `BezelMusicPlayingArt` · expressions `bz_railvis`, `bz_railc` · Home `bz_rail`
**Where:** right of the strip (home, x 1140) or centred (x 660), over every section that shows it
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
The big playing album is one layer that lives above every section, like the dust. Changing section, opening the menu or going fullscreen never rebuilds it, so its sway, glare and dust never restart. Screens only say where it sits: home (right of the strip), centre, or hidden. It also holds the artwork group for posters (see [artwork-group](artwork-group.md)) and, while music plays, quietly keeps the artist's fanart loaded so fullscreen opens instantly.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hidden | no music and no screen that shows it; fullscreen video, slideshow, screensaver | a showing screen | nothing |
| Home | Music lists, MM over any section with music, settings / add-ons / sources with music, fullscreen fanart stage | centre request | album at x 1140, swaying |
| Centre | Dialogue FS, fullscreen album view | back to home | album at x 660, swaying |
| Splash | app start | splash fade | album loads hidden and dissolves in with the splash |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| home ↔ centre | one continuous slide of 480 px, both directions | 280 default (480 / 380 / 280 / 180) | sine in-out |
| app start | album dissolves in with the splash's own fade | 3000 | sine |
| dims | MM dim / global dim apply to the album exactly like section content | 600 | sine |
| art change | new cover crossfades over the old | image fade | — |

### Interruptions
- A centre request while sliding home (or the reverse): the slide reverses from its current position.
- Section change mid-slide: the slide completes; nothing restarts.

### Continuity
- The album is never removed and re-added while its screen family stays up: the sway, glare, lit dust, cast and the inner fade-ins never replay (5.33.309 fixed a remount that left ~1 s with no album).
- Home ↔ centre is never a fade and never leaves a gap: the arriving copy is on screen from the first frame.
- Sway phase is shared with the poster (see [sway-animations](sway-animations.md)).

### Layering
Below: the section window. In the layer, back → front: fanart preload (3 %) · cast shadow · album art (+ glare, lit dust) · compact NP bar under the album · NP bar under the centred album. Above: fullscreen chrome, MM chrome, dialogs.

### Geometry
| Piece | Value |
|---|---|
| Album home | x 1140, y 220, 600 × 600 |
| Album centre | x 660 (home − 480) |
| Cast shadow | mounted once, outside the album, follows its sway |
| Fanart preload | stage x 120, 930 × 900, 3 % |

### Art
- Playing album cover (or the focused item's poster through the artwork group).
- No art → nothing drawn; no default cover (276).
- The preload draws the playing artist's fanart, scaled to cover, background-loaded.

### Input
None. The layer never takes keys. Touch: tapping the album in Music opens Dialogue FS.

### Speed targets
Slide ≤ 280 ms by default; art on screen with the splash, not after.

### Never
- No remount on section change (5.33.309).
- No fade or gap on home ↔ centre.
- No album pop after the splash (412).
- No art left invisible after the splash (417).

### Acceptance checks
1. Music → Movies → Music with a song playing and the MM open: album never blinks or restarts its swing.
2. Dialogue FS open / close: one smooth slide each way.
3. Cold start: album appears with the splash fade.
4. Start a video fullscreen: album gone; stop: back, swaying.

## Kodi implementation (sandbox)

### How it works
- **Modeless dialog with a `<visible>` tag** (Intent: global layer). `!fullscreenvideo + !slideshow + !screensaver + !1113`; Kodi opens it by itself. Modeless dialogs get no key actions, so nothing focusable lives inside. Touch reaches button 6180 (tap → `bz_rail=centre` + `ActivateWindow(1120)` when `bz_pndlg_ok`).
- **Shown when `$EXP[bz_railvis]`:** `bz_mmaudio` · MM open on the Music row with `bz_vmus` · music info dialogs · music / playlist windows on artists / albums / songs · `bz_mmmushide` (MM open with audio) · Kodi FS · 1120 · 1121 · audio + `bz_setkids` (settings / add-ons / sources) unless Tuner Album art during music = Off; and `bz_rail` ≠ `hide`.
- **Two copies** (Intent: never remount), each with its own real `left` so each sway camera is right at rest; both always "visible":
  - home copy (left 0, x 1140): Conditional slide −480 while `$EXP[bz_railc]`, alpha 0 at the end of the slide (fade 0 ms, delay = slide time).
  - centre copy (left −480): parked home (+480 while `!bz_railc`) under alpha 0; WindowOpen holds it at 0 for 600 ms.
  - `bz_railc` = `bz_rail` = `centre`, or (1121 or Kodi FS) + album view (`bz_pnoff` ≠ 1). Slide time from `bz_at_fsslide` (1 / 2 / empty-3 / 4 = 480 / 380 / 280 / 180).
- **Dims:** the `bz_railvis` group takes `BezelSecDim` (`bz_at_mmdim`, `bz_at_gdim`).
- **Splash:** group 6400 holds at alpha 0 (Conditional `start=100 end=0 time=0`) while `bz_warm_gate`; fades in 3000 ms when it clears.
- **Fanart preload (472):** image at the start of `<controls>`: `bz_stage_x`, `bz_stage_w` × 900, scale, background, `colordiffuse 03FFFFFF`, `Player.Art(artist.fanart)`; visible `Player.HasAudio + !Player.HasVideo + !Window.IsVisible(1121) + !Window.IsActive(visualisation)`.
- **NP bar under the centred album (VIZNPBAR):** `[viz | Window.IsVisible(1121)] + bz_fsnp + bz_railc + Player.HasAudio`, 600 ms in after 480, 300 out (see [np-bar](np-bar.md)).

### Wiring
| Piece | Where |
|---|---|
| `bz_rail=centre` | 1120 onload; 6390 Select / Right, 6180 tap and 1115 Right just before `ActivateWindow(1120)` |
| `bz_rail=home` | 1120 onunload |
| `bz_rail=hide` | free; nothing sets it |
| Fullscreen centre | follows `bz_pnoff` live |
| Expressions | `bz_railvis`, `bz_railc`, `bz_mmmushide`, `bz_mmaudio`, `bz_setkids`, `bz_pndlg_ok` |
| Tuner | `bz_at_fsslide`, `bz_at_warmmusicposters`, `bz_at_mmdim`, `bz_at_gdim` |

### Kodi workarounds (do not port)
- Two parked copies with alpha tricks: Kodi can't animate a control's position without restarting its children's animations when visibility flips. A port moves one album.
- The reversed-Conditional hold `start=100 end=0 time=0`: a reversed Kodi Conditional rests at its start value (417).
- The 3 % preload image: Kodi has no texture prefetch call.
- A dialog for a global layer: Kodi has no app-wide overlay.

## Related
[artwork-group](artwork-group.md) · [sway-animations](sway-animations.md) · [dialogue-fs](dialogue-fs.md) · [music-fanart-fs](music-fanart-fs.md) · [np-bar](np-bar.md) · [dust](dust.md) · [home-splash](home-splash.md)
