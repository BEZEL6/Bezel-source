# Fanart FS (visualisation)

**Object:** `MusicVisualisation.xml` (Kodi `visualisation`) · default `6390` (BezelNPInPlace, Includes_Bezel ~2896, 120,120, 840×900) · **fan art pill** `6391` (~2956, fanart only) · **big album pill** `6401` (album viz) · hidden redirects `6297`, `6299`, `6385`, `60` · touch `6407`/`6408`, `6409`/`6410`  
**Where:** Full-screen music  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live tree. 6409 click = pause, double = album viz. Right = next via keymap (5.33.205). Rob has not approved it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Two views

**Simple.** Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.

**How it works.** One Home prop decides the view: `bz_pnoff=1` means plain Fanart FS (sides off). Empty means album viz. `onload` always sets `bz_pnoff=1`, so every visit starts in fanart. Back is routed by the keymap to `6297`. If album viz is showing, 6297 sets `bz_pnoff=1` (drop to fanart, no exit anim). If fanart is already showing, it runs a real `Action(Back)` (5.33.108 t732).

**Wiring.** `6297` `onfocus`: `!bz_pnoff=1` → `SetProperty(bz_pnoff,1,home)`, else `Action(Back)`. Then `SetFocus(6390)`.

## Open / close

**How it works.** If viz opens straight from the Music window, the music playlist or 1112 (Kodi auto-viz), it is a bounce: the skin toggles viz off and replaces the window with Music. A fresh open sets the NP props, starts `bz_flip` if needed and focuses 6390 on the next tick.

**Wiring.**
- `onload` from music/musicplaylist/1112 → `bz_fsbounce=1` (cleared 1 s) · `bz_cmd.py vistoggle` · `ReplaceWindow(Music)`.
- `onload` always → `bz_cmd.py keymap` · `bz_pnoff=1` · `bz_dfs_mode=album` if empty.
- `onload` fresh → `bz_fsnp=true` · `bz_np=true` · `AlarmClock(bz_fsfoc,SetFocus(6390),00:00,silent)` · `RunScript(bz_flip.py)` if `bz_flip_running` is not true · `bz_sway_restart=true`.
- `onunload` → clear `bz_np` if `bz_fsnp` · if `!$EXP[bz_navmenu]` `AlarmClock(bz_vizret,SetFocus(60),00:00,silent)` · clear `bz_fsnp`, `bz_pnoff`, `bz_pnfoc`, `bz_vdtap` · `bz_gridret=1` for 1 s.
- `6299` `onfocus` → `ClearProperty(bz_np,home)` + `Action(Back)`. `6385` → focus 6390 + `bz_cmd.py npctl,toggle`. `60` → focus 6390.

## Keys

**Simple.** Select pauses (one tap) or opens album viz (two taps). Left = previous song. Right = next song, everywhere. Up = the pill. M/RED = Music controls.

**How it works.** In fanart, the first Select does not pause at once. It arms a 1 s alarm that pauses and sets `bz_vdtap=1`. A second Select inside that second cancels the alarm and clears `bz_pnoff` (album viz). `bz_vdtap` clears after 1 s either way. There is no `NextPreset` on this path. In album viz, Select pauses at once and shows the ghost logo. Right is taken by the keymap before the skin sees it, so the XML `onright` handlers of 6390 and 6391 never fire in viz.

**Wiring.**
| Key | Behavior |
|---|---|
| Select on 6390, fanart | 1st: `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01,silent)` + `bz_vdtap=1`. 2nd within 1 s: `CancelAlarm(bz_vdtapgo,true)` + `ClearProperty(bz_pnoff)` + `bz_vdtap=2` |
| Select on 6390, album viz | `!Paused` → `bz_pnfoc=6403`, else clear. Then `PlayerControl(Play)` |
| Left on 6390 | `PlayerControl(Previous)` |
| Right (anywhere) | keymap `<visualisation>` → `PlayerControl(Next)` |
| Up on 6390 | `bz_pnoff=1` → `6391`, else `6401` |
| Down on 6390 | `bz_noop` (noop) |
| M / RED | `ActivateWindow(1115)` (keymap) |
| Back | keymap → `SetFocus(6297)` |
| 6390 `onback` | `ClearProperty(bz_np)` + `6299` |

## Fan art pill 6391

**Simple.** The **fan art pill** shows only in plain fanart. It cycles what the right side shows: Visualizer → Bio → Fanart → Lyrics → Up Next → Controls. In Controls, Select or Down opens Music controls.

**How it works.** Select only sets the mode and stays on the pill (O78). The mode name flashes for 2 s through `bz_npmlabel`. Left in viz also cycles the pill (it is a SendClick). A "press down to open" hint shows only in Controls mode.

**Wiring.**
- `Skin.String(bz_npmode)`, label `$VAR[BezelNPModeName]`, `bezel/np_pill32.png` with `BzFSCTint50/80`.
- `onclick`: `bz_npm_ctl` → `ActivateWindow(1115)`. vis→bio, bio→fanart, fanart→lyrics, lyrics→upnext, upnext→controls. Then `bz_npmlabel=1` with `AlarmClock(bznpml, clear, 00:02)`.
- `ondown`: Controls → 1115, else 6390. `onup` 6390. `onleft` in viz → `SendClick(6391)`. `onback` → clear `bz_np` + 6299.

## Big album pill 6401

**Simple.** It shows only in album viz: ALBUM ↔ PREV/NEXT. See big-album-pill.md.

**Wiring.** `BezelBigAlbumPill` with `vis=[!bz_pnoff=1] + Player.HasAudio`, `main=6390`. Sides: `BezelFSPlayNext` `sdelay=3000`, `sfade=2000`, `sides=!album`, the same as 1120.

## Touch

**Wiring.**
- `6410` (960,0, 960×1080, fanart, `bz_npctl` not true) → `Skin.SetString(bz_npmode,upnext)`.
- `6409` (1100,220, 680×680) → `onclick PlayerControl(Play)` · `ondoubleclick ClearProperty(bz_pnoff,home)` (5.33.205).
- `6407`/`6408` (album viz + PREV/NEXT + neighbour exists) → `Playlist.PlayOffset(music,∓1)`.
- Every touch button has `onfocus SetFocus(6390)`, so keys never land on them.

## Keymap

**Wiring.** `resources/keymaps/bezel2_np_tab.xml` → installed `zz_bezel2_np_tab.xml` by `bz_cmd.py keymap` (Music and viz onload). `<visualisation>`: Right → `PlayerControl(Next)` · Back → `SetFocus(6297)` · M/RED → 1115 · Select → Select · longpress return → PlayPause · gamepad/joystick mapped to match (keymaps.md).

## Naming
- **Fan art pill** = `6391` only (6-mode `bz_npmode`), full screen **fanart** only.
- **Big album pill** = `6401` / `bz_dfs_mode`, on Dialogue FS **and** FS album viz.

## Related
big-album-pill.md · play-next.md · fullscreen-pill.md · music-controls.md · keymaps.md · dialogue-fs.md
