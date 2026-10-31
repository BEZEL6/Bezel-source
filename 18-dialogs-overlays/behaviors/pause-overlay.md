# Pause screen

**Object:** `Custom_1116_PauseScreen.xml` dialog `1116` (zorder 1, 3 images + 3 labels)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Shown automatically when fullscreen video is paused: `Window.IsActive(fullscreenvideo) + Player.Paused + Player.HasVideo + !Player.Caching`, and only when Video OSD / OSD sub-dialogs are closed. It shows the title (`BzVOSDTitle`, uppercase), a subtitle (`BzPauseSub`) and `PAUSED · time / duration`.

## Keys
None (no focusable controls). Play resumes and it hides; Select/Menu opens the Video OSD, which hides it.

## Note
The music "ghost logo" pause is in Dialogue FS (`bezel/logo_pause.png`, dialogue-fs.md), not here.

## Related
fullscreen-video.md · video-osd.md
