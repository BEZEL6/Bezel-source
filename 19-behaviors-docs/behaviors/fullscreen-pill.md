# FULLSCREEN pill (Music list)

**Object:** FULLSCREEN pill on the Music list · Kodi: button `6886` in a horizontal grouplist at 140,136 (300 × 32, left-aligned), inside `BezelFSLeftStage` (Includes_Bezel)
**Where:** Music section (artists / albums / songs lists), fanart stage upper left, while audio plays
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
While music plays, a small FULLSCREEN pill sits at the top left of the Music fanart stage. Select opens fullscreen music. Focus order from the list going left is: list → FULLSCREEN pill → A–Z jump bar. Left from the pill goes to the A–Z bar (or opens the main menu when there is no bar). Leave it focused for 5 seconds and focus goes back to the list.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hidden | no audio; not a Music artists / albums / songs list; MM open; any fullscreen or album view up; returning from Dialogue FS | conditions clear | — |
| Shown | audio + Music list | as above | pill at 50 % tint |
| Focused | Left from the list | Select / any direction / Back / 5 s idle | pill at 80 % tint |

### Timeline
Rides the stage: no own animation. Appears and disappears with hard visibility (no fade of its own, 155).

### Interruptions
Music stops while focused: pill hides; focus returns to the list.

### Continuity
Lives inside the stage group so it moves with it and never pops alone.

### Layering
Fanart stage < pill < MM / fullscreen.

### Geometry
Grouplist 140, 136, 300 × 32, left-aligned (same spot as the cycle pill in fullscreen).

### Art
32 px rounded pill (16 px caps), tint fill 50 % / 80 %, label FULLSCREEN in 15 px bold, tint colour.

### Input
| Action | Result |
|---|---|
| Select | open fullscreen music (Bezel's; Kodi FS only if Bezel's is switched off) |
| Left | A–Z bar if shown, else list + open the MM |
| Right / Up / Down / Back | list |
| 5 s idle | back to where focus came from |

### Speed targets
Fullscreen visible ≤ 300 ms after Select.

### Never
- No fade on hide (155): it must not linger over fullscreen.
- Not reachable from Left while hidden; Left from the list must not skip it when shown (297, 304).

### Acceptance checks
1. Play a song, Music list, Left → pill focused; Select → fullscreen.
2. Left again from the pill with a long artist list → A–Z bar.
3. Stop music → pill gone.

## Kodi implementation (sandbox)

### How it works
- Visible: `Player.HasAudio + Window.IsActive(music)` and not viz (active / visible), not fullscreenvideo, not 1120, not 1121, not 1112, `bz_pnoff` ≠ 1, `bz_fsret` ≠ true, `!$EXP[bz_navmenu]`, `Container.Content(artists | albums | songs)`.
- Select: `$EXP[bz_m1121ok]` → `ActivateWindow(1121)`, else `ActivateWindow(visualisation)`.
- Pill idle: bz_flip `_pill_idle` (6886 → last control, else 60).

### Wiring
| Handler | Action |
|---|---|
| onclick | 1121 / visualisation (above) |
| onleft | `Control.IsVisible(6100)` → `SetFocus(6100)`; else `SetFocus(60)` + (`bz_navok`) `bz_nav=true` |
| onright / onup / ondown / onback | 60 |
| Look | font `bz_b15`, `bezel/np_pill32.png`, text `BzFSCTint`, fill `BzFSCTint50` / `BzFSCTint80` |

### Kodi workarounds (do not port)
- The long negative visibility list exists because each Kodi fullscreen path is a separate window / dialog; a port hides the pill whenever fullscreen is up.
- The grouplist wrapper exists so Kodi routes Right from the pill.

## Related
[music-fanart-fs](music-fanart-fs.md) · [music-list](music-list.md) · [mm-autohide](mm-autohide.md)
