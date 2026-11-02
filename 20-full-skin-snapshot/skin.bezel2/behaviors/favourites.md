# Favourites

**Object:** `MyFavourites.xml` (Kodi `favourites`, 10060) · list `60` (`View_60_BezelInfoList`), grouplist `9000`; `scripts/bz_fav.py`, `scripts/bz_ctx.py fav`  
**Where:** Main Menu row FAVOURITES (`bz_mm.py fav`)  
**Last updated:** 2026-11-02 · 5.33.344  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** FAVOURITES in the Main Menu opens Kodi Favourites as a BEZEL list with a random backdrop. Back opens the Main Menu.

**How it works.** GO `fav` closes the MM and opens the window. Backdrop pick and save work as in add-ons (addons.md). Favourites has no XML `onback`. The open-MM-on-Back at the root is done by `bz_flip.py`'s root-arm logic. A folder normally has to have been shown for 0.6 s (`bz_rootarm`) before Back opens the MM, so a held Back that arrives during the open cannot bounce you straight into the MM. Freshly opened windows 10060 (Favourites), 10001 and 10820 arm at once (5.33.179 BUG-024).

**Wiring.**
- Open: `bz_mm.py` GO `fav` = `ClearProperty(bz_nav)` + `ActivateWindow(favouritesbrowser)`; the Home-strip Favourites button (Includes_Bezel ~496) uses the same name. Kodi 21 only knows `favouritesbrowser` (10060). The old `Favourites` name does nothing, so the MM closed onto the last section (5.33.344 fix, t2489).
- `<defaultcontrol always="true">60</defaultcontrol>`. `onload` `bz_cmd.py backdrop`. `onunload` saves `bz_backdrop_last` and clears `bz_backdrop`, `bz_minibig`.
- Includes: `BezelSecDim`, `View_60_BezelInfoList`, `BezelDtapHint`, `BezelFanartCycler`, grouplist 9000 `MediaMenu`, `BezelMiniPlayer`, `BezelLogoButton`.
- Back: `bz_flip.py` ~884 root-arm (`bz_rootarm`, `bz_navroot` / `bz_atnavroot`).

## Keys

**Simple.** Up and Down move. Select runs the favourite. Left opens the MM. Back opens the MM. A double-tap opens the Options menu where the window supports it.

**Wiring.** List 60 comes from `View_60_BezelInfoList` (shared section list behavior, including the MM focus bounces). I did not re-trace the Left→MM handler inside that include for this doc. The dtap hint is from `BezelDtapHint`.

## Adding favourites

**Simple.** Add from the BEZEL Options/section menu ("Favourite"), or toggle the playing file.

**How it works.** `bz_fav.py` toggles the current playing file through Kodi's `Favourites.AddFavourite` and stores the path in Home `bz_favpath`, so the star state can be shown. `bz_ctx.py fav` builds the right favourite type for the focused item.

**Wiring.**
- `bz_ctx.py fav`: media → media favourite. Add-on in programs/games/addonbrowser → script favourite, or window/videos favourite for plugins. Notification "Added to favourites" / "Could not add favourite", 2000 ms.
- `bz_ctx.py remove <type> <id>`: yes/no "Remove from library" → `Dialog.Close(all)` → `VideoLibrary.Remove*` → `Container.Refresh` (library, not favourites).

## Related
context-menu.md · info-options.md · addons.md · mm-list.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/MyFavourites.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 9000 | grouplist | —,50 | —×— | `—/—/—/—` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `RunScript(special://skin/scripts/bz_cmd.py,backdrop)`

**Source:** `xml/Includes_Bezel.xml` include `View_60_BezelInfoList`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 6891 | button | 894,144 | 45×32 | `—/—/—/—` | `false` |
| 6077 | textbox | 612,622 | 306×344 | `—/—/—/—` | `!$EXP[bz_infoup] + !$EXP[bz_ameta]` |
| 60 | list | 0,0 | 450×900 | `SetProperty(bz_vback_close,true,home)/SetFocus(6095)/SetProperty(bz_topedge,1,home)/6097` | `—` |
| 6097 | button | 0,0 | 450×60 | `SetProperty(bz_nav,true,home)/—/SetFocus(60,$INFO[Window(Home).Property(bz_allup)],absolute)/noop` | `!$EXP[bz_covercol] | $EXP[bz_allpick]` |
| 6140 | list | -4000,0 | 10×10 | `—/—/—/—` | `[Window.IsActive(music) | Window.IsActive(musicplaylist)] + [Container.Content(artists)…` |
| 6141 | list | -4000,20 | 10×10 | `—/—/—/—` | `[Window.IsActive(music) | Window.IsActive(musicplaylist)] + [Container.Content(artists)…` |
| 6100 | grouplist | 78,151 | 36×837 | `60/60/—/—` | `!$EXP[bz_navmenu]` |
| 6101 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6102 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6103 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6104 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6105 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6106 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6107 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6108 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6109 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6110 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6111 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6112 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6113 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6114 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6115 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6116 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6117 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6118 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6119 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6120 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6121 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6122 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6123 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6124 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6125 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6126 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6127 | button | —,— | 36×31 | `—/—/—/—` | `—` |
| 6886 | button | —,— | auto×32 | `60/60/60/60` | `—` |
| 6367 | grouplist | 0,0 | 1920×1080 | `—/—/—/—` | `String.IsEqual(Skin.String(bz_at_fsslide),1)` |
| 6368 | button | —,— | 1×1 | `—/—/—/—` | `—` |
| 6369 | button | —,— | 480×1 | `SetFocus(6368)/SetFocus(6368)/SetFocus(6368)/SetFocus(6368)` | `—` |
| 6377 | grouplist | 0,0 | 1920×1080 | `—/—/—/—` | `String.IsEqual(Skin.String(bz_at_fsslide),2)` |
| 6378 | button | —,— | 1×1 | `—/—/—/—` | `—` |
| … | 8 more ids not listed | | | | |

Actions (`onclick`/`onload`/`onback`) found:
- `60`
- `6299`
- `Action(Select)`
- `Action(firstpage)`
- `Action(lastpage)`
- `Action(nextletter)`
- `ActivateWindow(1115)`
- `ActivateWindow(1117)`
- `ActivateWindow(1121)`
- `ActivateWindow(12006)`
- `ActivateWindow(visualisation)`
- `ClearProperty(bezel_jump,home)`
- `ClearProperty(bz_nav,home)`
- `ClearProperty(bz_navbez,home)`
- `ClearProperty(bz_navtune,home)`
- `ClearProperty(bz_np,home)`
- `Control.Move(60,-1)`
- `RunScript(special://skin/scripts/bz_cmd.py,allrow)`
- `SetFocus(60)`
- `SetFocus(60,$INFO[Container(6140).CurrentItem],absolute)`
- `SetFocus(6140,0,absolute)`
- `SetFocus(6368)`
- `SetFocus(6378)`
- `SetFocus(6383)`
- `SetFocus(6390)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/favourites.md) · [state](../state/favourites.md) · [motion](../motion/favourites.md) · [art](../art/favourites.md) · [input](../input/favourites.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
