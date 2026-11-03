# Fanart FS (visualisation)

**Object:** `MusicVisualisation.xml` (Kodi `visualisation`) · default `6390` (BezelNPInPlace, Includes_Bezel ~2896, 120,120, 840×900) · **fan art pill** `6391` (~2956, fanart only) · **big album pill** `6401` (album viz) · hidden redirects `6297`, `6299`, `6385`, `60` · touch `6407`/`6408`, `6409`/`6410`  
**Where:** Full-screen music  
**Last updated:** 2026-11-02 · 5.33.377
**Status:** draft. This doc matches the live tree. 6409 click = pause, double = album viz. Right = next via keymap (5.33.205). Rob has not approved it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Two views

**Simple.** Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.

**How it works.** One Home prop decides the view: `bz_pnoff=1` means plain Fanart FS (sides off). Empty means album viz. `onload` always sets `bz_pnoff=1`, so every visit starts in fanart. Back is routed by the keymap to `6297`. If album viz is showing, 6297 sets `bz_pnoff=1` (drop to fanart, no exit anim). If fanart is already showing, it runs a real `Action(Back)` (5.33.108 t732).

**Wiring.** `6297` `onfocus`: `!bz_pnoff=1` → `SetProperty(bz_pnoff,1,home)`, else `Action(Back)`. Then `SetFocus(6390)`.

## Open / close

**Simple.** Fanart FS is always Kodi's real fullscreen music window, from every section including Music. Same look, same keys everywhere.

**How it works.** Every open of `visualisation` (MM FULL pill, Tab, 1112 auto-viz, any `ActivateWindow(visualisation)`) stays on `MusicVisualisation.xml`, so the `<visualisation>` keymap always applies. The old Music bounce (opened from music/musicplaylist/1112 → toggle viz off, `ReplaceWindow(Music)` with the in-place 6390 panel) was removed (t1584). Each open sets the NP props, starts `bz_flip` if needed and focuses 6390 on the next tick.

**Wiring.**
- No `Window.Previous` gating; `bz_fsbounce` is never set now (the list-60 cover-column fade checks in `Includes_Bezel.xml` treat it as empty). `bz_cmd.py vistoggle` is unused.
- `onload` always → `bz_cmd.py keymap` · `bz_pnoff=1` · `bz_dfs_mode=album` if empty.
- `onload` every open → `bz_fsnp=true` · `bz_np=true` · `AlarmClock(bz_fsfoc,SetFocus(6390),00:00,silent)` · `RunScript(bz_flip.py)` if `bz_flip_running` is not true · `bz_sway_restart=true`.
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

**How it works.** Select only sets the mode and stays on the pill (O78). The mode name flashes for 2 s through `bz_npmlabel`. On 1121 the pill (6421) Left = previous, Right = next mode, wrapping all six (5.33.287). A "press down to open" hint shows only in Controls mode.

**Wiring.**
- `Skin.String(bz_npmode)`, label `$VAR[BezelNPModeName]`, `bezel/np_pill32.png` with `BzFSCTint50/80`.
- `onclick`: `bz_npm_ctl` → `ActivateWindow(1115)`. vis→bio, bio→fanart, fanart→lyrics, lyrics→upnext, upnext→controls. Then `bz_npmlabel=1` with `AlarmClock(bznpml, clear, 00:02)`.
- `ondown`: Controls → 1115, else 6390. `onup` 6390. `onleft` in viz → `SendClick(6391)`. `onback` → clear `bz_np` + 6299.

## Big album pill 6401

**Simple.** It shows only in album viz: ALBUM ↔ PREV/NEXT. See big-album-pill.md.

**Wiring.** `BezelBigAlbumPill` with `vis=[!bz_pnoff=1] + Player.HasAudio`, `main=6390`. Sides: `BezelFSPlayNext` `sdelay=0` (5.33.317, was 3000), `sfade=2000`, `sides=!album`, the same as 1120.

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

## Music Fanart FS 1121 (5.33.210)

**ALERT RULE (Rob):** before making any Fanart FS or 1121 change, alert Rob that it applies to BOTH (Kodi Fanart FS `MusicVisualisation.xml` and Music Fanart FS 1121).

**STANDING (Rob):** every change to Fanart FS applies to Music dialog **1121** in the same build (shared includes / same wiring — see music-fanart-fs.md). In Music, pills 6886/6960/6910, Tab and Tuner fsctrl Back open 1121 instead of this window (`$EXP[bz_m1121ok]`); every other section still opens `visualisation`.


## 5.33.277
Music Fanart FS (1121) now draws its own meta block + pill→progress; the shared BezelNPInPlace title/progress overlay hides only while 1121 is visible. See music-fanart-fs.md.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/fanart-fs.md) · [state](../state/fanart-fs.md) · [motion](../motion/fanart-fs.md) · [art](../art/fanart-fs.md) · [input](../input/fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.302 current state (Music Fanart FS 1121)
- Pill→progress bar (FSMETA, 150,296): the fill `progress` now has a real clear `texturebg` (np_pill32, border 12, 00FFFFFF) so Kodi scales the fill to the 24px track inside the 780×32 pill. (Empty texturebg left the fill at native 32px height, off-centre below the pill — worst at low % / long files / paused entry.)
- Old Fanart-FS cycle-pill **shadow** grouplist (530,130, BzFSShSlide L1 + 4 rings) is gated exactly like pill 6391: hidden while 1121 is visible and in album viz. 1121 draws its own cycle pill 6421 at 140,136 (no shadow).

## 5.33.306 — exit fade only outside Music Level 3 (Rob pt2304u)
- The Fanart FS (1121) exit fades (300 ms and 600 ms WindowClose) now only play when the music window underneath is not on Level 3. Level 3 is detected with the skin's existing bz_m13 check: music window, songs content, path starting musicdb://artists/.
- Leaving Fanart FS onto the Level 3 song list closes it straight away, with no fade. Everywhere else it fades as before.

## 5.33.307 — album viz sway (Rob)
- Fanart FS album viz centres the album with a real left -480, so the sway camera moves with the album and the tip doesn't freeze. Details are in sway-animations.md.


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## 5.33.314 — cycle pill Down (6391, BezelNPInPlace)
- Controls mode → `ActivateWindow(1115)`; Up Next mode → focus Up Next list proxy 6396; any other mode → 6390. 6396 Up from first row returns to 6390 (unchanged).

## Fanart cycle mode hides chrome (5.33.314 Fix D, Rob t2385/t2386)
When the cycle pill is on **Fanart** (`$EXP[bz_npm_fan]`) and Tuner `bz_fschrome_fan` is **unset** (default "A Hide"), these fade out (300ms sine Conditional):
- BezelNPInPlace title/artist/album group and progress+time group (Music / MusicVisualisation path).
- 1121 FSMETA: artist/album meta block and pill-row→progress strip.
**Stay visible:** the 6-mode cycle pill (6391 + its shadow grouplist in NPInPlace; 6421 on 1121) and the transport bar (prev/next triangles at the bottom of the colour block, `bz_fs_tbar_off` group). The prev/next song-title pills (226×32 at 128 / 726, y981) use the same chrome as cycle pill 6391: `bezel/np_pill32.png` border 16, `BzFSCTint50` fill, `bz_b15` text in `BzFSCTint`, live shadow/ring copies kept; whole bar still static 50% (K43), plus BezelFSPlayNext neighbour tiles on 1121.
Tuner "Keep" (`bz_fschrome_fan` set) keeps all chrome. The fade used to sit on the whole NPInPlace text wrapper (t4326b), which also hid the pill and transport bar — moved onto the two child groups.
Down on 6421 in Up Next focuses 1121's own Up Next proxy **6396** (list **6395**), from shared include `BezelFSUpNext` mounted inside 1121 (5.33.315). Up from the first row / Left / Back return to **6421**; Down/Up move the list; Select plays via `bz_cmd.py upnext_goto`. Controls → 1115; other modes → 6420. The Music-window copy hides while 1121 is visible (`!Window.IsVisible(1121)`).


## Up Next include (5.33.315)
Up Next list 6395 + proxy 6396 now live in shared include `BezelFSUpNext` (params `vis`, `home`, `upc1-3`). BezelNPInPlace mounts it with home 6390 and `!Window.IsVisible(1121)`; Music Fanart FS 1121 mounts its own copy with home 6421. Visualisation path unchanged.

## DustViz layer (5.33.352)
- Bottom layer of the window is `BezelDustViz` (Includes_Bezel.xml): `visualisation` control id **6399**, full 1920×1080, drawn **behind** all Bezel chrome. Same include in Dialogue FS 1120, Music Fanart FS 1121 and MusicVisualisation — one place to change.
- Visible: `Player.HasAudio + !Player.HasVideo + System.HasAddon(visualization.bezel) + !Skin.HasSetting(bz_dustviz_off)`; 400ms fade-in.
- The viz (visualization.bezel) only paints its rect from Kodi's audio bins; no input, no focus, no skin access. Skin → viz triggers only via Home properties.
- Install: Startup runs `scripts/bz_dustviz.py` — copies bundled `resources/dustviz/<android|linux>/visualization.bezel` into special://home/addons when the version differs, UpdateLocalAddons, enables it, sets `musicplayer.visualisation`, sets Home `bz_dustviz_ok`. Windows: no binary, skipped (logged).
- Kill switch: `Skin.SetBool(bz_dustviz_off)`.

## 5.33.377 — layout matches Music Fanart FS 1121 (current)
On the fanart stage (`bz_pnoff=1`) Kodi Fanart FS draws the same chrome as 1121: shared include `BezelFSMeta` (small ARTIST · ALBUM 150,196 `bz_mm18s`; big SONG TITLE 150,226 `bz_mm34`; year pill zooms into 780×32 progress at 150,296, 25% bar, time/duration in at 2100 ms; genre pill fades). BezelNPInPlace's old title/artist/album + thin progress/time overlay is hidden while `visualisation` is active (as for 1121). Cycle pill 6391 sits at 140,136 left-aligned (NPInPlace params `pillx/pilly/pillal`, defaults 530/130/right for other hosts), no live-shadow copies in viz; "press down to open" hint 140,172 left. Tuner `bz_fs_ttl_off` / `bz_fs_prog_off` / `bz_fs_pill_off` / `bz_fschrome_fan` act on the shared block. Keys/pill cycle logic unchanged (6391 Select-on-Controls still opens 1115; 6421 L/R cycles).


## Exit rule (5.33.378)
- FS opened **from MM** (MM open, or MM closed by the opener <0.8 s before FS): `bz_fsmm` latches (bz_cmd tab/np + bz_flip FS rise edge). On FS exit bz_flip reopens MM (`bz_nav=true`, normal open path → strip 6996 on the current section row); the `SetFocus(60)` onunload alarm and fs_was list re-focus are skipped.
- FS opened **from inside a section** (list / FULLSCREEN pill 6886): exit → section list 60 (intended, unchanged).
