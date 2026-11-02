# Big album pill

**Object:** Shared include `BezelBigAlbumPill` (Includes_Bezel ~931) → button `6401` (`Skin.String(bz_dfs_mode)`), used on Dialogue FS `Custom_1120_PlayNext.xml` **and** FS album viz `MusicVisualisation.xml`  
**Where:** Upper right, grouplist at 1360,60, 500×32, aligned right  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** live on both windows. The id stays `6401`. This doc matches the live tree. Rob has not approved it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Name

**Simple.** The **big album pill** is the ALBUM ↔ PREV/NEXT mode control. It looks the same, sits in the same place and works the same on Dialogue FS and on full screen album viz. It is **not** the fan art pill (`6391`, fanart-fs.md).

## Modes

**Simple.** ALBUM shows the big album alone. PREV/NEXT also shows the previous and next albums at the sides.

**How it works.** The mode lives in one Skin.String, so it is shared across 1120 and viz and survives restarts. Both windows set `bz_dfs_mode=album` on load when it is empty, so ALBUM is the default. The side albums come from `BezelFSPlayNext` with `sides=!String.IsEqual(Skin.String(bz_dfs_mode),album)`. Their reveal uses `sdelay 0` / `sfade 2000` (5.33.317), so after a switch to PREV/NEXT the sides start fading in at once over 2 s.

**Wiring.**
| Label (`$VAR[BezelDFSModeName]`) | `bz_dfs_mode` | Sides |
|---|---|---|
| ALBUM (default) | `album` | hidden |
| PREV/NEXT | empty (`Skin.Reset`) | shown |

## Keys

**Simple.** Select, Left or Right flips the mode. Up or Down goes back to the album. Back closes Dialogue FS, or goes back to the album in viz.

**How it works.** All three toggle keys use the same two guarded actions. If the mode is `album` they reset it, otherwise they set `album`. `back_close=1` (1120 only) runs the Dialogue FS close latch: `bz_fsret=true` for 1 s, then `Dialog.Close(1120)`. The latch holds the left stage off-frame until the side fade finishes. With `back_close` empty (viz), Back just focuses `main`.

**Wiring.**
- Params: `vis` (default `[!bz_pnoff=1] + Player.HasAudio`), `main` (6400 on 1120, 6390 on viz), `back_close`.
- `onfocus ClearProperty(bz_pnfoc,home)` hides the pause ghost while the pill has focus.
- `onclick` / `onleft` / `onright`: `album` → `Skin.Reset(bz_dfs_mode)`, else `Skin.SetString(bz_dfs_mode,album)`.
- `onup` / `ondown` → `$PARAM[main]`.
- Look: font `bz_b15`, `bezel/np_pill32.png` border 16, text `$VAR[BzFSCTint]`, nofocus `BzFSCTint50`, focus `BzFSCTint80`.
- Anim: WindowOpen fade 0→100 over 600 ms after 1000 ms (sine inout). WindowClose fade over 600 ms.

## Dialogue FS (1120)

**Simple.** The pill shows the whole time the dialog is open.

**Wiring.** `<include content="BezelBigAlbumPill"><param name="main" value="6400"/><param name="back_close" value="1"/></include>`. `vis` is the default. 6400 `onup` → 6401.

## Full screen album viz

**Simple.** The pill shows only in album viz (sides mode), not in the plain fanart view, where the fan art pill 6391 sits instead.

**Wiring.** `vis=[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + Player.HasAudio`, `main=6390`. 6390 `onup` → 6401 when `bz_pnoff≠1`, else 6391. The touch side hits `6407`/`6408` (`Playlist.PlayOffset(music,∓1)`) need PREV/NEXT mode and an existing neighbour track.

## Related
dialogue-fs.md · fanart-fs.md · play-next.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Includes_Bezel.xml` include `BezelBigAlbumPill`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 6401 | button | —,— | auto×32 | `Skin.Reset(bz_dfs_mode)/Skin.Reset(bz_dfs_mode)/$PARAM[main]/$PARAM[main]` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `$PARAM[main]`
- `AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)`
- `Dialog.Close(1120)`
- `SetProperty(bz_fsret,true,home)`
- `Skin.Reset(bz_dfs_mode)`
- `Skin.SetString(bz_dfs_mode,album)`

**Source:** `xml/Custom_1120_PlayNext.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 6400 | button | 660,220 | 600×600 | `PlayerControl(Previous)/PlayerControl(Next)/6401/SetProperty(bz_noop,1,home)` | `—` |
| 6405 | button | 90,250 | 540×540 | `—/—/—/—` | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(-1…` |
| 6406 | button | 1290,250 | 540×540 | `—/—/—/—` | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(1)…` |

Actions (`onclick`/`onload`/`onback`) found:
- `AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)`
- `ClearProperty(bz_pnfoc,home)`
- `Dialog.Close(1120)`
- `PlayerControl(Play)`
- `Playlist.PlayOffset(music,-1)`
- `Playlist.PlayOffset(music,1)`
- `SetProperty(bz_fsret,true,home)`
- `SetProperty(bz_pnfoc,6403,home)`
- `Skin.SetString(bz_dfs_mode,album)`

**Source:** `xml/MusicVisualisation.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 6387 | button | 0,0 | 120×116 | `—/—/—/—` | `—` |
| 6297 | button | -400,40 | 10×10 | `—/—/—/—` | `—` |
| 6299 | button | -400,0 | 10×10 | `—/—/—/—` | `—` |
| 6385 | button | -400,40 | 10×10 | `—/—/—/—` | `—` |
| 60 | button | -400,80 | 10×10 | `—/—/—/—` | `—` |
| 6407 | button | 90,250 | 540×540 | `—/—/—/—` | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_d…` |
| 6408 | button | 1290,250 | 540×540 | `—/—/—/—` | `[!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !String.IsEqual(Skin.String(bz_d…` |
| 6410 | button | 960,0 | 960×1080 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Proper…` |
| 6409 | button | 1100,220 | 680×680 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Proper…` |

Actions (`onclick`/`onload`/`onback`) found:
- `Action(Back)`
- `AlarmClock(bz_fsfoc,SetFocus(6390),00:00,silent)`
- `ClearProperty(bz_np,home)`
- `PlayerControl(Play)`
- `Playlist.PlayOffset(music,-1)`
- `Playlist.PlayOffset(music,1)`
- `RunScript(special://skin/scripts/bz_cmd.py,keymap)`
- `RunScript(special://skin/scripts/bz_flip.py)`
- `SetProperty(bz_fsnp,true,home)`
- `SetProperty(bz_np,true,home)`
- `SetProperty(bz_pnoff,1,home)`
- `SetProperty(bz_sway_restart,true,home)`
- `Skin.SetString(bz_dfs_mode,album)`
- `Skin.SetString(bz_npmode,upnext)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/big-album-pill.md) · [state](../state/big-album-pill.md) · [motion](../motion/big-album-pill.md) · [art](../art/big-album-pill.md) · [input](../input/big-album-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
