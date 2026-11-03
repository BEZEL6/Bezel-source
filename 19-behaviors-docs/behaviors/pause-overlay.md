# Pause screen (dialog 1116)

**Object:** `Custom_1116_PauseScreen.xml` dialog `1116` (zorder 1) · poster, shadow, dim, 3 labels, progress bar
**Where:** Over full-screen video while it's paused
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. It shows automatically on video pause and hides as soon as the OSD or a sub-dialog opens or playback resumes. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## When it shows

### Simple
Pause a film or episode and the picture dims. The poster slides in on the right, with the title, a subtitle line and "PAUSED · time / duration" plus a thin progress bar. Press Play and it all goes away.

### How it works
- 1116 has no opener. It's a dialog with a `<visible>` condition, so Kodi shows and hides it by itself whenever that condition changes.
- The condition requires full-screen video, paused, with video, not buffering, and none of the OSDs open. Opening the Video OSD (Select/Menu) or subtitle/audio settings hides the pause screen instantly, so the two never overlap.
- There are no focusable controls, so it never takes keys. Play, Select and Back all go to the player or OSD underneath.

### Wiring
| Item | Value |
|---|---|
| Window | dialog `1116`, zorder 1 |
| Visible | `Window.IsActive(fullscreenvideo) + Player.Paused + Player.HasVideo + !Player.Caching + !Window.IsActive(videoosd) + !Window.IsActive(osdsubtitlesettings) + !Window.IsActive(osdaudiosettings)` |
| Focus | none |

---

## Layout and motion

### Simple
The dim fades in over about half a second while the poster glides in from the right. Text is right-aligned to the poster's left edge.

### How it works
The whole group fades in 0→100 over 600 ms cubic out and fades out over 250 ms. At the same time, the poster group slides from 906 px to the right into place over 600 ms, so the motion and fade finish together. The poster has its own rounded shadow image behind it.

### Wiring
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

## Keys / touch
None of its own (no focusable controls). Play resumes and hides it; Select/Menu opens the Video OSD, which hides it.

## Note
The music "ghost logo" pause lives in Dialogue FS (`bezel/logo_pause.png`, dialogue-fs.md), not here.

## Related
fullscreen-video.md · video-osd.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Custom_1116_PauseScreen.xml`

_No id’d controls in this file (layout comes from includes)._

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/pause-overlay.md) · [state](../state/pause-overlay.md) · [motion](../motion/pause-overlay.md) · [art](../art/pause-overlay.md) · [input](../input/pause-overlay.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
