# Music OSD / viz settings (dialog 1105)

**Object:** `Custom_1105_MusicOSDSettings.xml` dialog `1105` · grouplist `5000` · rows `5001`, `5002`, `5004–5009`
**Where:** Kodi-style settings popup for the music visualisation and lyrics
**Last updated:** 2026-10-31
**Status:** Present in the 5.33.207 tree. **No opener found:** nothing in `xml/` or `scripts/` calls `ActivateWindow(1105)`, so it may be reachable only through Kodi's internal music OSD settings ID. Per-viz settings in BEZEL normally go through Music controls 1115 (music-controls.md). Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Rows

### Simple
A short list of music-visualisation options: hide or animate the background fan art, pick a visualisation, open its settings or presets, choose a lyrics add-on, or get more visualisations.

### How it works
- All rows sit in one vertical grouplist (5000). Kodi moves focus inside it, and Up/Down at either end stays put (onup/ondown point back to 5000).
- The two fan art rows are radiobuttons. They flip a skin bool, and the tick shows the *inverse* of the "hide" setting, so ticked means on.
- Rows that open another dialog (choose viz, Get more) close this one first, so dialogs don't stack.
- The presets row only appears when the active viz reports presets. The lyrics-settings row only appears once a lyrics add-on is chosen.

### Wiring
| ID | Type | Action | Visible |
|---|---|---|---|
| 5001 | radiobutton | `Skin.ToggleSetting(hide_background_fanart)`; selected = `!Skin.HasSetting(hide_background_fanart)` | always |
| 5002 | radiobutton | toggles `animate_background_fanart` | always |
| 5004 | button | Close + `Addon.Default.Set(xbmc.player.musicviz)` | always |
| 5005 | button | `Addon.Default.OpenSettings(xbmc.player.musicviz)` | always |
| 5006 | visualisationpresetlist | Kodi preset picker | `Visualisation.HasPresets` |
| 5007 | button | `Skin.SetAddon(LyricScript_Path,xbmc.python.lyrics)` | always |
| 5008 | button | OpenSettings for `LyricScript_Path` | `!String.IsEmpty(Skin.String(LyricScript_Path))` |
| 5009 | button | `Dialog.Close(all)` + `ActivateWindow(AddonBrowser,addons://repository.xbmc.org/xbmc.player.musicviz/)` | always |

- `defaultcontrol` 5000. Window anim: `Animation_DialogPopupOpenClose`.

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move; ends stay |
| Select | Toggle / run row |
| Back | Close (Kodi default) |

## Unverified
- Entry point: no `ActivateWindow(1105)` anywhere in the tree (grep of xml + scripts, 2026-10-31).

## Related
music-controls.md · fanart-fs.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Custom_1105_MusicOSDSettings.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 5000 | grouplist | —,— | 600×700 | `—/—/5000/5000` | `—` |
| 5001 | radiobutton | —,— | 600×— | `—/—/—/—` | `—` |
| 5002 | radiobutton | —,— | —×— | `—/—/—/—` | `—` |
| 5004 | button | —,— | 600×— | `—/—/—/—` | `—` |
| 5005 | button | —,— | 600×— | `—/—/—/—` | `—` |
| 5006 | button | —,— | 600×— | `—/—/—/—` | `Visualisation.HasPresets` |
| 5007 | button | —,— | 600×— | `—/—/—/—` | `—` |
| 5008 | button | —,— | 600×— | `—/—/—/—` | `!String.IsEmpty(Skin.String(LyricScript_Path))` |
| 5009 | button | —,— | 600×— | `—/—/—/—` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `ActivateWindow(AddonBrowser,addons://repository.xbmc.org/xbmc.player.musicviz/,return)`
- `ActivateWindow(visualisationpresetlist)`
- `Addon.Default.OpenSettings(xbmc.player.musicviz)`
- `Addon.Default.Set(xbmc.player.musicviz)`
- `Addon.OpenSettings($INFO[Skin.String(LyricScript_Path)])`
- `Dialog.Close(1105)`
- `Dialog.Close(all)`
- `Skin.SetAddon(LyricScript_Path,xbmc.python.lyrics)`
- `Skin.ToggleSetting(animate_background_fanart)`
- `Skin.ToggleSetting(hide_background_fanart)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/music-viz-settings.md) · [state](../state/music-viz-settings.md) · [motion](../motion/music-viz-settings.md) · [art](../art/music-viz-settings.md) · [input](../input/music-viz-settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## DustViz auto-install (5.33.358)
`scripts/bz_dustviz.py` copies the bundled `visualization.bezel` from `resources/dustviz/<plat>/` into `special://home/addons/` when versions differ, enables it, and sets it as the music visualisation. Platforms: `windows` (x64 DX11 dll), `android` (Shield aarch64 GLES), `linux` (desktop). Any other platform is skipped.
