# Music Fanart FS (dialog 1121)

**Object:** `Custom_1121_MusicFanartFS.xml` dialog `1121` · main `6420` · fan art pill copy `6421` · Back router `6422` · touch `6426`–`6430` · big album pill `6401` (shared include)
**Where:** Music section only, over the Music window
**Last updated:** 2026-10-31 · 5.33.209 live tree + 1121 album-centre (not zipped)
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
