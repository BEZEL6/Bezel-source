# File manager

**Object:** `FileManager.xml` · lists `20` / `21`, scrollbars `60` / `61`, labels `101` / `102`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Kodi two-pane file manager (`GO['files']`).

## Keys
| Key | Behavior |
|---|---|
| Left / Right | Switch pane 20 ↔ 21 |
| Up / Down | Move; top/bottom stay (no wrap) |
| Select | Open |
| Back with empty FolderPath + MM closed | Open MM (`bz_nav=true`) |
| Double-tap Select / Menu | Kodi `Action(ContextMenu)` (5.33.144) |

## Window props
onload backdrop; onunload saves/clears backdrop.

## Related
filebrowser.md · keymaps.md
