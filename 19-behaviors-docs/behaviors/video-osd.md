# Video OSD

**Object:** `VideoOSD.xml` · buttons `6501–6509`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## Rows (Up/Down wraps 6509 ↔ 6501)
Play/Pause 6501 (`BzOSDPlayLbl`) · Rewind 6502 · Fast forward 6503 · Stop 6504 · Subtitles 6505 (osdsubtitlesettings) · Audio 6506 (osdaudiosettings) · Bookmarks 6507 · Settings 6508 (osdvideosettings) · Info 6509.

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move (wraps) |
| Left | Close OSD |
| Right | noop |
| Select | Row action |
| Back | Kodi default (close OSD) |

**Fix this pass:** the old doc listed the order "Rewind / Play / FF / Stop / Audio / Subtitles". The live order is Play, Rewind, FF, Stop, Subtitles, Audio, Bookmarks, Settings, Info.

## Related
fullscreen-video.md · pause-overlay.md
