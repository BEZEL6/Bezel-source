# Playlists

**Object:** `MyPlaylist.xml` (default `60`, side `9000`: shuffle `20`, repeat `26`, save `21`, clear `22`); `MyMusicPlaylistEditor.xml` (default `6`, grouplist `9000`, buttons `6`/`7`/`8`, lists `50`/`100`)  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
- Now-playing queue (musicplaylist/videoplaylist): opened by Up next (1115 6409) or the side Playlist button 612.
- Saved playlists: `GO['playlists']` → music window `special://musicplaylists/`.
- onload: backdrop, start `bz_flip` if needed, `bz_sway_restart`.

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move |
| Select | Play from item |
| Menu / double-tap | Section menu 1119 (Play from here, Info, Move up/down, Remove, Shuffle, Repeat, Save, Clear) |
| Back | Previous window |
| Editor Left/Right | 9000 ↔ lists 50/100 via scrollbars 60/61 |

## Related
context-menu.md · music-controls.md
