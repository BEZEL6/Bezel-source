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

**How it works.** The mode lives in one Skin.String, so it is shared across 1120 and viz and survives restarts. Both windows set `bz_dfs_mode=album` on load when it is empty, so ALBUM is the default. The side albums come from `BezelFSPlayNext` with `sides=!String.IsEqual(Skin.String(bz_dfs_mode),album)`. Their reveal uses `sdelay 3000` / `sfade 2000`, so after a switch to PREV/NEXT the sides wait 3 s and then fade in over 2 s.

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
