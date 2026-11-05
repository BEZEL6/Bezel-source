# Pause screen

**Object:** pause overlay over fullscreen video · Kodi: dialog `1116` (`Custom_1116_PauseScreen.xml`, zorder 1)
**Where:** fullscreen video while paused
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Pause a film or episode and the picture dims; the poster glides in on the right with the title, a subtitle line and "PAUSED · time / duration" with a thin progress bar. Play hides it; opening the OSD hides it at once. It never takes keys.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Shown | video paused in fullscreen, not buffering, no OSD | resume; OSD / subtitle / audio settings open | dim, poster, title, subtitle, status, progress |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | fade 0 → 100 and poster slide from +906 px, together | 600, cubic out |
| close | fade | 250 |

### Interruptions
OSD opening hides it instantly (never overlaps).

### Continuity
—

### Layering
Video < 28 % black dim < poster shadow < poster < texts.

### Geometry
Poster group 1014, 156; poster 552 × 828 (shadow 552 × 834); title y 628, right-aligned 500 wide ending at the poster's left; subtitle 690; status 728; progress 774 (500 × 4).

### Art
Poster with rounded mask; progress in the strip colour.

### Input
None (keys go to the player / OSD).

### Speed targets
—

### Never
No overlap with the OSD.

### Acceptance checks
Pause → overlay glides in; Select → OSD replaces it; Play → gone.

## Kodi implementation (sandbox)

### How it works
#### When it shows

##### Simple
Pause a film or episode and the picture dims. The poster slides in on the right, with the title, a subtitle line and "PAUSED · time / duration" plus a thin progress bar. Press Play and it all goes away.

##### How it works
- 1116 has no opener. It's a dialog with a `<visible>` condition, so Kodi shows and hides it by itself whenever that condition changes.
- The condition requires full-screen video, paused, with video, not buffering, and none of the OSDs open. Opening the Video OSD (Select/Menu) or subtitle/audio settings hides the pause screen instantly, so the two never overlap.
- There are no focusable controls, so it never takes keys. Play, Select and Back all go to the player or OSD underneath.

##### Wiring
| Item | Value |
|---|---|
| Window | dialog `1116`, zorder 1 |
| Visible | `Window.IsActive(fullscreenvideo) + Player.Paused + Player.HasVideo + !Player.Caching + !Window.IsActive(videoosd) + !Window.IsActive(osdsubtitlesettings) + !Window.IsActive(osdaudiosettings)` |
| Focus | none |

---

#### Layout and motion

##### Simple
The dim fades in over about half a second while the poster glides in from the right. Text is right-aligned to the poster's left edge.

##### How it works
The whole group fades in 0→100 over 600 ms cubic out and fades out over 250 ms. At the same time, the poster group slides from 906 px to the right into place over 600 ms, so the motion and fade finish together. The poster has its own rounded shadow image behind it.

##### Wiring
| Element | Value |
|---|---|
| Group fade | 0→100, 600 ms cubic out (open); 250 ms (close) |
| Dim | full-screen image, colour `47000000` |
| Poster group | at 1014,156; slide from 906,0, 600 ms cubic out |
| Shadow | `mm_round.png`, `AA000000`, 552×834 |
| Poster | `$VAR[BzPausePoster]`, 552×828, `mm_round` diffuse |
| Title | top 628, left −540, width 500, right-aligned, `[UPPERCASE]$VAR[BzVOSDTitle]`, font `bz_mm48b` |
| Subtitle | top 690, `$VAR[BzPauseSub]`, `bz_mm20` |
| Status | top 728, `PAUSED · $INFO[Player.Time] / $INFO[Player.Duration]`, `bz_mm18b` |
| Progress | top 774, 500×4, mid colour `$VAR[BezelBlockBF]` |

---

#### Keys / touch
None of its own (no focusable controls). Play resumes and hides it; Select/Menu opens the Video OSD, which hides it.

#### Note
The music "ghost logo" pause lives in Dialogue FS (`bezel/logo_pause.png`, dialogue-fs.md), not here.

### Wiring
See the detail above.

### Kodi workarounds (do not port)
A dialog opened by its own `<visible>` condition (no opener); Kodi decides when it shows.

## Related
[video-osd](video-osd.md) · [fullscreen-video](fullscreen-video.md)
