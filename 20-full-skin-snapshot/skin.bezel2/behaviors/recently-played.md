# Recently played

**Object:** MM row RECENTLY PLAYED → `bz_mm.py GO['recent']` → music window `musicdb://recentlyplayedalbums/` (`bz_navroot` set)
**Where:** Main menu → Music window
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Opens Music on recently played albums. That path is registered as the nav root, so Back there opens the MM. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open

### Simple
RECENTLY PLAYED on the main menu takes you to Music, showing the albums you played most recently. From there it behaves exactly like the music list.

### How it works
1. The MM row first sets `bz_navroot` to the recently-played path, so BEZEL treats that folder as "home" for this visit.
2. It then runs `bz_cmd.py tomusic` with the path:
   - If 1112 Now Playing is open, it's closed first.
   - The music window loads behind the menu, held hidden (`bz_secload`) until the list and focused art are in, with a 3 s cap.
   - Then the MM closes and the section fades in once (`bz_secfade`, 400 ms).
   - If MM warm already loaded this exact list, the menu just closes.

### Wiring
| Item | Value |
|---|---|
| Opener | `SetProperty(bz_navroot,musicdb://recentlyplayedalbums/,home)` · `RunScript(bz_cmd.py,tomusic,musicdb://recentlyplayedalbums/)` |
| Load | `_bz_load_then_close` (`bz_secload` / `bz_secfade`, 3 s cap; warm short-cut) |

---

## Back / Left to MM

### Simple
- Back at the recently-played list opens the main menu.
- Left opens it whenever the A–Z bar isn't showing.
- Inside an album, Back steps out first.

### How it works
- After the folder has been shown for 0.6 s, `bz_flip` sets `bz_rootarm`. It also sets `bz_atnavroot`, because the folder equals `bz_navroot`.
- That makes `bz_atroot` true, so list 60 onback opens the MM (when `bz_navok`).
- Left uses list 60's onleft: A–Z bars 6500/6100 hidden + `bz_navok` → MM.

### Wiring
- `bz_flip.py` ~L711: `bz_rootarm` when the folder is in ROOTS or equals `bz_navroot`.
- `bz_atroot` (Includes_Bezel ~L2323) requires `bz_rootarm`.
- List 60 onback / onleft: see music-list.md.

---

## Keys
Same as music-list.md: Up/Down (Up wrap to the ALL row 6097 when it's visible), Select opens or plays, Left (A–Z hidden + navok) → MM, Back at root (`bz_atroot`) → MM.

## Touch
Same as music-list.md.

## Related
mm-list.md · music-list.md · mm-warm.md
