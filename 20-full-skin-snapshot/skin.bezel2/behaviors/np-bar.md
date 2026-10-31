# NP bar / now-playing chrome

**Object:** `Includes_Bezel.xml` — expression `bz_np` / Home prop `bz_np`; music window `6385` (np toggle), `6390` (NP focus)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Now-playing chrome on section screens while media plays. Home `bz_np` marks NP mode; `bz_np_was` is saved on music-window unload and `bz_np` is cleared unless the next window is visualisation.

## Keys
| Key | Behavior |
|---|---|
| Focus landing on 6385 | If NP showing → focus 6390 and `bz_cmd.py npctl,toggle`; else → side menu 9000 |
| `bz_np_focus=true` on music load | Focus 6390 |

Under MM the transport is the mini-player (mm-mini-player.md). In Music the compact NP rides grouplist 6397 with the big album (now-playing.md).

## Related
mm-mini-player.md · now-playing.md · music-list.md
