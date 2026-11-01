# File manager

**Object:** `FileManager.xml` (Kodi `filemanager`) · lists `20` / `21`, scrollbars `60` / `61` (offscreen)  
**Where:** Main Menu row FILES (GO `files` → `ActivateWindow(filemanager)`)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** It opens with a random backdrop. Back at the top of a pane opens the Main Menu.

**How it works.** It has no `always` default, so Kodi gives focus back to the pane you last used (5.33.145 BUG-002). The pane `onback` only opens the MM when that pane has no folder (the source list). Inside a folder, Back is Kodi's parent step.

**Wiring.**
- `defaultcontrol` 20 (no `always`). `onload` / `onunload` backdrop as in addons.md.
- 20/21 `onback` with `String.IsEmpty(Container(N).FolderPath) + !$EXP[bz_navmenu]` → `SetProperty(bz_nav,true,home)`.

## Two panes

**Simple.** It has two lists in the same spot. The one you are not using slides left and dims, so the active pane is always in front.

**Wiring.** Lists 20 and 21: left 570, top 120, 390×900. Unfocused animation: slide to -450,0 and fade to 45 over 200 ms (sine). `pagecontrol` 60/61, `scrolltime` 200. Scrollbars 60/61 at left -400 (offscreen).

## Keys

**Simple.** Left and Right swap panes. Up and Down move within a pane. Select opens. A double-tap gives Kodi's context menu (copy/move/delete).

**Wiring.**
| Key | 20 | 21 |
|---|---|---|
| Left / Right | 21 | 20 |
| Up / Down | 20 | 21 |
| Double-tap | `bz_dtap.info()` → `Action(ContextMenu)` | same |

## Related
filebrowser.md · media-sources.md · addons.md · keymaps.md
