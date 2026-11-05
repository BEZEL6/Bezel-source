# File manager

**Object:** Kodi file manager · Kodi: `FileManager.xml` (`filemanager`), lists `20` / `21`, scrollbars `60` / `61` (off-screen)
**Where:** FILES (from Settings / tools)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Two file panes in the same spot: the one you're not using slides left and dims, so the active pane is in front. Left / Right swap panes, Up / Down move, Select opens, double-Select gives Kodi's copy / move / delete menu. Opens with a random backdrop; Back at the top of a pane opens the main menu.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Pane A / Pane B | open / Left / Right | Back at root → MM | active pane in front, the other slid left and dimmed |

### Timeline
pane swap: slide + dim of the inactive pane; window 400 fade-in.

### Interruptions
—

### Continuity
Under the MM the held art stays (Settings tree kid).

### Layering
Backdrop < inactive pane (dimmed) < active pane.

### Geometry
Both panes share one position; the inactive one offset left.

### Art
Random backdrop.

### Input
Left / Right swap panes; Up / Down move; Select opens; double Select → Kodi context menu; Back up / MM.

### Speed targets
—

### Never
No blank art under the MM (Settings kids hold).

### Acceptance checks
FILES → open a source → copy a file via the menu.

## Kodi implementation (sandbox)

### How it works (live detail; dated sections are the current state unless a later one supersedes them)
#### Open / close

**Simple.** It opens with a random backdrop. Back at the top of a pane opens the Main Menu.

**How it works.** It has no `always` default, so Kodi gives focus back to the pane you last used (5.33.145 BUG-002). The pane `onback` only opens the MM when that pane has no folder (the source list). Inside a folder, Back is Kodi's parent step.

**Wiring.**
- `defaultcontrol` 20 (no `always`). `onload` / `onunload` backdrop as in addons.md.
- 20/21 `onback` with `String.IsEmpty(Container(N).FolderPath) + !$EXP[bz_navmenu]` → `SetProperty(bz_nav,true,home)`.

#### Two panes

**Simple.** It has two lists in the same spot. The one you are not using slides left and dims, so the active pane is always in front.

**Wiring.** Lists 20 and 21: left 570, top 120, 390×900. Unfocused animation: slide to -450,0 and fade to 45 over 200 ms (sine). `pagecontrol` 60/61, `scrolltime` 200. Scrollbars 60/61 at left -400 (offscreen).

#### Keys

**Simple.** Left and Right swap panes. Up and Down move within a pane. Select opens. A double-tap gives Kodi's context menu (copy/move/delete).

**Wiring.**
| Key | 20 | 21 |
|---|---|---|
| Left / Right | 21 | 20 |
| Up / Down | 20 | 21 |
| Double-tap | `bz_dtap.info()` → `Action(ContextMenu)` | same |

### Wiring
See the detail above.

### Kodi workarounds (do not port)
Kodi file manager windows; stock-style keyboard kept by Rob.

## Related
[filebrowser](filebrowser.md) · [settings](settings.md) · [keyboard](keyboard.md)
