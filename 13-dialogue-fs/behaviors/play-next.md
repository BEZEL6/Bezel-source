# Play Next (1120 non-album mode)

**Object:** `Custom_1120_PlayNext.xml` dialog `1120` with `bz_dfs_mode` ≠ album · main `6400`, **big album pill** `6401` (`BezelBigAlbumPill`, Includes_Bezel ~L940), tiles `6405`/`6406` · album viz in `MusicVisualisation.xml` (same pill `6401`, `6407`/`6408`, `bz_pnoff` + `bz_dfs_mode`) · sides `BezelFSPlayNext`
**Where:** Dialogue FS (1120) over Music, and the FS album viz
**Last updated:** 2026-10-31
**Status:** Live. The big album pill toggles ALBUM ↔ PREV/NEXT on both windows, with one shared Skin.String. The prev/next side albums fade in after a 3 s delay over 2 s. Draft: not Rob-approved.
**Skin:** skin.bezel2

**Naming:** control `6401` is the **big album pill** (ALBUM ↔ PREV/NEXT). It isn't the fan art pill `6391`.

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Modes (big album pill)

### Simple
A small pill at the top right switches between **ALBUM** (just the big album) and **PREV/NEXT**, where the previous and next songs' albums show at the sides. The choice is remembered and shared between Dialogue FS and the full-screen album viz.

### How it works
- Both windows read the Skin.String `bz_dfs_mode`. `album` hides the sides, and empty (reset) shows them.
- 1120's onload sets `album` if the string is empty, so a first open defaults to ALBUM.
- Select, Left and Right on the pill all toggle the mode: Reset ↔ SetString album.
- Up and Down return to the window's main control: 6400 on 1120, 6390 on viz.
- On 1120 the pill's Back closes the dialog (`back_close=1`). On viz, Back returns to the main control.

### Wiring
| Handler (6401) | Value |
|---|---|
| onclick / onleft / onright | `bz_dfs_mode`=album → `Skin.Reset(bz_dfs_mode)` · else `Skin.SetString(bz_dfs_mode,album)` |
| onup / ondown | `$PARAM[main]` |
| onback (`back_close=1`) | `SetProperty(bz_fsret,true,home)` · `AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)` · `Dialog.Close(1120)` |
| onback (else) | `$PARAM[main]` |
| onfocus | `ClearProperty(bz_pnfoc,home)` |
| 1120 onload | `String.IsEmpty(Skin.String(bz_dfs_mode))` → `Skin.SetString(bz_dfs_mode,album)` |

---

## Main control (6400) on 1120

### Simple
- Select pauses or resumes, and a ghost logo shows while paused.
- Left and Right change song, Up goes to the pill, and Back closes the view.

### How it works
- When Select pauses, it first sets `bz_pnfoc=6403`, which drives the pause ghost logo. Resuming clears it.
- Down is a deliberate noop.
- Back sets `bz_fsret` for 1 s so the music window knows it's returning from FS, then closes 1120.
- On unload, 1120 clears `bz_pnfoc`/`bz_pnsel` and refocuses the album rail's home slot for the current `bz_at_fsslide`, through a 0 s `AlarmClock(bz_pvret,…)`.

### Wiring
| Handler (6400) | Value |
|---|---|
| defaultcontrol | `always` 6400 |
| onclick | `!Player.Paused` → `SetProperty(bz_pnfoc,6403,home)` · `Player.Paused` → `ClearProperty(bz_pnfoc,home)` · `PlayerControl(Play)` |
| onleft / onright | `PlayerControl(Previous)` / `PlayerControl(Next)` |
| onup / ondown | 6401 / `SetProperty(bz_noop,1,home)` |
| onback | `bz_fsret=true` + 1 s clear alarm + `Dialog.Close(1120)` |
| onunload | clear `bz_pnfoc`, `bz_pnsel` · `AlarmClock(bz_pvret,SetFocus(6368\|6378\|6398\|6383),00:00,silent)` by fsslide 1 / 2 / empty-or-3 / 4 |

---

## Prev / next tiles

### Simple
In PREV/NEXT mode, tapping the left or right album plays the previous or next song. A tile only appears when there's a song to go to.

### How it works
- 6405 and 6406 are touch targets. They're visible only outside album mode and when `MusicPlayer.offset(∓1).Title` exists.
- If a remote lands focus on a tile, it bounces straight back to 6400.
- On viz, 6407/6408 do the same and also need PREV/NEXT mode.

### Wiring
| ID | visible | onfocus | onclick |
|---|---|---|---|
| 6405 | `!album + !String.IsEmpty(MusicPlayer.offset(-1).Title)` | `SetFocus(6400)` | `Playlist.PlayOffset(music,-1)` |
| 6406 | `!album + !String.IsEmpty(MusicPlayer.offset(1).Title)` | `SetFocus(6400)` | `Playlist.PlayOffset(music,1)` |

---

## Sides fade-in (WindowOpen)

### Simple
When the view opens, the centre album and now-playing appear immediately. The side albums ease in a few seconds later.

### How it works
- The shared include `BezelFSPlayNext` takes `sdelay`/`sfade` params.
- 1120 passes 3000 / 2000 explicitly. MusicVisualisation uses the include defaults, which are the same values.
- The sides gate is `sides = !album`.

### Wiring
- `Custom_1120_PlayNext.xml` L15: `BezelFSPlayNext` vis `Player.HasAudio`, `sdelay` 3000, `sfade` 2000, `sides` `!String.IsEqual(Skin.String(bz_dfs_mode),album)`.

---

## Fanart FS Play Next sides (viz)

### Simple
In the full-screen viz, the side albums can be switched off. A double-Select on the main block brings them back.

### How it works / Wiring
- `bz_pnoff=1` turns the sides off. A double-Select on 6390 clears it (sides on / album viz).
- 6409 (right hit) only bounces and doesn't clear `bz_pnoff`.
- 6410 → `bz_npmode=upnext`.
- Side tiles 6407/6408 → `Playlist.PlayOffset` ∓1.

---

## Slide speed and cast

### Simple
How fast the album slides into FS is a tuner setting. The soft side shadows breathe with the sway.

### How it works / Wiring
- `bz_at_fsslide`: 1 = 480 ms · 2 = 380 · 3/empty = 280 · 4 = 180. It's shared with Dialogue FS and viz preview-next.
- Stub cast opacity follows the shared sway clock (`bz_castL`/`bz_castR`, 5.33.170 BUG-021). Its overall level is the Tuner Viz opacity (5.33.171), and the cast is gated on Cover.

---

## Keys (1120)
| Key | Behavior |
|---|---|
| Select on 6400 | Play/Pause (sets `bz_pnfoc=6403` when pausing → ghost logo) |
| Left / Right on 6400 | Previous / Next |
| Up / Down on 6400 | Pill 6401 / noop |
| Select / Left / Right on pill | Toggle ALBUM ↔ PREV/NEXT |
| Up / Down on pill | 6400 |
| Back | `bz_fsret` (1 s), close 1120 |

## Touch
Prev/next tiles 6405/6406 (1120) and 6407/6408 (viz) play offset ∓1.

## Related
big-album-pill.md · dialogue-fs.md · fanart-fs.md · sway-animations.md · music-list.md
