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
