# File browser

**Object:** Kodi's pick-file / pick-folder dialog · Kodi: `FileBrowser.xml` (`filebrowser`), panels `450` / `451`, buttons `9100`, scrollbar `60` (hidden), label `412`
**Where:** Add source, import and other "browse for" actions; Warm strip look
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Kodi's picker for a file or folder, in the Bezel strip look: browse in the list, buttons (OK, Cancel, new folder …) on the left. Up / Down move, Left goes to the buttons, Select opens a folder or picks, double-Select gives Kodi's own context menu (the one place Bezel keeps it).

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Browsing | a browse action | OK / Cancel / Back | path label, list, buttons |

### Timeline
400 fade-in (sine out); no close animation.

### Interruptions
—

### Continuity
Returns to the dialog that asked (e.g. Add Source) with the picked path.

### Layering
Caller dialog < picker (strip chrome) .

### Geometry
Strip column layout (Warm strip).

### Art
Folder / file icons.

### Input
Up / Down move; Left → buttons; Right → scrollbar; Select open / pick; double Select → Kodi context menu; Back → up / cancel.

### Speed targets
—

### Never
No Bezel section menu here (Kodi's menu is needed for file actions).

### Acceptance checks
Media sources › Add source › Browse → pick a folder → OK → path filled in.

## Kodi implementation (sandbox)

### How it works (live detail; dated sections are the current state unless a later one supersedes them)
#### Current layout (5.33.223 Warm strip)
Warm strip like 1130/1131/1117: group at 570,120, full-screen 8C dim, `BezelMMStripChrome box=true`. 411 title, 412 path crumb. Panels 450/451: width 390, rows 48, `$VAR[BzATHiTex]`/`BzATHiCol`/`BzATHiText` highlight; folders show », files show size + ✓. Grouplist 9100 is now a horizontal row of np_pill32 pills (413 OK, 414 Cancel, 415/416 when enabled) at y 808. 60 hidden. Nav: 450 Left/Right/Down → 9100; 9100 Up/Down → 450. Footer hint + FileBrowserSelectLabel.
**Classic fallback:** `xml/FileBrowser.xml.classic.bak` (classic double pane; copy over FileBrowser.xml to restore). Kept until every picker screen is designed. The tables below describe the classic nav.

#### What it does

**Simple.** Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**How it works.** This is a Kodi system dialog. BEZEL restyles it and fixes the navigation so focus always starts in the panel and moves in a loop: buttons ↔ panel ↔ scrollbar. Dust is hidden while it is open (dust.md).

**Wiring.** `<defaultcontrol always="true">450</defaultcontrol>`. 451 is Kodi's alternate panel (thumb view).

#### Keys

**Simple.** Up and Down move through the list. Left goes to the buttons. Right goes to the scrollbar. Select opens the folder or picks the item. A double-tap gives Kodi's own context menu.

**How it works.** The dtap keymap includes `filebrowser`. A single Select goes through `bz_dtap` (it fires after the tap window). A second tap inside the window runs `info()`, which for filebrowser is `Action(ContextMenu)` (5.33.99).

**Wiring.**
| Control | Left | Right | Up / Down |
|---|---|---|---|
| 9100 buttons | 450 | 450 | 9100 |
| 450 panel | 9100 | 60 | 450 (stay) |
| 451 panel | 9100 | 60 | 451 (stay) |
| 60 scrollbar | 450 | 9100 | — |

### Wiring
See the detail above.

### Kodi workarounds (do not port)
Kodi pickers are fixed dialogs; Bezel only restyles them.

## Related
[media-sources](media-sources.md) · [files-filemanager](files-filemanager.md) · [context-menu](context-menu.md)
