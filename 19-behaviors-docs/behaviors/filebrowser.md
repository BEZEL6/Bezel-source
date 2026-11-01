# File browser

**Object:** `FileBrowser.xml` (Kodi `filebrowser`) · panels `450`/`451`, button grouplist `9100`, scrollbar `60` (hidden), label `412`  
**Where:** Kodi pick-file / pick-folder dialog (Add source, Import, etc.)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it does

**Simple.** Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**How it works.** This is a Kodi system dialog. BEZEL restyles it and fixes the navigation so focus always starts in the panel and moves in a loop: buttons ↔ panel ↔ scrollbar. Dust is hidden while it is open (dust.md).

**Wiring.** `<defaultcontrol always="true">450</defaultcontrol>`. 451 is Kodi's alternate panel (thumb view).

## Keys

**Simple.** Up and Down move through the list. Left goes to the buttons. Right goes to the scrollbar. Select opens the folder or picks the item. A double-tap gives Kodi's own context menu.

**How it works.** The dtap keymap includes `filebrowser`. A single Select goes through `bz_dtap` (it fires after the tap window). A second tap inside the window runs `info()`, which for filebrowser is `Action(ContextMenu)` (5.33.99).

**Wiring.**
| Control | Left | Right | Up / Down |
|---|---|---|---|
| 9100 buttons | 450 | 450 | 9100 |
| 450 panel | 9100 | 60 | 450 (stay) |
| 451 panel | 9100 | 60 | 451 (stay) |
| 60 scrollbar | 450 | 9100 | — |

## Related
files-filemanager.md · media-sources.md · keymaps.md
