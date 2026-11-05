# Fanart FS (Kodi visualisation window)

**Object:** Kodi's fullscreen music window · Kodi: `MusicVisualisation.xml` (`visualisation`) · main `6390` (`BezelNPInPlace`, 120,120 840×900) · cycle pill `6391` · big album pill `6401` · Back router `6297` · redirects `6299`, `6385`, `60` · touch `6407`–`6410`
**Where:** fullscreen music when Bezel's own fullscreen ([music-fanart-fs](music-fanart-fs.md)) can't be used
**Last updated:** 2026-11-04 · 5.33.474 · **Status:** live (fallback) · **Lock:** none. **Rob rule:** every change here is made to Music Fanart FS in the same build, and the reverse; alert Rob that it applies to both.

## Simple
This is Kodi's own fullscreen music screen, dressed to look and work exactly like Bezel's fullscreen music: the fanart stage, the swaying big album, the meta and progress bar, the six-mode cycle pill, double-Select for album view, Back to the fanart and Back again to leave. Bezel now uses its own fullscreen almost everywhere; this screen stays only where Bezel's can't be hosted (Settings, PVR and other Kodi screens) or when Bezel's fullscreen is switched off. When a remote app, an add-on or Kodi's own FullScreen action opens it over Music, Home, Movies / TV, Pictures, Programs or Add-ons, it hands over to Bezel's fullscreen at once (behind a black cover).

## Feel contract (any framework)
A port has **one** fullscreen music screen: build [music-fanart-fs](music-fanart-fs.md). This screen must match it. The only allowed differences are listed here.

### States
Same as Music Fanart FS: Fanart stage · Album view · Cycle mode · Up Next list · Controls · Closed.

### Timeline
Same as Music Fanart FS (open 300 ms fade, progress grows 2000 ms from 150 ms, album-to-centre slide on the fullscreen rail, NP bar 600 ms after 480 ms). Close: 300 ms chrome + 600 ms screen fade-out.

### Interruptions
Same as Music Fanart FS. Back during album view → fanart stage with no exit animation; Back on the fanart stage → leaves.

### Continuity
- **Difference (Kodi only):** opening this window restarts the album sway (the window replaces the section). Bezel's own fullscreen exists to avoid exactly this; a port must not copy the restart.
- Everything else matches: no reload flash of the fanart, return to the same row.

### Layering
Kodi FS window (fanart stage, meta, pills) < big album layer (album, sides, sway, NP bar under the centred album).

### Geometry
Same as Music Fanart FS: cycle pill 140,136 left-aligned; "press down to open" hint 140,172; meta 150,196 / 150,226; progress 150,296 780×32; album home 1140 / centre 660.

### Art
Same as Music Fanart FS.

### Input
Same as Music Fanart FS. Right = next song everywhere on this screen (taken by the keymap before any control sees it).

### Speed targets
Same as Music Fanart FS.

### Never
- Same as Music Fanart FS.
- No old cycle pill in the upper-right corner on return from the big album (465 OLDPILL).
- No bounce back into the Music window (the old toggle-off path, removed t1584).

- No drop shadows behind the overlay text, pills or transport bar (473 FSSHADOWDEL).
### Acceptance checks
1. Open Kodi Settings with music playing → Tab → this screen; it looks identical to Bezel fullscreen.
4. From a phone remote, press fullscreen while in Movies with music playing → black for a moment, then Bezel fullscreen; Back → Movies.
2. Double-Select → album view; Back → fanart; Back → Settings.
3. No pill in the top-right at any point.

## Kodi implementation (sandbox)

### How it works
- **When it opens.** Any `ActivateWindow(visualisation)` / `Action(FullScreen)` with audio: Bezel openers when `$EXP[bz_m1121ok]` is false (window outside `bz_fs1121win`, kill switch `bz_m1121_off`), 1121's own onload redirect, Tuner `fsctrl` Back with 1121 not allowed, and outside callers (remote apps, add-ons, Kodi FullScreen).
- **Hand-over (474 VIZREDIR, Intent: one fullscreen).** `$EXP[bz_vizredir]` = `!bz_m1121_off + Player.HasAudio + !Player.HasVideo + Window.Previous(music | home | videos | pictures | programs | addonbrowser)` (Window.Previous is set before WINDOW_INIT, so it is valid in onload; Bezel's own openers never produce this case). Onload then sets Home `bz_vizredir` (black 1920 × 1080 cover on top), skips the sway restart and the 6390 focus alarm, and focuses 6297 (with `bz_pnoff=1` = `Action(Back)` → previous window). Onunload queues `ActivateWindow(1121)`; 1121 onload clears `bz_vizredir`.
- **onload:** keymap refresh (`bz_cmd.py keymap`), `bz_pnoff=1` (fanart), `bz_dfs_mode` defaults to `album`, `bz_fsnp`, `bz_np`, `AlarmClock(bz_fsfoc,SetFocus(6390))`, start bz_flip if needed, **`bz_sway_restart=true`** (album re-zeroes).
- **onunload:** clear `bz_np` (if `bz_fsnp`), `bz_fsnp`, `bz_pnoff`, `bz_pnfoc`, `bz_vdtap`; `bz_gridret` 3 s; MM closed and not opened from the MM → `AlarmClock(bz_vizret,SetFocus(60))`; opened from the MM (`bz_fsmm`) → bz_flip reopens the MM.
- **Two views.** `bz_pnoff=1` = fanart stage; empty = album view. Back is keymapped to `SetFocus(6297)`; 6297 onfocus: album view → `bz_pnoff=1`, else `Action(Back)`; then focus 6390.
- **Select on 6390.** Fanart: 1st arms `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01)` + `bz_vdtap=1`; 2nd within 1 s cancels and clears `bz_pnoff`. Album view: pause / resume + `bz_pnfoc=6403` ghost logo.
- **Cycle pill 6391.** Shown only with `Window.IsActive(visualisation)` + fanart stage (465 OLDPILL), params `pillx/pilly/pillal` = 140 / 136 / left. Mode in `Skin.String(bz_npmode)`, label flash `bz_npmlabel` 2 s. Down: Controls → `ActivateWindow(1115)`, Up Next → 6396, else 6390.
- **Shared with 1121:** `BezelFSMeta`, `BezelBigAlbumPill` (`vis=[!bz_pnoff=1] + Player.HasAudio`, `main=6390`), `BezelFSPlayNext` (sdelay 0, sfade 2000, `sides=!album`), `BezelFSUpNext`, `BezelNPControls`, the fanart-mode chrome hide (`bz_fschrome_fan`). The old `BezelNPInPlace` title / thin progress is hidden while viz is active.
- **Album view in 1122.** Same rail as 1121: 1122 slides the album −480 (`bz_at_fsslide`), VIZNPBAR under it.

### Wiring
| Control / key | Action |
|---|---|
| 6390 Select | see above |
| 6390 Left | `PlayerControl(Previous)` |
| Right (keymap `<visualisation>`) | `PlayerControl(Next)` |
| 6390 Up | fanart → 6391; album view → 6401 |
| 6390 Down | `bz_noop` |
| 6390 onback | `ClearProperty(bz_np)` + 6299 |
| Back / backspace (keymap) | `SetFocus(6297)` |
| M / RED (keymap) | `ActivateWindow(1115)` |
| long return / enter | PlayPause |
| Touch 6407–6410 | onfocus `SetFocus(6390)`; 6409 click = pause, double = album view |
| Keymap file | `resources/keymaps/bezel2_np_tab.xml` → `zz_bezel2_np_tab.xml` |
| Open / close fades | WindowOpen 300; WindowClose 300 + 600 |

### Kodi workarounds (do not port)
- The whole screen: a port has one fullscreen music screen, not a Bezel one plus Kodi's.
- `bz_sway_restart` on open: needed in Kodi because the window switch tears down the album's timing context.
- `AlarmClock(bz_fsfoc…)` focus on the next tick, the 6297 Back router, the 1 s alarm double-tap.
- `bz_fsbounce` and `bz_cmd.py vistoggle` legacy names: no longer used for a bounce.

## Related
[music-fanart-fs](music-fanart-fs.md) · [big-album](big-album.md) · [big-album-pill](big-album-pill.md) · [play-next](play-next.md) · [np-bar](np-bar.md) · [music-controls](music-controls.md) · [keymaps](keymaps.md)
