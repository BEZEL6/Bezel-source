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
