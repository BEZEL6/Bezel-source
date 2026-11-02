# Section menu (context)

**Object:** `Custom_1119_SecCtx.xml` dialog `1119` · grouplist `9000` · buttons `7901–7947` (40 rows); `scripts/bz_ctx.py`, `scripts/bz_dtap.py`  
**Where:** Options+Info template shell (black left mask, BezelLogo, 450 fanart crop `BzCIStage`, title at 150,150, `BzCIStripBG` strip, rows at 582,166)  
**Last updated:** 2026-11-01 · 5.33.242
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What opens it

**Simple.** BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.

**How it works.** The keymap sends menu keys to the background script instead of Kodi. `bz_dtap.info()` then picks the menu. Kodi's own contextmenu is closed first in case it opened anyway. That is a race: Kodi can open its menu before the notify arrives. On a double-tap the script also sets `bz_dtapinfo` for 0.8 s.

**Wiring.**
- noctx keymap `zz_bezel2_noctx.xml`: in home/music/videos+SECW, `c`/menu/title/contextmenu/rightclick/longclick → `NotifyAll(bz,bz_ctx)`.
- `bz_ctx` handler: closes Kodi `contextmenu` (up to 40 × 25 ms), then `info()`.
- `info()`: filebrowser/filemanager → `Action(ContextMenu)`. A SECW window that is not on 1119 → `ActivateWindow(1119)`. Else → `Action(Info)` (info-options.md).
- SECW = pictures, programs, games, addonbrowser, music/video playlist, PVR windows.

## Keys

**Simple.** Up and Down move through the rows and stop at the ends. Left or Right closes. Select runs the row. Back closes.

**How it works.** Most rows close 1119 first and then fire the action on a 0-second AlarmClock. That way the action lands on the window underneath, with the right focused item, instead of on the dialog.

**Wiring.**
| Key | Behavior |
|---|---|
| Up / Down | `onup`/`ondown` `noop` on 9000: no wrap, no escape |
| Left / Right | `Close` |
| Select | e.g. 7901 `Dialog.Close(1119,true)` + `AlarmClock(bzsc,Action(Select),00:00,silent)` |
| Back | close |

`<defaultcontrol always="true">9000</defaultcontrol>`, `DepthDialog+`, no pop-in anim (5.33.29). Rows use `BzCIBtn`. The left mask (`-60,-60` 630×1200 `FF000000`) is still **on** here. Only the Info dialogs disabled theirs (info-options.md).

## Rows by window

**Simple.** Each section shows only its own rows.

**Wiring.** Each row has a `visible` condition on `Window.IsActive(...)`.
- **Programs / Games / Add-ons:** Open 7901 · Add-on info 7902 · Add-on settings 7903 (needs `ListItem.Property(Addon.ID)`) · Favourite 7904 · Check for updates 7905 · Sort by 7906 · Order 7907 · Get more 7908 (programs) / 7909 (games) · Install from repository 7910 (addonbrowser)
- **Music/Video playlist:** Play from here 7911 · Item info 7912 · Move up/down 7913/7914 · Remove 7915 · Shuffle 7916 (SendClick 20) · Repeat 7917 (26) · Save 7918 (21) · Clear 7919 (22)
- **PVR:** Switch to channel 7920 · Programme info 7921 · Record 7922 · Guide 7923 · Play / Recording info / Delete recording 7924–7926 · Timer edit/info/delete 7927–7929 · Search guide 7930 · Channel manager 7931 · PVR settings 7932
- **Pictures:** View 7940 · Open folder 7941 · Picture info 7942 · Slideshow 7943 · Recursive slideshow 7944 · Sort 7945 · Order 7946 · Favourite 7947

## Favourite rows

**Simple.** A Favourite row adds the item to Kodi Favourites and shows "Added to favourites".

**Wiring.** `bz_ctx.py fav`. Media → a media favourite. Add-ons in programs/games/addonbrowser → a script favourite, or a window/videos favourite for plugins. Notification "Added to favourites" / "Could not add favourite" for 2000 ms. `bz_ctx.py remove` is the library-remove path used by Info (dialog-confirm.md).

## Related
info-options.md · favourites.md · keymaps.md · pictures.md · playlists.md

## Warm source variant (current, 5.33.242)
Menu on a source row (1117 / SOURCES 1132 / Pictures sources root) now draws Kodi's context menu in the Warm strip: `DialogContextMenu` with `$EXP[bz_ctxwarm]` hides BezelStdFrame, shows `BezelMMStripChrome` (w 450) at 570,120 titled with the item + `SOURCE · OPTIONS`, and slides grouplist 996 to 570,232. Rows are still Kodi's own (Edit source / Remove source …) — whatever Kodi offers for that list.


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Custom_1119_SecCtx.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 9000 | grouplist | 582,166 | 360×430 | `Close/Close/noop/noop` | `—` |
| 7901 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)]` |
| 7902 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)]` |
| 7903 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)] + …` |
| 7905 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)]` |
| 7906 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)] | …` |
| 7907 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)] | …` |
| 7908 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(programs)` |
| 7909 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(games)` |
| 7910 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(addonbrowser)` |
| 7911 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7912 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7913 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7914 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7915 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7916 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7917 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7918 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7919 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(musicplaylist) | Window.IsActive(videoplaylist)]` |
| 7920 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)]` |
| 7921 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)] | [Window.IsActive(tvgui…` |
| 7922 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)] | [Window.IsActive(tvgui…` |
| 7923 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)]` |
| 7924 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvrecordings) | Window.IsActive(radiorecordings)]` |
| 7925 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvrecordings) | Window.IsActive(radiorecordings)]` |
| 7926 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvrecordings) | Window.IsActive(radiorecordings)]` |
| 7927 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvtimers) | Window.IsActive(radiotimers) | Window.IsActive(tvtimerrule…` |
| 7928 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvtimers) | Window.IsActive(radiotimers) | Window.IsActive(tvtimerrule…` |
| 7929 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvtimers) | Window.IsActive(radiotimers) | Window.IsActive(tvtimerrule…` |
| 7904 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(programs) | Window.IsActive(games) | Window.IsActive(addonbrowser)] | …` |
| 7930 | button | —,— | —×— | `—/—/—/—` | `[[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)] | [Window.IsActive(tvgu…` |
| 7931 | button | —,— | —×— | `—/—/—/—` | `[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)]` |
| 7932 | button | —,— | —×— | `—/—/—/—` | `[[Window.IsActive(tvchannels) | Window.IsActive(radiochannels)] | [Window.IsActive(tvgu…` |
| 7940 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures) + !ListItem.IsFolder` |
| 7941 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures) + ListItem.IsFolder + !ListItem.IsParentFolder` |
| 7942 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures) + !ListItem.IsFolder` |
| 7943 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures)` |
| 7944 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures)` |
| 7945 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures)` |
| 7946 | button | —,— | —×— | `—/—/—/—` | `Window.IsActive(pictures)` |
| … | 1 more ids not listed | | | | |

Actions (`onclick`/`onload`/`onback`) found:
- `ActivateWindow(PVRChannelManager)`
- `ActivateWindow(TVGuide)`
- `ActivateWindow(TVSearch)`
- `ActivateWindow(addonbrowser,addons://more/executable/,return)`
- `ActivateWindow(addonbrowser,addons://more/game/,return)`
- `ActivateWindow(addonbrowser,addons://repos/,return)`
- `ActivateWindow(pvrsettings)`
- `Addon.OpenSettings($INFO[ListItem.Property(Addon.ID)])`
- `AlarmClock(bzsc,Action(Delete),00:00,silent)`
- `AlarmClock(bzsc,Action(Info),00:00,silent)`
- `AlarmClock(bzsc,Action(MoveItemDown),00:00,silent)`
- `AlarmClock(bzsc,Action(MoveItemUp),00:00,silent)`
- `AlarmClock(bzsc,Action(Record),00:00,silent)`
- `AlarmClock(bzsc,Action(Select),00:00,silent)`
- `AlarmClock(bzsc,Container.NextSortMethod,00:00,silent)`
- `AlarmClock(bzsc,Container.SortDirection,00:00,silent)`
- `AlarmClock(bzsc,SendClick(20),00:00,silent)`
- `AlarmClock(bzsc,SendClick(21),00:00,silent)`
- `AlarmClock(bzsc,SendClick(22),00:00,silent)`
- `AlarmClock(bzsc,SendClick(26),00:00,silent)`
- `AlarmClock(bzsc,SlideShow($INFO[Container.FolderPath]),00:00,silent)`
- `AlarmClock(bzsc,SlideShow($INFO[Container.FolderPath],recursive),00:00,silent)`
- `Dialog.Close(1119,true)`
- `RunScript(special://skin/scripts/bz_ctx.py,fav)`
- `UpdateAddonRepos`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/context-menu.md) · [state](../state/context-menu.md) · [motion](../motion/context-menu.md) · [art](../art/context-menu.md) · [input](../input/context-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
