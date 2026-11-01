# Favourites

**Object:** `MyFavourites.xml` (Kodi `favourites`, 10060) · list `60` (`View_60_BezelInfoList`), grouplist `9000`; `scripts/bz_fav.py`, `scripts/bz_ctx.py fav`  
**Where:** Main Menu row FAVOURITES (`bz_mm.py fav`)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** FAVOURITES in the Main Menu opens Kodi Favourites as a BEZEL list with a random backdrop. Back opens the Main Menu.

**How it works.** GO `fav` closes the MM and opens the window. Backdrop pick and save work as in add-ons (addons.md). Favourites has no XML `onback`. The open-MM-on-Back at the root is done by `bz_flip.py`'s root-arm logic. A folder normally has to have been shown for 0.6 s (`bz_rootarm`) before Back opens the MM, so a held Back that arrives during the open cannot bounce you straight into the MM. Freshly opened windows 10060 (Favourites), 10001 and 10820 arm at once (5.33.179 BUG-024).

**Wiring.**
- Open: `bz_mm.py` GO `fav` = `ClearProperty(bz_nav)` + `ActivateWindow(Favourites)`.
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
