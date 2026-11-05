# Now Playing (routes)

**Object:** every "show now playing" request · Kodi: `bz_cmd.py` actions `np` / `nptoggle` / `tab` / `vistoggle` / `npctl`, bz_flip `bz_tabq` · old dialog `1112` (`Custom_1112_NowPlaying.xml`) **removed in 5.33.465**
**Where:** anywhere music plays
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live (routes); old Now Playing dialog retired · **Lock:** none

## Simple
There is no separate Now Playing screen any more. Every way of asking for "now playing" (Tab, the remote's Display key, Select on the playing song, Info with nothing else to show, the optional auto Now Playing after idle) opens fullscreen music ([music-fanart-fs](music-fanart-fs.md)). The Music window's in-place panel stays, because it is the fanart stage under fullscreen.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Request | any route below | — | fullscreen music opens |
| Not playing | route with no audio | — | nothing happens (Info opens the normal info page) |
| Video playing | route | — | video fullscreen / video OSD |

### Timeline
Same as opening fullscreen music (300 ms fade).

### Interruptions
A request while fullscreen is already up: Tab / Display close it instead (toggle).

### Continuity
Same as fullscreen music: nothing restarts.

### Layering
See fullscreen music.

### Geometry
—

### Art
—

### Input
| Route | Result |
|---|---|
| Tab / Display | open fullscreen (toggle) |
| Select on the playing song | open fullscreen |
| Info with no album / item info | open fullscreen |
| Auto Now Playing after idle (Tuner, off by default) | open fullscreen |
| Tab while the app is busy | queued, then fullscreen |

### Speed targets
≤ 300 ms to fullscreen.

### Never
- No old Now Playing panel or dialog, no old upper-right pill around fullscreen (465 "remove the old code so I won't see the wrong screen").

### Acceptance checks
Each route above opens the same fullscreen screen.

## Kodi implementation (sandbox)

### How it works
- `bz_cmd.py` `np` / `nptoggle` / `tab` / `vistoggle` share one block: with audio and `bz_m1121ok`-style condition (`!Skin.HasSetting(bz_m1121_off)` + [music | home | videos | pictures | programs | addonbrowser] + !viz) → `ActivateWindow(1121)`; else Kodi FS. Video → `Action(FullScreen)`.
- `npctl` opens / closes 1115 (fullscreen video: `videoosd`).
- bz_flip `bz_tabq` (Tab pressed while busy) → `ActivateWindow(1121)`.
- Auto Now Playing: Tuner `bz_at_autonp` (off by default) in bz_flip nav_menu.
- ~60 `Window.IsActive(1112)` / `Dialog.Close(1112)` references remain as no-ops (always false / nothing to close).

### Wiring
| Item | Value |
|---|---|
| Script | `bz_cmd.py np`, `nptoggle`, `tab`, `vistoggle`, `npctl`, `xinfo` |
| Keymap | Tab / Display → `ActivateWindow(1121)` (Music, Home, Videos, Pictures, Programs, Add-ons) |
| Tuner | `bz_at_autonp` |

### Kodi workarounds (do not port)
The leftover 1112 references; the busy-Tab queue (Kodi drops keys while a script holds the GUI lock).

## Related
[music-fanart-fs](music-fanart-fs.md) · [np-bar](np-bar.md) · [keymaps](keymaps.md) · [music-controls](music-controls.md)
