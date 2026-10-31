# Fullscreen pill (Music strip)

**Object:** control `6886` in `Includes_Bezel.xml`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Small pill on the Music section colour strip while audio plays. Select/tap opens Fanart FS (`ActivateWindow(visualisation)` when `Player.HasAudio`).

## Visibility (5.33.173 gate, still live)
Shown only with audio + music window + artists/albums/songs content + MM closed. Hard-hidden if any of these is true: visualisation active/visible, `bz_pnoff=1`, 1120 active/visible, `bz_fsret=true`, `fullscreenvideo` (BUG-018 .169/.173).

## Keys
| Key | Behavior |
|---|---|
| Select / tap | Fanart FS (visualisation) |
| Up / Down / Left / Right / Back | Return focus to list `60` |

**Fix this pass:** the old doc said "Left/Right cycle style". The live control sends every direction to 60. Style cycling is the **fan art pill** (`6391`) inside Fanart FS (fanart-fs.md).

## Related
fanart-fs.md · music-list.md · dialogue-fs.md
