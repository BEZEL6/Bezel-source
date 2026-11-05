# Big album pill

**Object:** ALBUM ↔ PREV/NEXT mode pill · Kodi: include `BezelBigAlbumPill` → button `6401`, mode `Skin.String(bz_dfs_mode)` · used in Dialogue FS (1120), Music Fanart FS (1121) album view and Kodi FS album view
**Where:** upper right, 1360,42 500 × 32, right-aligned (centred on the Bezel logo, y 58)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
When the big album is in the centre, a small pill at the top right says ALBUM or PREV/NEXT. ALBUM shows the big album alone; PREV/NEXT also shows the previous and next albums beside it. Select, Left or Right flips it. Up or Down goes back to the album. The choice is remembered (also after a restart) and shared by every album view. It is a different pill from the six-mode cycle pill on the fanart stage.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| ALBUM (default) | first use; flip | flip | big album alone |
| PREV/NEXT | flip | flip | big album + side albums |
| Focused | Up from the album | Up / Down / 5 s idle | pill brighter (80 % tint), pause logo hidden |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| view opens | pill fades in after a delay | 600 after 1000 | sine in-out |
| flip to PREV/NEXT | side albums fade in | 2000 | sine in-out |
| flip to ALBUM | side albums fade out | 800 | sine in-out |
| view closes | pill fades out | 600 | sine in-out |

### Interruptions
- Flipping again mid-fade reverses the side fade from where it is.
- 5 s without input on the pill: focus returns to where it came from (the album).

### Continuity
Mode survives closing, reopening and app restarts; one value for all album views.

### Layering
Over the fanart / Music window and the big album layer; same level as the other fullscreen chrome.

### Geometry
Group 1360, 42, 500 × 32, text right-aligned (pill grows left); its centre (y 58) lines up with the Bezel logo (64 × 64 at 28, 26).

### Art
32 px rounded pill, 16 px caps, fill = fullscreen tint at 50 % (unfocused) / 80 % (focused), label in the tint colour, 15 px bold font. Labels: ALBUM, PREV/NEXT.

### Input
| Action | Result |
|---|---|
| Select / Left / Right | flip mode |
| Up / Down | back to the album |
| Back | Dialogue FS: close it; fullscreen: back to the album |

### Speed targets
Flip is instant; sides follow the fade above.

### Never
- Not the same object as the cycle pill (don't merge them).
- No wait before the sides (317).

### Acceptance checks
1. Album view → Up → pill focused, pause logo gone.
2. Select → PREV/NEXT, sides fade in; Select → ALBUM, they fade.
3. Close and reopen fullscreen → mode kept.

## Kodi implementation (sandbox)

### How it works
- One include; params `vis` (default `true`), `main` (control to return to), `back_close`.
- Mode: `album` hides sides; empty (Skin.Reset) shows them. 1120 / 1121 / Kodi FS onload set `album` when empty.
- Toggle: `onclick` / `onleft` / `onright` → `album` ? `Skin.Reset(bz_dfs_mode)` : `Skin.SetString(bz_dfs_mode,album)`.
- `back_close=1` (1120): `bz_fsret=true` + 1 s clear alarm + `Dialog.Close(1120)`; else `onback` → `$PARAM[main]`.
- Pill idle return: bz_flip `_pill_idle` (6401 → 6400).

### Wiring
| Host | Params |
|---|---|
| 1120 | `main=6400`, `back_close=1`; 6400 onup → 6401 |
| 1121 | `main=6420`, `vis=[!bz_pnoff=1] + Player.HasAudio` |
| Kodi FS | `main=6390`, same `vis` |
| Look | font `bz_b15`, `bezel/np_pill32.png` border 16, text `$VAR[BzFSCTint]`, nofocus `BzFSCTint50`, focus `BzFSCTint80`, label `$VAR[BezelDFSModeName]` |
| Anim | WindowOpen fade 600 ms delay 1000; WindowClose 600 ms |
| onfocus | `ClearProperty(bz_pnfoc,home)` |

### Kodi workarounds (do not port)
- Toggling by Reset / SetString: Kodi skin strings have no toggle.
- The legacy name "dfs" (Dialogue FS) on a pill that now serves three screens.

## Related
[dialogue-fs](dialogue-fs.md) · [music-fanart-fs](music-fanart-fs.md) · [fanart-fs](fanart-fs.md) · [play-next](play-next.md)
