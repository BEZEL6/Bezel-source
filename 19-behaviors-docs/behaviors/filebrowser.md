# File browser

**Object:** `FileBrowser.xml` (Kodi `filebrowser`) · panels `450`/`451`, button grouplist `9100`, scrollbar `60` (hidden), label `412`  
**Where:** Kodi pick-file / pick-folder dialog (Add source, Import, etc.)  
**Last updated:** 2026-11-01 · 5.33.223 (built, not smoked)  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Current layout (5.33.223 Warm strip)
Warm strip like 1130/1131/1117: group at 570,120, full-screen 8C dim, `BezelMMStripChrome box=true`. 411 title, 412 path crumb. Panels 450/451: width 390, rows 48, `$VAR[BzATHiTex]`/`BzATHiCol`/`BzATHiText` highlight; folders show », files show size + ✓. Grouplist 9100 is now a horizontal row of np_pill32 pills (413 OK, 414 Cancel, 415/416 when enabled) at y 808. 60 hidden. Nav: 450 Left/Right/Down → 9100; 9100 Up/Down → 450. Footer hint + FileBrowserSelectLabel.
**Classic fallback:** `xml/FileBrowser.xml.classic.bak` (classic double pane; copy over FileBrowser.xml to restore). Kept until every picker screen is designed. The tables below describe the classic nav.

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


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/FileBrowser.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 411 | label | 34,30 | 340×48 | `—/—/—/—` | `—` |
| 412 | label | 36,78 | 336×24 | `—/—/—/—` | `—` |
| 450 | panel | 0,112 | 390×672 | `9100/9100/450/9100` | `—` |
| 451 | panel | 0,112 | 390×672 | `9100/9100/451/9100` | `—` |
| 60 | scrollbar | 380,112 | 8×672 | `450/9100/—/—` | `false` |
| 9100 | grouplist | 20,808 | 360×32 | `9100/9100/450/450` | `—` |
| 413 | button | —,— | 70×32 | `—/—/—/—` | `—` |
| 414 | button | —,— | 100×32 | `—/—/—/—` | `—` |
| 415 | button | —,— | 120×32 | `—/—/—/—` | `Control.IsEnabled(415)` |
| 416 | button | —,— | 120×32 | `—/—/—/—` | `Control.IsEnabled(416)` |

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/filebrowser.md) · [state](../state/filebrowser.md) · [motion](../motion/filebrowser.md) · [art](../art/filebrowser.md) · [input](../input/filebrowser.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
