# Playlists

**Object:** the play queue and saved playlists · Kodi: `MyPlaylist.xml` (list `60`, side `9000`: shuffle `20`, repeat `26`, save `21`, clear `22`), `MyMusicPlaylistEditor.xml`, section menu `1119` rows `7911`–`7919`, `7904`
**Where:** the queue window (music / video playlist) and saved playlists
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
**Up next** in music controls (or the Playlist side button) shows what's queued. Its side buttons are Shuffle, Repeat, Save and Clear; Menu / double-Select on a queued song gives Play from here, Item info, Move up, Move down, Remove, Shuffle, Repeat, Save, Clear and Favourite. Saved music playlists open as a normal Music list. Back returns where you came from.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Queue | Up next (music controls), Playlist side button | Back | queue list, side buttons, backdrop |
| Item menu | Menu / double-Select on a row | an action / Back | section menu with the queue actions |
| Saved playlists | a saved-playlists path | Back | Music list |
| Editor | Kodi's playlist editor | Back | button column + two lists |

### Timeline
| What | Duration | Curve |
|---|---|---|
| queue window fade-in | 400 | sine out |
| album sway | **re-anchors** on open (0.25 s flat, then lead-in again) | — |

### Interruptions
Menu actions close the menu first, then act on the list.

### Continuity
The menu's Shuffle / Repeat / Save / Clear are the same actions as the side buttons.

### Layering
Backdrop < queue list + side buttons < menu.

### Geometry
Kodi playlist layout under the Bezel chrome.

### Art
A backdrop is picked on open (and saved on close).

### Input
| Action | Result |
|---|---|
| Select | play from that song |
| Menu / double Select | item menu |
| Back | previous screen |

### Speed targets
—

### Never
No MM PLAYLISTS row (5.33.60 removed it).

### Acceptance checks
Music controls › Up next → queue; Menu on a song → Move up works; Back → fullscreen / previous screen.

## Kodi implementation (sandbox)

### How it works
- MyPlaylist onload: `bz_cmd.py backdrop`, start bz_flip if needed, `bz_sway_restart=true`; onunload saves `bz_backdrop_last`, clears `bz_backdrop`. `BezelWindowFade` + `BezelSecDim`. defaultcontrol `always` 60.
- `musicplaylist` / `videoplaylist` are in `bz_dtap.py` SECW, so double-tap / context keys open 1119; each item does `Dialog.Close(1119,true)` then a 0 s `AlarmClock(bzsc,…)` on the playlist window.
- Saved playlists: `bz_cmd.py tomusic special://musicplaylists/` (GO entry kept).
- Editor: defaultcontrol `always` 6; grouplist 9000 ↔ lists 50 / 100 with scrollbars 60 / 61 in a ring.

### Wiring
| Id | Item | Action |
|---|---|---|
| 7911 | Play from here | `Action(Select)` |
| 7912 | Item info | `Action(Info)` |
| 7913 / 7914 | Move up / down | `Action(MoveItemUp / MoveItemDown)` |
| 7915 | Remove | `Action(Delete)` |
| 7916–7919 | Shuffle / Repeat / Save / Clear | `SendClick(20 / 26 / 21 / 22)` |
| 7904 | Favourite | `bz_ctx.py fav` |

### Kodi workarounds (do not port)
`SendClick` to Kodi's own button ids; the sway re-anchor on open (Kodi window switch).

## Related
[music-controls](music-controls.md) · [context-menu](context-menu.md) · [sway-animations](sway-animations.md)
