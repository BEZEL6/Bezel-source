# Pictures

**Object:** `MyPics.xml` · view `63` (`View_63_BezelPictureList`, Includes_Bezel ~L2279) · side `9000` (`6`, `7`, `9` radio, `624`, `621`) · section menu `1119` (7940–7947)
**Where:** Opened from MM PICTURES (`bz_mm.py GO['pictures']`)
**Last updated:** 2026-11-01 · 5.33.242
**Status:** Live in 5.33.207. Kodi Pictures in BEZEL chrome. Back at the sources root, or Left when navok, opens the MM. Menu or double-tap opens the section menu. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
PICTURES on the main menu opens your picture sources. It fades in like every other section.

### How it works
- `bz_mm.py` clears `bz_nav`, so the MM closes, then activates `pictures`.
- The window fades in with `BezelWindowFade`.
- The MM global dim (`BezelSecDim`) is applied to the parent group.
- Focus always starts on picture view 63.

### Wiring
| Item | Value |
|---|---|
| Opener | `GO['pictures']`: `ClearProperty(bz_nav,home)` + `ActivateWindow(pictures)` |
| Window anim | `BezelWindowFade` (WindowOpen fade 0→100, 400 ms sine out) |
| Dim | `BezelSecDim` on the parent group (gdim / mmdim, 600 ms) |
| defaultcontrol | `always` 63 |
| Other includes | `DefaultBackground`, `BezelFanartCycler`, `ListThumbInfoPanel`, `BezelDtapHint`, `MediaMenu*` side menu |

---

## Getting back to the MM

### Simple
- At the top of Pictures, Back opens the main menu.
- Left opens it at any depth, as long as the menu isn't locked.
- Inside a folder, Back goes up a level as usual.

### How it works
- "Root" here means the folder path is empty or exactly `sources://pictures/`.
- List 63 and **every** side-menu button carry the same conditional onback, so Back from the side menu at root also opens the MM.
- In a subfolder the condition is false, so Kodi's own Back (parent folder) runs.
- Left uses `$EXP[bz_navok]`: no `bz_navlock`, no `bz_navgrace`, and the MM isn't already open.

### Wiring
| Control | Handler |
|---|---|
| 63 onback | `[String.IsEmpty(Container.FolderPath) \| String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_navmenu]` → `SetProperty(bz_nav,true,home)` |
| 63 onleft | `$EXP[bz_navok]` → `SetProperty(bz_nav,true,home)` |
| 6, 7, 9, 624, 621 onback | same root condition → `bz_nav=true` |

---

## Side menu

### Simple
The side menu has Slideshow, Recursive slideshow and Random. When relevant, it also shows Add-on settings and Get more.

### How it works
- These are Kodi's standard MyPics button IDs, so Kodi wires their actions.
- BEZEL adds the Back handling and two visibility gates: plugin settings only inside a plugin, and Get more only on add-on listings.

### Wiring
| ID | Label | Notes |
|---|---|---|
| 6 | `$LOCALIZE[13317]` | slideshow (Kodi) |
| 7 | `$LOCALIZE[13318]` | recursive slideshow (Kodi) |
| 9 | `$LOCALIZE[13319]` | random, radiobutton (Kodi) |
| 624 | `$LOCALIZE[10140]` | `Addon.OpenSettings($INFO[Container.PluginName])` · visible `!String.IsEmpty(Container.PluginName)` |
| 621 | `$LOCALIZE[21452]` | `ActivateWindow(addonbrowser,addons://more/image/,return)` · visible `Container.Content(addons)` |

---

## Section menu (1119) and double-tap

### Simple
Press Menu, or double-tap, for a short list: View, Open folder, Picture info, Slideshow, Recursive slideshow, Sort by, Order, Favourite.

### How it works
- `pictures` is in `bz_dtap.py` SECW. A single tap is Select after the tap window. A double tap (or c/menu/title via the noctx keymap) opens 1119 instead of Kodi's context menu.
- Each 1119 item closes the dialog first and then runs its action on a 0 s `AlarmClock(bzsc,…)`, so the action reaches the Pictures window and not the closing dialog.

### Wiring
| ID | Label | Action (after `Dialog.Close(1119,true)`) |
|---|---|---|
| 7940 | View | `Action(Select)` |
| 7941 | Open folder | `Action(Select)` |
| 7942 | Picture info | `Action(Info)` |
| 7943 | Slideshow | `SlideShow($INFO[Container.FolderPath])` |
| 7944 | Recursive slideshow | `SlideShow($INFO[Container.FolderPath],recursive)` |
| 7945 | Sort by | `Container.NextSortMethod` |
| 7946 | Order | `Container.SortDirection` |
| 7947 | Favourite | `RunScript(bz_ctx.py,fav)` |

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down / Select | Kodi defaults (open folder / view) |
| Left (`bz_navok`) | Open MM |
| Back at root | Open MM (also from side buttons) |
| Back in folder | Parent folder |
| Menu / double-tap / Info | Section menu 1119 |

## Touch
Double-tap = 1119 (`bz_dtap`). Single tap = Select after the tap window.

## Related
context-menu.md · media-sources.md · touch-group.md · section-transitions.md

## Warm strip (current, 5.33.242)

### Simple
Pictures now looks like Media Sources and the MM: your folders and pictures are rows inside the colour strip, the MM art stays behind, and the focused picture shows on the right. Nothing fades in — the strip is already there when the MM closes.

### How it works
- `View_63_BezelPictureList` (Includes_Bezel) puts list 63 at strip 570,120 (rows 48 px, 390 wide, » on folders) under `BezelMMStripChrome box=true`, title `BzPicTitle` (PICTURES at root, else folder name) + `PICTURES · N ITEMS` breadcrumb.
- Rows, title and footer hide under the MM (`!bz_navmenu`); the strip chrome stays, so the MM strip lands on an identical strip (no blink).
- MyPics wrapper group lost `BezelWindowFade` (234/1117 pattern). Held lane (bz_fan_a/b) draws behind; black + section fanart only when `bz_fan_on` is empty.
- Right: `BezelArtworkPanel` with resolution · date taken. The old info-pairs column was dropped.
- Back/Left/MM handlers on 63 unchanged; Up/Down wrap 63. Touch scrollbar at 952,232.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/pictures.md) · [state](../state/pictures.md) · [motion](../motion/pictures.md) · [art](../art/pictures.md) · [input](../input/pictures.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
