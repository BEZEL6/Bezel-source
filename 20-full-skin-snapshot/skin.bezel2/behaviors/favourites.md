# Favourites

**Object:** Favourites · Kodi: `MyFavourites.xml` (`favouritesbrowser`, 10060), list `60` (`View_60_BezelInfoList`), grouplist `9000`, `scripts/bz_fav.py`, `scripts/bz_ctx.py fav`
**Where:** MM FAVOURITES
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
FAVOURITES opens Kodi favourites as a Bezel strip list over a random backdrop. Select runs a favourite; Left or Back opens the main menu. Add favourites from the Options / section menu ("Favourite"), which picks the right kind for the focused item.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| List | MM FAVOURITES | Back / Left → MM; Select → runs | strip list, backdrop |

### Timeline
Open: 400 fade-in (sine out). Add / remove notifications: 2000 ms.

### Interruptions
—

### Continuity
Under the MM the last Music / Movies / TV art is held.

### Layering
Backdrop < strip list < MM.

### Geometry
Strip list (as the other sections).

### Art
Random backdrop each visit.

### Input
Up / Down move; Select runs; Left / Back → MM; double Select → Options.

### Speed targets
—

### Never
No blank art under the MM after Favourites (WARM HOLD).

### Acceptance checks
Add a movie via Options › Favourite → appears; FAVOURITES → Select → plays; Back → MM.

## Kodi implementation (sandbox)

### How it works
- GO `fav`: `ClearProperty(bz_nav)` + `ActivateWindow(favouritesbrowser)` (Kodi 21 name).
- defaultcontrol `always` 60; onload `bz_cmd.py backdrop`; onunload save / clear backdrop.
- Back at root via bz_flip root-arm (`bz_rootarm`, `bz_navroot` / `bz_atnavroot`); no XML onback.
- `bz_ctx.py fav`: media → media favourite; add-on in programs / games / addonbrowser → script favourite, plugin → window favourite; notification 2000 ms. `bz_fav.py` toggles the playing file and stores `bz_favpath`.

### Wiring
| Item | Value |
|---|---|
| Includes | `BezelSecDim`, `View_60_BezelInfoList`, `BezelDtapHint`, `BezelFanartCycler`, `MediaMenu`, `BezelMiniPlayer`, `BezelLogoButton` |

### Kodi workarounds (do not port)
Favourite type selection per Kodi object kind.

## Related
[context-menu](context-menu.md) · [info-options](info-options.md) · [addons](addons.md) · [mm-list](mm-list.md)
