# Options + Info

**Object:** `DialogVideoInfo.xml` / `DialogMusicInfo.xml` · grouplist `9000`, cast list `50`; `Custom_1111_XInfo.xml` (1111 — closes itself on load; legacy)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
BEZEL Options+Info replaces both Info and the context menu for Movies/TV/Music/Pictures. It opens with Info, Menu/C, or double-tap Select (bz_dtap). Three pages are switched by Window property `bz_ci_more`:
- **Main (empty):** Video → Play 8 · Play next 9081 · Queue 9082 · Browse seasons 9085 · Trailer 11 · Browse set 443 · More options 9089. Music → Play 8 · Play next 9081 · Queue 9082 · Favourite 9095 · Browse 9083/9084 · More options 9089.
- **More (`1`):** Choose art 7710 · Refresh 6 · Set rating 7 · Director 13 / watched 9095 / Add to favourites 9097 / Remove from library 9098 (video) · Other 12 (music) · Section options 9980 (music) · ‹ Back 9096.
- **Section (`sec`):** View type 9979 · Sort 9971 · Filter / Order · Update library · Party mode · Go to playlist · Get more · Edit nodes · Add-on settings · Clearart toggle 9969 (`bz_tvclear_off`, video) · Visualizer 9974 (music) · ‹ Back 9990/9967.

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move in 9000 (top noop); Down from last → cast list 50 (video) |
| Left / Right in 9000 | Close |
| Cast 50 Select | Open Movies filtered by that actor, close all |
| Back on a sub page | `ClearProperty(bz_ci_more)` → main, focus 9980 |
| Back on main | Close |

## Related
context-menu.md · dialog-confirm.md · favourites.md
