# Play Next and Up Next

**Object:** side albums around the centred big album, and the Up Next queue list · Kodi: include `BezelFSPlayNext` (sides), include `BezelFSUpNext` (proxy `6396`, list `6395`) · touch `6405` / `6406` (1120), `6427` / `6428` (1121), `6407` / `6408` (Kodi FS)
**Where:** album views (Dialogue FS, fullscreen album view) and the fullscreen cycle mode Up Next
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
**Play Next** (PREV/NEXT mode): with the big album centred, the previous song's album sits on the left and the next song's on the right, each with its title and artist. Tap one to play it. They fade in gently; nothing waits.
**Up Next**: on the fullscreen fanart stage, the cycle pill's Up Next mode shows the queue as a list at the left. Down from the pill enters it, Select plays the song.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Sides hidden | ALBUM mode; fanart stage | PREV/NEXT in album view | big album only |
| Sides shown | PREV/NEXT + album view | ALBUM; leave album view | two side covers + labels, soft cast, soft frame |
| No neighbour | first / last song | queue changes | that side is empty (no frame, no shadow) |
| Up Next shown | cycle mode Up Next | other mode | queue list (fades 300 ms) |
| Up Next focused | Down from the pill | Back / Left / Up on the first row | focused row highlighted |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 (view opens) | sides fade in, no delay | 2000 | sine in-out |
| track change | sides' covers crossfade to the new neighbours | 800 | sine in-out |
| ALBUM | sides fade out | 800 | sine |
| Up Next on / off | list fades | 300 / 300 | sine in-out |

### Interruptions
- Track change during the sides' fade-in: covers swap in place; the fade continues.
- Mode flip mid-fade: reverses from where it is.

### Continuity
- Side cast shadows breathe with the big album's sway (one clock).
- Up Next keeps its scroll position while it stays up.

### Layering
Fanart stage < side albums (cover, glare, bottom gradient, label panel, soft frame, cast) < big album < chrome.

### Geometry
| Piece | Value |
|---|---|
| Left side | 90, 250, 540 × 540 |
| Right side | 1290, 250, 540 × 540 |
| Label panel | lower 162 px of the cover (0, 378); artist 22, 446 (496 × 26); title 22, 474 (496 × 40) |
| Frame | 542 × 542 around the cover |
| Up Next list | 150, 346, 869 × 640; rows 64 px: thumb 48 (14, 8), title 580 × 30 (78, 6), artist 580 × 22 (78, 36), time 110 (745) |

### Art
- Covers: previous / next song's album cover; empty when none.
- Frame: soft frame texture; cast: soft cast under each side, only with a real cover.
- Up Next rows: title white, artist 70 % white; focused row = white outline over a 25 % black rounded fill (one soft shadow per label).

### Input
| Action | Result |
|---|---|
| Touch left / right side | play previous / next |
| Remote on sides | never lands there (focus goes to the album) |
| Up Next: Up / Down | move |
| Up Next: Select | play that song |
| Up Next: Up on first row / Left / Back | back to the cycle pill |

### Speed targets
Sides begin fading on the first frame; no wait.

### Never
- No delay before the sides (317 "remove the wait"; was 3000 ms).
- No stub cast without a real cover (127).
- No four-ring label shadows on Up Next rows; no white block highlight (308).
- No NP bar under the home album with Up Next (470 reverted 463).

### Acceptance checks
1. Album view, PREV/NEXT: sides fade in at once, labels readable.
2. Next song: covers move along without a flash.
3. First song in the queue: left side empty, no shadow.
4. Fanart stage → pill → Up Next → Down → Select a row → that song plays.

## Kodi implementation (sandbox)

### How it works
- `BezelFSPlayNext` params: `vis` (default `[!bz_pnoff=1] + Player.HasAudio`), `sdelay` (0), `sfade` (2000), `sides` (1120 / viz / 1121: `!String.IsEqual(Skin.String(bz_dfs_mode),album)`).
- Covers `MusicPlayer.offset(-1 / 1).Cover`; labels from the same offsets; touch tiles visible only with `MusicPlayer.offset(∓1).Title`.
- Cast opacity: Home `bz_castL` / `bz_castR` from bz_flip sway_clock (`_bz_cast`); Tuner `bz_at_fsvizop` sets the overall level (1 = off, 2 = 10 %, …).
- `BezelFSUpNext` params: `vis` (`$EXP[bz_np] + $EXP[bz_npm_upn]`), `home` (control to return to), colours `upc1` / `upc2` / `upc3`. 1121 mounts its own copy (`home=6421`); the Music-window copy hides while 1121 is visible. Select → `bz_cmd.py upnext_goto`.

### Wiring
| Piece | Value |
|---|---|
| Side textures | `bezel/pn_glare_ul.png`, `bezel/grad_bottom.png`, `bezel/bz_frame_soft.png`, `bezel/pn_cast.png` |
| Touch | 6405 / 6406 (1120), 6427 / 6428 (1121), 6407 / 6408 (viz): onfocus → main; click `Playlist.PlayOffset(music,-1 / 1)` |
| Up Next | proxy 6396, list 6395 |
| Skin | `bz_dfs_mode`, `bz_npmode=upnext`, `bz_at_fsvizop` |

### Kodi workarounds (do not port)
- `MusicPlayer.offset(n)` infolabels stand in for a queue model.
- Proxy control 6396 in front of list 6395: lets Up from the first row leave the list in Kodi.

## Related
[big-album-pill](big-album-pill.md) · [dialogue-fs](dialogue-fs.md) · [music-fanart-fs](music-fanart-fs.md) · [fanart-fs](fanart-fs.md) · [sway-animations](sway-animations.md)
