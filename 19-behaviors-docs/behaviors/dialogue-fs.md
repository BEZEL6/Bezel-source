# Dialogue FS

**Object:** `Custom_1120_PlayNext.xml` dialog `1120` · main `6400` (660,220, 600×600) · **big album pill** `6401` (shared `BezelBigAlbumPill`) · touch sides `6405`/`6406` · side albums `BezelFSPlayNext` · album grouplist `6397`  
**Where:** Music section, over the left fanart stage  
**Last updated:** 2026-11-01 · 5.33.221
**Status:** draft. This doc matches the live tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** Tap the big album in Music, or press Right from Music controls, and the album slides out to a full-screen album view. Back slides it home again.

**How it works.** From the Music section, Right or Select on the NP control `6390` (when `$EXP[bz_pndlg_ok]`) first focuses the album rail button for the current slide speed (6369/6379/6399/6384), then `ActivateWindow(1120)`. The left stage then slides -1100 px at the Tuner slide speed. On Back, 6400 sets the `bz_fsret` latch, which holds the LeftStage off-frame for about 1 s, and then closes 1120. That lets the side fade (600 ms) finish before the reverse slide starts, so no half-faded album slides back. On unload, focus goes back to the rail button that matches the slide speed, so the strip lands on the same row it left from.

**Wiring.**
- `onload` (empty `bz_dfs_mode`) → `Skin.SetString(bz_dfs_mode,album)`.
- `onunload`: clear `bz_pnfoc`, `bz_pnsel`. Then `AlarmClock(bz_pvret,SetFocus(N),00:00,silent)` with N by `bz_at_fsslide`: 1→6368 · 2→6378 · 3/empty→6398 · 4→6383.
- 6400 `onback`: `SetProperty(bz_fsret,true,home)` · `AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)` · `Dialog.Close(1120)` (5.33.105 t717).

## Keys

**Simple.** Select pauses or resumes and shows a ghost logo. Left and Right change song. Up goes to the big album pill. Down does nothing.

**How it works.** Select checks whether the player is paused before toggling. Going into pause sets `bz_pnfoc=6403`, which shows the pause logo. Resuming clears it. The CEC-repeat guard of 5.33.115 was replaced by this single action (5.33.116 t807).

**Wiring.**
| Key | 6400 |
|---|---|
| Select | `!Player.Paused` → `SetProperty(bz_pnfoc,6403,home)`; paused → `ClearProperty(bz_pnfoc,home)`; then `PlayerControl(Play)` |
| Left / Right | `PlayerControl(Previous)` / `PlayerControl(Next)` |
| Up | `6401` |
| Down | `SetProperty(bz_noop,1,home)` (noop) |
| Back | fsret latch + close (above) |
| `onfocus` | `ClearProperty(bz_pnfoc,home)` |

## Big album pill 6401

**Simple.** Upper right: ALBUM ↔ PREV/NEXT. Select, Left or Right flips it. Up or Down returns to 6400. Back closes 1120 with the same latch. Full spec: big-album-pill.md. It is not the fan art pill `6391`.

**Wiring.** `<include content="BezelBigAlbumPill"><param name="main" value="6400"/><param name="back_close" value="1"/></include>`.

## Side albums (Play Next)

**Simple.** In PREV/NEXT mode the previous and next albums fade in at the sides after 3 seconds.

**Wiring.** `BezelFSPlayNext` with `vis=Player.HasAudio`, `sdelay=3000`, `sfade=2000`, `sides=!String.IsEqual(Skin.String(bz_dfs_mode),album)`. These are the same defaults as FS album viz. Touch: 6405/6406 play that side song (mouse only, keys never land there, 5.33.117 t815).

## Touch

**Simple.** The BEZEL logo is Back. Cast is gated on Cover. Pause and cast work the same as Play Next.

## Slide speed (shared)

**Simple.** One Tuner setting sets how fast the stage slides.

**How it works.** The same string drives the Dialogue FS slides (Includes_Bezel ×2, Custom_1112) and viz preview-next (MusicVisualisation ×2), so they stay in sync. Kodi `scrolltime` cannot be conditional, so album grouplist `6397` gets four speed-gated rails (5.33.165). The default, mid-high, uses 6397/6398/6399.

**Wiring.** Tuner › FULLSCREEN MUSIC › VIZ › Slide speed `bz_at_fsslide`: 1 Slow 480 ms · 2 Mid-low 380 · 3/empty Mid-high 280 (default) · 4 Fast 180. Compact Music NP rides 6397 (5.33.121), so album and NP move as one.

## Pause logo

**Wiring.** `bezel/logo_pause.png` (BEZEL logo with centred pause bars, 5.33.167), 111 px (~35 %) at 245,245, centred on the 600 px album (5.33.166). `logo.png` is unchanged.

## Related
big-album-pill.md · play-next.md · music-controls.md · fullscreen-pill.md · fanart-fs.md

## Touch: big album tap (5.33.221)
- Button `6180` (Includes_Bezel `BezelMusicPlayingArt`, left 1140 top 220, 600×600; visible while `bz_audio_latch` and no back/flip anim) now has the same Dialogue FS onclicks as remote 6390 when `$EXP[bz_pndlg_ok]`: SetFocus fsslide slot (`bz_at_fsslide` 1→6369, 2→6379, empty/3→6399, 4→6384) then `ActivateWindow(1120)`. When `bz_pndlg_ok` is false the tap does nothing.
