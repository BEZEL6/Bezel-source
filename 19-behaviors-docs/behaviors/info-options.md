# Options + Info

**Object:** `DialogVideoInfo.xml` / `DialogMusicInfo.xml` · grouplist `9000` (582,166, 360 wide), cast list `50` (video); `Custom_1111_XInfo.xml` (legacy 1111, closes itself)  
**Where:** Movies / TV / Music (and Pictures) item info  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live tree. The left fanart mask has been off since 5.33.205. Rob has not approved it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it is

**Simple.** One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.

**How it works.** The menu routing is in context-menu.md (`bz_dtap.info()` → `Action(Info)`). Every open starts on Main, because `onload` clears the page prop. Page changes set the Window prop `bz_ci_more` and move focus on a 0-second AlarmClock, so the focus move happens after the rows' visible conditions update.

**Wiring.**
- `onload ClearProperty(bz_ci_more)`. `defaultcontrol always` 8 (Play) inside 9000.
- Pages: empty = Main · `1` = More · `sec` = Section.
- 9980 "Section options ›": `SetProperty(bz_ci_more,sec)` + `AlarmClock(bzci_sec,SetFocus(9979),00:00,silent)`. Video: visible on Main (`bz_ci_more` empty). Music: visible inside More (`=1`, t4183).

## Left fanart

**Simple.** The left fanart stays visible while the menu is open.

**Wiring.** The old left black mask (`-60,-60` 630×1200 `FF000000` `bezel/white.png`) is `visible=false` in DialogVideoInfo / DialogMusicInfo / DialogAddonInfo (5.33.205). Video still has `BezelBlack` when `!Window.IsVisible(videos)`.

## Pages

**Wiring.**
- **Main:** Video → Play 8 · Play next 9081 · Queue 9082 · Browse seasons 9085 · Trailer 11 · Browse set 443 · More options 9089 · Section options 9980. Music → Play 8 · Play next 9081 · Queue 9082 · Favourite 9095 · Browse 9083/9084 · More options 9089.
- **More (`1`):** Choose art 7710 · Refresh 6 · Set rating 7 · Director 13 / watched 9095 / Add to favourites 9097 / Remove from library 9098 (video) · Other 12 (music) · Section options 9980 (music) · ‹ Back 9096.
- **Section (`sec`):** View type 9979 · Sort 9971 · Filter / Order · Update library · Party mode · Go to playlist · Get more · Edit nodes · Add-on settings · Clearart toggle 9969 (`bz_tvclear_off`, video) · Visualizer 9974 (music) · ‹ Back 9990/9967.

## Keys

**Simple.** Up and Down move. Left or Right closes. Back on a sub-page goes back to Main. Back on Main closes.

**Wiring.**
| Key | Video 9000 | Music 9000 |
|---|---|---|
| Up | `noop` | `noop` |
| Down (last row) | `50` cast list | `9000` (stays) |
| Left / Right | `Close` | `Close` |
| Back on sub page | `ClearProperty(bz_ci_more)` + `AlarmClock(bzci_back,SetFocus(9980),00:00,silent)` | same |
| Back on Main | close | close |

Cast 50 Select opens Movies filtered by that actor and closes everything. Remove from library → `bz_ctx.py remove` → confirm (dialog-confirm.md).

## Legacy 1111

**Wiring.** `Custom_1111_XInfo.xml` runs `onload Dialog.Close(1111,true)` and `onunload` clears `bz_xinfo`. BezelXInfo was retired (t4166).

## Related
context-menu.md · dialog-confirm.md · favourites.md

**Section page (music) also:** Album View 9978 (above View Type) — A · 3B ALBUM / D · SONGS + DISCS (default D), skin bool `bz_albview_a`. See music-list.md.


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/DialogVideoInfo.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 50 | list | 593,476 | 352×108 | `noop/noop/9000/noop` | `!String.IsEmpty(Container(50).ListItem(0).Label)` |
| 9000 | grouplist | 582,166 | 360×276 | `Close/Close/noop/50` | `—` |
| 9980 | button | —,— | —×— | `—/—/9000/—` | `String.IsEmpty(Window.Property(bz_ci_more))` |
| 9969 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [String.IsEqual(ListItem.DBType,tvsho…` |
| 9979 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9971 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9972 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9973 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9989 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9981 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9982 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [Container.Content(MusicVideos)]` |
| 9983 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [System.HasLocks]` |
| 9984 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [Integer.IsGreater(Playlist.Length(vi…` |
| 9985 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [Container.Content(addons)]` |
| 9986 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [Container.Content() + String.IsEmpty…` |
| 9987 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [Container.Content(studios) + !System…` |
| 9988 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + [!String.IsEmpty(Container.PluginName)]` |
| 9990 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 8 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,tvshow) +…` |
| 9081 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + [String.IsEqual(ListItem.DBType,movie) | …` |
| 9082 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + [String.IsEqual(ListItem.DBType,movie) | …` |
| 9085 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + String.IsEqual(ListItem.DBType,tvshow)` |
| 11 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEmpty(ListItem.Trailer)` |
| 443 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEmpty(ListItem.SetID)` |
| 9089 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more))` |
| 7710 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 6 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 13 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1) + !String.IsEmpty(ListItem.Director)` |
| 7 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1) + Control.IsEnabled(7)` |
| 9095 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1) + !String.IsEqual(ListItem.DBType,season)` |
| 9097 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 9098 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1) + !String.IsEmpty(ListItem.DBID) + !Strin…` |
| 9096 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |

Actions (`onclick`/`onload`/`onback`) found:
- `Action(Queue)`
- `Action(ToggleWatched)`
- `ActivateWindow(Videos,videodb://movies/sets/$INFO[ListItem.SetId]/?setid=$INFO[ListItem.SetId],return)`
- `ActivateWindow(Videos,videodb://tvshows/titles/$INFO[ListItem.DBID]/,return)`
- `ActivateWindow(addonbrowser,addons://more/video/,return)`
- `ActivateWindow(videoplaylist)`
- `Addon.OpenSettings($INFO[Container.PluginName])`
- `AlarmClock(bzci_back,SetFocus(9000,1,absolute),00:00,silent)`
- `AlarmClock(bzci_back,SetFocus(9980),00:00,silent)`
- `AlarmClock(bzci_sec,SetFocus(9979),00:00,silent)`
- `ClearProperty(bz_ci_more)`
- `Container.NextSortMethod`
- `Container.SortDirection`
- `Dialog.Close(all,true)`
- `Dialog.Close(movieinformation)`
- `InstallAddon(resource.images.studios.white)`
- `QueueMedia($VAR[BzPlayNextPath],playnext)`
- `RunScript(special://skin/scripts/bz_cmd.py,chooseart,$INFO[ListItem.DBType],$INFO[ListItem.DBID])`
- `RunScript(special://skin/scripts/bz_ctx.py,fav)`
- `RunScript(special://skin/scripts/bz_ctx.py,remove,$INFO[ListItem.DBType],$INFO[ListItem.DBID])`
- `SendClick(10)`
- `SendClick(11)`
- `SendClick(16)`
- `SendClick(19)`
- `SendClick(622)`

**Source:** `xml/DialogMusicInfo.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 50 | list | -2000,0 | 10×10 | `—/—/—/—` | `false` |
| 9000 | grouplist | 582,166 | 360×420 | `Close/Close/noop/9000` | `—` |
| 9980 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 9978 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9979 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9971 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9972 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9973 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9974 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9975 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 9976 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + !Container.Content(addons)` |
| 9977 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + Integer.IsGreater(Playlist.Length(mus…` |
| 9978 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + Container.Content(addons)` |
| 9968 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + !String.IsEmpty(Container.PluginName)` |
| 9969 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec) + String.IsEmpty(Container.FolderPath) …` |
| 9967 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),sec)` |
| 8 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,artist)` |
| 9081 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,artist)` |
| 9082 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more))` |
| 9095 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more))` |
| 9083 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + !String.IsEqual(ListItem.DBType,artist) +…` |
| 9084 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more)) + String.IsEqual(ListItem.DBType,artist) + …` |
| 9089 | button | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window.Property(bz_ci_more))` |
| 7710 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 6 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 7 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1) + Control.IsEnabled(7)` |
| 12 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |
| 9096 | button | —,— | —×— | `—/—/—/—` | `String.IsEqual(Window.Property(bz_ci_more),1)` |

Actions (`onclick`/`onload`/`onback`) found:
- `Action(Queue)`
- `ActivateWindow(Music,"musicdb://albums/?artist=$VAR[BzCIArtistQ]&albumartistonly=true",return)`
- `ActivateWindow(Music,musicdb://artists/$INFO[ListItem.DBID]/,return)`
- `ActivateWindow(addonbrowser,addons://more/audio/,return)`
- `ActivateWindow(musicplaylist)`
- `Addon.Default.Set(xbmc.player.musicviz)`
- `Addon.OpenSettings($INFO[Container.PluginName])`
- `AlarmClock(bzci_back,SetFocus(9000,1,absolute),00:00,silent)`
- `AlarmClock(bzci_back,SetFocus(9980),00:00,silent)`
- `AlarmClock(bzci_sec,SetFocus(9979),00:00,silent)`
- `ClearProperty(bz_ci_more)`
- `Container.NextSortMethod`
- `Container.SortDirection`
- `Dialog.Close(all,true)`
- `Dialog.Close(musicinformation)`
- `QueueMedia($VAR[BzPlayNextPath],playnext)`
- `RunScript(special://skin/scripts/bz_cmd.py,chooseart,$INFO[ListItem.DBType],$INFO[ListItem.DBID])`
- `RunScript(special://skin/scripts/bz_ctx.py,fav)`
- `SendClick(16)`
- `SendClick(19)`
- `SendClick(622)`
- `SetFocus(9000,0,absolute)`
- `SetProperty(bz_ci_more,1)`
- `SetProperty(bz_ci_more,sec)`
- `Skin.Reset(bz_albumlist)`

**Source:** `xml/Custom_1111_XInfo.xml`

_No id’d controls in this file (layout comes from includes)._

Actions (`onclick`/`onload`/`onback`) found:
- `Dialog.Close(1111,true)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/info-options.md) · [state](../state/info-options.md) · [motion](../motion/info-options.md) · [art](../art/info-options.md) · [input](../input/info-options.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
