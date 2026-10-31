# Favourites

**Object:** `MyFavourites.xml` · default `60` · side grouplist `9000`; `scripts/bz_fav.py` (now-playing favourite toggle); `bz_ctx.py fav` (add from menus)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Kodi Favourites window, opened from MM FAVOURITES (`GO['fav']` → `ClearProperty(bz_nav)` + `ActivateWindow(Favourites)`).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move rows |
| Select | Run favourite |
| Back at top level | Straight to MM (armed on open, 5.33.179 BUG-024) |
| Back in subfolder | Previous level |
| Left (`bz_navok`) | Open MM |

## Adding / removing
- Section menu / Info "Favourite" → `bz_ctx.py fav`
- Playing song: `bz_fav.py` toggles it with AddFavourite (adding an existing one removes it) and sets Home `bz_favpath` so the lit Favourite button shows the state.

## Window props
onload `bz_cmd.py backdrop`; onunload `bz_backdrop_last` + clears `bz_backdrop`, `bz_minibig`.

## Related
mm-list.md · context-menu.md · info-options.md
