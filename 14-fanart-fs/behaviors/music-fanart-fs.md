# Music Fanart FS (dialog 1121)

**Object:** `Custom_1121_MusicFanartFS.xml` dialog `1121` · main `6420` · fan art pill copy `6421` · Back router `6422` · touch `6426`–`6430` · big album pill `6401` (shared include)
**Where:** Music section only, over the Music window
**Last updated:** 2026-11-02 · 5.33.327
**Status:** draft — built, not smoke-tested on device. Rob locks t1589–t1595.
**Skin:** skin.bezel2

**ALERT RULE (Rob):** before making any Fanart FS or 1121 change, alert Rob that it applies to BOTH (Kodi Fanart FS `MusicVisualisation.xml` and Music Fanart FS 1121).

**STANDING (Rob):** any change to Kodi Fanart FS (`MusicVisualisation.xml`, fanart-fs.md) is applied to 1121 in the same build — shared includes / same wiring so they cannot drift. Shared: `BezelLogo`, `BezelFSPlayNext`, `BezelBigAlbumPill`, `BezelNPControls`, `BezelNPInPlace` (drawn by Music), keys/props (`bz_pnoff`, `bz_vdtap`, `bz_pnfoc`, `bz_dfs_mode`, `bz_npmode`). Any Tuner row that drives Fanart FS / visualisation also drives 1121.

## Simple
In Music, FULLSCREEN goes to a dialog copy of Fanart FS instead of Kodi's visualisation window. The Music window stays underneath, so the fanart stage and the swaying album never restart. Same look, same keys. Every other section still opens real Kodi visualisation.

## How it works
- Triggers (when `$EXP[bz_m1121ok]`: Music active, audio, no video, not viz, kill switch off): FS pill `6886`, MM FULL `6960`, old menu Full `6910`, Tab / remote Display in Music, Tuner Back with `bz_tunesrc=fsctrl`. Otherwise the same controls run `ActivateWindow(visualisation)`.
- Onload sets `bz_np=true` (Music draws `BezelNPInPlace` in place — same include and coords as viz = pixel-match), `bz_fsnp`, `bz_pnoff=1`, keymap refresh, starts bz_flip if needed. **No `bz_sway_restart`.** Closes 1112 if open.
- Play Next copied in: double-Select (or double-tap 6429) clears `bz_pnoff` → album viz. Music's stage slides -1100 (same `bz_at_fsslide` rails as 1120), sides + big album pill draw in 1121. 1120 is never opened (`bz_pndlg_ok` false while 1121 visible).
- Back: album viz → fanart; fanart → close, focus Music list `60`.
- Music's own fan art pill 6391 and FULLSCREEN pill hide while 1121 is visible; 1121's 6421 replaces 6391 in the same spot.
- Auto-close: Timers `bz_m1121stop` on `!Player.HasAudio`.
- Kill switch: `Skin.SetBool(bz_m1121_off)` → onload closes and opens visualisation.

## Wiring
| Key | 1121 |
|---|---|
| Select (6420) fanart | 1st: `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01)` + `bz_vdtap=1`; 2nd in 1 s: cancel + `ClearProperty(bz_pnoff)` |
| Select album viz | pause/resume + `bz_pnfoc=6403` ghost |
| Left / Right | `PlayerControl(Previous/Next)` |
| Up | fanart → 6421 · album viz → 6401 |
| Down | noop |
| Back / Backspace / B | `SetFocus(6422)` (keymap `<window1121>`) |
| M / RED | 1115 · Tab / Display → `Dialog.Close(1121)` |
| onunload | clear `bz_np bz_fsnp bz_pnoff bz_pnfoc bz_vdtap` · `!bz_navmenu` → `AlarmClock(bz_m1121ret,SetFocus(60))` |

## Album centre (property-driven slide, Rob t1600)
- In 1121 album viz (`Window.IsVisible(1121)` + `bz_pnoff` cleared), the playing-album group inside each Music speed rail (6367/6377/6397/6382, `BezelMusicPlayingArt`) gets a Conditional slide `-480,0` → album 1140 → 660, same distance as 1120's rail scroll. Time follows the active rail: 480/380/280/180 ms (`bz_at_fsslide` 1/2/3-default/4), sine inout.
- No focus moves into Music from the dialog. Leaving album viz (Back → fanart sets `bz_pnoff`) or closing 1121 drops the condition → Kodi reverses the slide back to 1140.
- Gated on 1121 only — real visualisation / 1120 paths unchanged (1120 still centres by focusing rail 6399).

## Related
fanart-fs.md · play-next.md · fullscreen-pill.md · mm-mini-player.md · keymaps.md · skin-settings-tuner.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Custom_1121_MusicFanartFS.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 6421 | button | —,— | auto×32 | `prev mode/next mode/6420/cycle (Select)` | `—` |
| 6420 | button | 0,0 | 1920×1080 | `PlayerControl(Previous)/PlayerControl(Next)/6401/SetProperty(bz_noop,1,home)` | `—` |
| 6422 | button | -400,40 | 10×10 | `—/—/—/—` | `—` |
| 6427 | button | 90,250 | 540×540 | `—/—/—/—` | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_d…` |
| 6428 | button | 1290,250 | 540×540 | `—/—/—/—` | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_d…` |
| 6430 | button | 960,0 | 960×1080 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Proper…` |
| 6429 | button | 1100,220 | 680×680 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Proper…` |
| 6426 | button | 0,0 | 120×116 | `—/—/—/—` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `6422`
- `ActivateWindow(1115)`
- `ActivateWindow(visualisation)`
- `AlarmClock(bz_vdtapclr,ClearProperty(bz_vdtap,home),00:01,silent)`
- `AlarmClock(bz_vdtapgo,PlayerControl(Play),00:01,silent)`
- `AlarmClock(bznpml,ClearProperty(bz_npmlabel,home),00:02,silent)`
- `CancelAlarm(bz_vdtapgo,true)`
- `CancelAlarm(bznpml,true)`
- `ClearProperty(bz_pnfoc,home)`
- `ClearProperty(bz_pnoff,home)`
- `Dialog.Close(1112,true)`
- `Dialog.Close(1121)`
- `Dialog.Close(1121,true)`
- `PlayerControl(Play)`
- `Playlist.PlayOffset(music,-1)`
- `Playlist.PlayOffset(music,1)`
- `RunScript(special://skin/scripts/bz_cmd.py,keymap)`
- `RunScript(special://skin/scripts/bz_flip.py)`
- `SetProperty(bz_fsnp,true,home)`
- `SetProperty(bz_np,true,home)`
- `SetProperty(bz_npmlabel,1,home)`
- `SetProperty(bz_pnfoc,6403,home)`
- `SetProperty(bz_pnoff,1,home)`
- `SetProperty(bz_vdtap,1,home)`
- `SetProperty(bz_vdtap,2,home)`


## FS meta + pill→progress (5.33.277, current)
**Simple.** On Music Fanart FS (1121) the top-left of the fanart shows the same meta block as the approved Music-section mock: small artist, big album, then year/genre pills. As FS opens, the first (year) pill stretches right into the Now Playing progress bar (pill-shaped, elapsed left in black, duration right); the genre pill fades away. The FULLSCREEN pill's spot (fanart upper-left) now holds the 6-cycle pill — same labels and same cycle behaviour as before, only the position moved.

**Wiring.** `Custom_1121_MusicFanartFS.xml`: meta group visible `bz_pnoff=1`; artist label 150,196 780×30 `bz_mm18s` C8FFFFFF; album 150,226 780×60 `bz_mm34` bold; pill row group 150,296. Progress group zoom WindowOpen 12%→100% x, centre 150,312, 600 ms sine, delay 150; 780×32 white np_pill32 outline over E6000000 fill, `progress` 772×24 `Player.Progress`; time labels fade in at 700 ms. Pill grouplist (year/genre, `bz_mm18s` black on white np_pill32) fades out 150–450 ms then held hidden. Tuner `bz_fs_ttl_off` hides meta, `bz_fs_prog_off` hides progress. Cycle pill 6421 grouplist moved 530,130 right-aligned → 140,136 left-aligned. `BezelNPInPlace` title/artist/album and progress overlay groups (Includes_Bezel ~L3172/3176) fade to 0 while `Window.IsVisible(1121)` (still show in MusicVisualisation).

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/music-fanart-fs.md) · [state](../state/music-fanart-fs.md) · [motion](../motion/music-fanart-fs.md) · [art](../art/music-fanart-fs.md) · [input](../input/music-fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.280 (Nov 1 2026)
- Music L2/L3 half list (bz_mhalf → bz_covercol): small album at top of strip, list under it, no big strip title (BezelArtistMeta3B hidden). Strip slide 450→510.
- Meta = FS fanart format: small artist bz_mm18s, big title bz_mm34 uppercase, outlined pills np_pill32_ol.png (also in Custom_1121 year/genre).
- FULLSCREEN pill 6886: Left from list 60 (music strip, pill visible) → 6886; Left on 6886 → list 60 + open MM; Select unchanged (1121 when bz_m1121ok, else visualisation).
- Open: L2 ALL ALBUMS row 6097/6098 not shown in half-list mode.

## FS meta pill→progress bar morph (5.33.286, Rob t2210/t2211)
- Year pill (grouplist at 150,296, h32) zooms right into the 780×32 NP bar on WindowOpen. Zoom centre fixed `150,312` → `0,16` (local to the 150,296 group — old value was double-offset, so the bar grew from the wrong origin and didn't line up with the pill). Bar now grows from the pill's left edge, same y/height.
- Extend time **2000 ms** (sine inout, delay 150; 5.33.327 Rob t2423 slowed from 1200). Time/duration labels fade in at **2100 ms** (300 ms fade). Genre pill row fade-out **1000 ms**, hard-hide **1150 ms**.
- Bar opacity lowered: ring + fill `FFFFFFFF` → `99FFFFFF` (~60%), dark inner `E6000000` → `99000000`.

### Cycle pill 6421 Left/Right (5.33.287)
With 6421 focused, **Right = next** and **Left = previous** mode, wrapping through all six: Visualizer → Bio → Fanart → Lyrics → Up Next → Controls → (Visualizer). State is `Skin.String(bz_npmode)` (vis/bio/fanart/lyrics/upnext/controls; empty = vis). Each step flashes the mode name 2 s via `Window(Home).Property(bz_npmlabel)`. Left/Right/Select/Down never open Music controls (5.33.288): Select cycles to next mode in every mode (Controls → Visualizer), Down always → 6420.

## 5.33.304 — "press down to open" hint (Rob)
- In Fanart FS the hint now sits under the cycle pill in the upper-left fanart corner (140,172, left-aligned). The old hint at 530,166 is hidden while Fanart FS is open.

## Meta text (current, 5.33.311 — Rob pt2364u)
- Small line: ARTIST · ALBUM (`MusicPlayer.Artist` + `MusicPlayer.Album`).
- Big line: SONG TITLE (`BzFSL3Big` → MusicPlayer.Title, falls back to Player.Title).
- This intentionally differs from Music L3 (L3 = artist / album). Pills unchanged.

## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## 5.33.314 — cycle pill Down (6421)
- Controls mode → `ActivateWindow(1115)`; else → 6420.
- Up Next: Down → 1121's own 6396 (BezelFSUpNext inside the dialog, 5.33.315).

## Fanart cycle mode hides chrome (5.33.314 Fix D, Rob t2385/t2386)
When the cycle pill is on **Fanart** (`$EXP[bz_npm_fan]`) and Tuner `bz_fschrome_fan` is **unset** (default "A Hide"), these fade out (300ms sine Conditional):
- BezelNPInPlace title/artist/album group and progress+time group (Music / MusicVisualisation path).
- 1121 FSMETA: artist/album meta block and pill-row→progress strip.
**Stay visible:** the 6-mode cycle pill (6391 + its shadow grouplist in NPInPlace; 6421 on 1121) and the transport bar (prev/next triangles at the bottom of the colour block, `bz_fs_tbar_off` group). The prev/next song-title pills (226×32 at 128 / 726, y981) use the same chrome as cycle pill 6391: `bezel/np_pill32.png` border 16, `BzFSCTint50` fill, `bz_b15` text in `BzFSCTint`, live shadow/ring copies kept; whole bar still static 50% (K43), plus BezelFSPlayNext neighbour tiles on 1121.
Tuner "Keep" (`bz_fschrome_fan` set) keeps all chrome. The fade used to sit on the whole NPInPlace text wrapper (t4326b), which also hid the pill and transport bar — moved onto the two child groups.
Down on 6421 in Up Next focuses 1121's own Up Next proxy **6396** (list **6395**), from shared include `BezelFSUpNext` mounted inside 1121 (5.33.315). Up from the first row / Left / Back return to **6421**; Down/Up move the list; Select plays via `bz_cmd.py upnext_goto`. Controls → 1115; other modes → 6420. The Music-window copy hides while 1121 is visible (`!Window.IsVisible(1121)`).

## Progress bar opacity (5.33.319, Rob t2399 — current)
- FS meta pill bar (1121, 780×32 at 150,296): ring `40FFFFFF`, dark inner `40000000`, fill `40FFFFFF` = **25%** (was `99` ≈ 60% since 5.33.286). Time/duration labels unchanged (100%).
