# Section menu (context)

**Object:** `Custom_1119_SecCtx.xml` dialog `1119` · grouplist `9000` · buttons `7901–7947`; `scripts/bz_ctx.py`, `scripts/bz_dtap.py`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
BEZEL replaces Kodi's context menu. The noctx keymap sends C / Menu / Title / ContextMenu in home, music, videos and the section windows to `NotifyAll(bz,bz_ctx)`. `bz_dtap.info()` then picks the menu:
- Movies / TV / Music / Pictures → `Action(Info)` = BEZEL Options+Info (info-options.md)
- pictures, programs, games, addonbrowser, music/video playlist and PVR windows (`SECW`) → `ActivateWindow(1119)`
- filebrowser / filemanager → Kodi `Action(ContextMenu)`

Double-tap Select does the same (keymaps.md, touch-group.md).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move; top/bottom = noop (no wrap, no escape) |
| Left / Right | Close 1119 |
| Select | Run the row (most rows `Dialog.Close(1119,true)` then `AlarmClock(bzsc,…)` so the action hits the window underneath) |
| Back | Close |

## Rows by window (visible conditions)
- **Programs / Games / Add-ons:** Open 7901 · Add-on info 7902 · Add-on settings 7903 · Check for updates 7905 · Sort by 7906 · Order 7907 · Favourite 7904 · Get more 7908 (programs) / 7909 (games) · Install from repository 7910 (addonbrowser)
- **Music/Video playlist:** Play from here 7911 · Item info 7912 · Move up/down 7913/7914 · Remove 7915 · Shuffle 7916 (SendClick 20) · Repeat 7917 (26) · Save 7918 (21) · Clear 7919 (22)
- **PVR:** Switch to channel 7920 · Programme info 7921 · Record 7922 · Guide 7923 · Play / Recording info / Delete recording 7924–7926 · Timer edit/info/delete 7927–7929 · Search guide 7930 · Channel manager 7931 · PVR settings 7932
- **Pictures:** View 7940 · Open folder 7941 · Picture info 7942 · Slideshow 7943 · Recursive slideshow 7944 · Sort 7945 · Order 7946 · Favourite 7947

The Favourite rows run `bz_ctx.py fav`: `Favourites.AddFavourite` (add-ons as script/window favourites) plus a "Added to favourites" notification. `bz_ctx.py remove` is the library-remove path used by Info.

## Related
info-options.md · favourites.md · keymaps.md · pictures.md · playlists.md
