# Touch / tap inputs

**Object:** Cross-object. The logo-back button (`Includes_Bezel.xml`), the tap targets in `Includes_Bezel.xml` / `Custom_1120_PlayNext.xml`, and the double-tap service `scripts/bz_dtap.py`, plus the Tuner rows `dtap` / `dtapwin`
**Where:** Global (logo), music strip, Fanart FS, Play Next 1120, every section window (double-tap)
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Touch only does what each object's doc specifies. Double-tap Select is a Tuner option. There is **no touch master toggle** in the live tree. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

## Rule
Touch only does what Rob specified per object. Each object's file lists its own touch actions.

---

## Logo = Back

### Simple
Tap the BEZEL logo in the top-left corner to go back. This works everywhere except fullscreen video and the video OSD.

### How it works
- An invisible 120×116 button sits over the logo corner.
- It has no ID, so remote focus never lands on it. Only a mouse or touch can hit it.
- Where `BezelLogoButton` 6001 exists, that button sits above it and handles the tap itself.

### Wiring
| Item | Value |
|---|---|
| Button | `Includes_Bezel.xml` L572 · 0,0 120×116 · no textures |
| Visible | `!Window.IsActive(FullscreenVideo) + !Window.IsActive(VideoOSD)` |
| onclick | `Action(Back)` (see bezel-logo-back.md) |

---

## Tap targets

### Simple
- Music strip: the FULL pill opens fullscreen music (Fanart FS).
- On Fanart FS, the big album or the fanart opens Play Next.
- On Play Next, the side tiles play the previous or next track.

### How it works
- These are ordinary focusable controls, so a tap does the same thing as pressing Select on them.
- No extra touch-only logic is added.

### Wiring
| Where | Control | Action |
|---|---|---|
| Music strip | FS pill 6886 (`Includes_Bezel.xml` ~L2194) | `ActivateWindow(visualisation)` when `Player.HasAudio` |
| Fanart FS | big album / fanart | Play Next / Up Next (fanart-fs.md) |
| 1120 | tiles 6405 / 6406 | play offset −1 / +1 (play-next.md) |

---

## Double-tap Select (remote "touch")

### Simple
- With double-tap on: one press of Select still selects, after a short wait. Two quick presses open the options/info menu.
- The Tuner sets both whether this is on and how quick "quick" is.

### How it works
- `bz_dtap.py` runs as a loop. In a section window it times Select presses.
- **One press:** after the window expires, it sends a normal Select.
- **Two presses inside the window:** the Options+Info path (1119, or Kodi's ContextMenu); see context-menu.md.
- It works in windows only (the SECW list: pictures, programs, games, addonbrowser, playlists, PVR windows, and so on). It never acts in dialogs, the keyboard, the OSD or fullscreen video.
- The window length comes from `STEPS`.

### Wiring
| Item | Value |
|---|---|
| On/off | Tuner `dtap` → `Skin.HasSetting(bz_dtap_off)` (`BzATVal_dtap` ON/OFF) |
| Window | Tuner `dtapwin` → `bz_at_dtapwin`, 15 steps, `STEPS` = [150, 175, …, 600] ms |
| Script | `scripts/bz_dtap.py` (the same loop also runs the Tuner reload; see skin-settings-tuner.md) |

---

## Unknown / flagged
Earlier docs said a "Touch master On/Off" lived in the Tuner. No touch master row or skin setting exists in the live tree (searched Includes_Tuner.xml and the scripts). Treat it as not present.

## Related
keymaps.md · skin-settings-tuner.md · context-menu.md · bezel-logo-back.md · fanart-fs.md · play-next.md
