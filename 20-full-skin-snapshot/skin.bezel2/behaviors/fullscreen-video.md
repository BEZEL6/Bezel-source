# Fullscreen video

**Object:** fullscreen video playback · Kodi: `VideoFullScreen.xml`, keymap `fullscreenvideo` / `videoosd` sections, `bz_cmd.py vidsel` / `vidback`
**Where:** while a video plays fullscreen
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Plain fullscreen video with Bezel chrome. Video starts in fullscreen. Select pauses and shows the controls (OSD); the pause screen shows while paused with no OSD. Back peels away whatever is on screen one layer at a time, and only then stops. Tab keeps Kodi's own behaviour here; Bezel fullscreen music never opens over a video.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Playing | play a video | stop | video only |
| Paused | Select / pause | Select / play | pause screen |
| OSD | Select | Back / Left | OSD column |

### Timeline
See [video-osd](video-osd.md) and [pause-overlay](pause-overlay.md).

### Interruptions
Back with something on screen hides it first; Back with nothing on screen stops.

### Continuity
After stop, the section and row you started from.

### Layering
Video < pause screen < OSD < dialogs.

### Geometry
Full screen.

### Art
—

### Input
Select: pause + OSD; Back: stepped (hide → stop); Tab: Kodi default.

### Speed targets
Select responds at once.

### Never
Back never stops a film by accident (stepped Back).

### Acceptance checks
Play → Select → OSD; Back → OSD gone; Back → stops, back in the list.

## Kodi implementation (sandbox)

### How it works (live detail; dated sections are the current state unless a later one supersedes them)
#### What it does

**Simple.** Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.

**How it works.** Kodi opens the window by itself when video starts (4.0.1 O28 restored this; the 4.0.0 bounce-back was removed). The window has no focusable controls (`defaultcontrol` empty), so keys go through the BEZEL keymap to `bz_cmd.py`.

**Wiring.** Labels 10/11/12 at 45, top 15/45/75 (Kodi info lines). Group 1 `DepthOSD+` visible `Player.Caching + Integer.IsGreater(Player.CacheLevel,0)`, fade in 200 ms after 300, fade out 150 ms after 200.

#### Select

**Simple.** Pause or resume, and show the OSD.

**Wiring.** keymap `fullscreenvideo` select → `bz_cmd.py vidsel` = `PlayerControl(Play)` + `ActivateWindow(videoosd)` (BETA 2.6).

#### Back

**Simple.** The first Back hides the controls. The next Back stops.

**How it works.** `vidback` checks the layers top-down and removes only the first one it finds. A seek bar that Kodi leaves after the OSD closes does not count as another layer for 6 s. Without that rule you would need an extra Back.

**Wiring.** `bz_cmd.py vidback` (keymap back in `fullscreenvideo` and `videoosd`):
1. `videoosd` visible → set `bz_vosdc=now`, `Dialog.Close(videoosd)`.
2. `fullscreeninfo` visible → close it.
3. `Player.ShowInfo` → `Action(Info)` (toggle off).
4. `Player.DisplayAfterSeek | Player.Seeking`, and the OSD did not close within the last 6 s → stamp `bz_vosdc` and stop there.
5. Else `PlayerControl(Stop)`.

**Unverified:** the np_tab keymap also has a second `FullscreenVideo` block that maps Back → `Action(FullScreen)` (minimise). Which of the two Back maps Kodi applies has not been tested on device.

#### Interactions
- Pause screen 1116 shows when paused (pause-overlay.md).
- The global logo-back button and FS pill are hidden here. Dust is off (dust.md).
- The dtap keymap does not list `fullscreenvideo`, so Select is not double-tap-delayed here.

#### Exit (5.33.378 audit)
Video FS Back = `bz_cmd vidback` (OSD/info close, then Stop); Kodi returns to the opener window (section). No MM latch — video is started from a section list, so section return is intended.

### Wiring
See the detail above.

### Kodi workarounds (do not port)
`vidsel` / `vidback` scripts decide per press; duplicate `fullscreenvideo` / `FullscreenVideo` keymap blocks (which wins is untested).

## Related
[video-osd](video-osd.md) · [pause-overlay](pause-overlay.md) · [keymaps](keymaps.md)
