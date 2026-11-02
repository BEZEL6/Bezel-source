# Search (dialog 1107)

**Object:** `Custom_1107_SearchDialog.xml` dialog `1107` · list `9000` (3 static rows)
**Where:** Opened from MM SEARCH (`bz_mm.py GO['search']`)
**Last updated:** 2026-11-01 (5.33.235)
**Status:** Live in 5.33.207. Three search rows; Back returns to the MM. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
Pick SEARCH on the main menu and a small panel offers three kinds of search. Back closes it and puts you back on the main menu.

### How it works
1. `bz_mm.py` clears `bz_nav` first, so the MM starts closing.
2. It then opens 1107, which fades in with the standard section fade.
3. Focus is pinned to list 9000. Every direction points back at 9000, so you can't wander off the list.
4. Back sets `bz_nav=true` (the MM reopens on its row), then `Dialog.Close(1107,true)` closes the dialog (a control onback consumes Back, so Kodi will not close it by itself).

### Wiring
| Item | Value |
|---|---|
| Opener | `bz_mm.py` GO search: `ClearProperty(bz_nav,home)` + `ActivateWindow(1107)` |
| Window | dialog, include `BezelSecFadeInDialog` (WindowOpen fade 0→100, 400 ms sine out, `DepthDialog`) |
| defaultcontrol | `always` 9000 |
| List 9000 | onup/ondown/onleft/onright → 9000 · onback `SetProperty(bz_nav,true,home)` + `Dialog.Close(1107,true)` · static content |

---

## Rows

### Simple
- **Global search** searches movies, shows, music and more across the whole library.
- **Add-on search** finds add-ons in your repositories.
- **YouTube** search.

If an add-on is missing, Select installs it. If it's disabled, Select enables it. After that, press Select again to search.

### How it works
- Every row first closes all dialogs (`Dialog.Close(all)`), so the search window opens cleanly.
- Then exactly one conditional action runs, depending on the add-on: run it when it's enabled, enable it when it's installed but disabled, or install it when it's missing.
- Install and enable don't launch the search in the same press.
- A label under the list shows the focused row's label and description (Label2).

### Wiring
| Row | Label | Actions after `Dialog.Close(all)` |
|---|---|---|
| 1 | `$LOCALIZE[31113]` | enabled → `RunScript(script.globalsearch)` · installed+disabled → `EnableAddon(script.globalsearch)` · missing → `InstallAddon(script.globalsearch)` |
| 2 | `$LOCALIZE[31145]` | `ActivateWindow(addonbrowser,addons://search/,return)` |
| 3 | `$LOCALIZE[31114]` | enabled → `ActivateWindow(videos,"plugin://plugin.video.youtube/kodion/search/list/",return)` · else Enable / Install `plugin.video.youtube` |

- Header label "SEARCH". Footer "OK select   BACK close". Detail labels: `Container(9000).ListItem.Label` / `Label2`.

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move in 9000 (all directions stay in 9000) |
| Select | Run row |
| Back | `bz_nav=true` → close → MM |

## Touch
None specified.

## Related
mm-list.md · section-transitions.md

## Text entry
Search text uses the strip keyboard (`BzStripKeyboard`, see keyboard.md) since 5.33.239.


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Custom_1107_SearchDialog.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 9000 | list | 40,80 | 370×740 | `9000/9000/9000/9000` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `Dialog.Close(1107,true)`
- `SetProperty(bz_nav,true,home)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/search.md) · [state](../state/search.md) · [motion](../motion/search.md) · [art](../art/search.md) · [input](../input/search.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
